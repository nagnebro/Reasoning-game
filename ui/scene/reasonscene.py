from ursina import Entity, dedent, camera, color, Button

from ui.component.renconversation import RenConversation


class ReasonScene(Entity):

    def __init__(self, player):
        super().__init__(parent=camera.ui)

        conversation = RenConversation(parent=self, font='NanumSquareRoundR.ttf')
        with open('_resources/script/reasoning.txt', 'r', encoding='UTF8') as file:
            # open(파일 경로, r/w, 인코딩)

            data = file.read()
            convo = dedent(data)
            conversation.start_conversation(convo)

        background = Entity(parent=self, model='quad', texture='',
                            scale=(camera.aspect_ratio, 1),
                            color=color.white, z=4, world_y=0)

        print(player.inventory)

        Button(parent=self, texture='stu_pr_0',
               scale=.4, color=color.white, x=-.6)

        Button(parent=self, texture='gradu_0',
               scale=.4, color=color.white, x=-.3)

        Button(parent=self, texture='club_leader_0',
               scale=.5, color=color.white, x=0, y=.05)

        Button(parent=self, texture='prof_nam_0',
               scale=.4, color=color.white, x=.3)

        Button(parent=self, texture='ex_gf_0',
               scale=.5, color=color.white, x=.6, y=.05)