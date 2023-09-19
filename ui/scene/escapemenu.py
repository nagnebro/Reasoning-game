from ursina import Entity, camera, color, Text, Button, Sequence, Func


class EscapeMenu(Entity):

    def __init__(self, resume, save_exit):
        super().__init__(parent=camera.ui)
        background = Entity(parent=self, model='quad', color=color.black50,
                            scale=(camera.aspect_ratio, 1), z=4)
        version = Text(parent=self, text="0.5.28.1. Early Access", color=color.light_gray,
                       scale=.8, origin=(-1, 0), x=-.98, y=-.48, z=1)
        btn_resume = Button(parent=self, font="NanumSquareRoundB.ttf", text="게임으로",
                            scale=(.2, .05), x=.0, y=.1, z=1)
        btn_save_exit = Button(parent=self, font="NanumSquareRoundB.ttf", text="저장하고 나가기",
                               scale=(.2, .05), x=.0, y=.0, z=1)
        btn_exit = Button(parent=self, font="NanumSquareRoundB.ttf", text="게임 종료",
                          scale=(.2, .05), x=.0, y=-.2, z=1)

        self.buttons = (btn_resume, btn_save_exit, btn_exit)
        for b in self.buttons:
            b.text_entity.font = "NanumSquareRoundB.ttf"
            b.text_entity.line_height = 1.15

        resume_sequence = Sequence()
        resume_sequence.append(Func(resume))
        resume_sequence.append(Func(self.disable))

        save_exit_sequence = Sequence()
        save_exit_sequence.append(Func(save_exit))
        save_exit_sequence.append(Func(self.disable))

        btn_resume.on_click = resume_sequence.start
        btn_save_exit.on_click = save_exit_sequence.start
        btn_exit.on_click = exit
