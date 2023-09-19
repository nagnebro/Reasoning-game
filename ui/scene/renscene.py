from ursina import Entity, dedent, camera, color

from ui.component.renconversation import RenConversation


class RenScene(Entity):

    def __init__(self, background, script, font, no_background=False,
                 variables_object=None):
        # variables_object = None이라는 것은 매개변수값으로 아무것도 들어오지 않을시
        # default값으로 none을 집어넣겠다는 것.

        super().__init__(parent=camera.ui)

        self.conversation = RenConversation(parent=self, font=font, variables_object=variables_object)
        with open('_resources/script/' + script, 'r', encoding='UTF8') as file:
            # open(파일 경로, r/w, 인코딩)

            data = file.read()
            convo = dedent(data)
            self.conversation.start_conversation(convo)

        self.gradient_v = Entity(model='quad', texture='vertical_gradient', parent=self.conversation,
                                 rotation_z=180,
                                 scale=(2, 1),
                                 color=color.rgba(0, 0, 0, 180), world_y=0, z=2)

        self.background = Entity(parent=self.conversation, model='quad', texture=background,
                                 scale=(camera.aspect_ratio, 1),
                                 color=color.white, z=4, world_y=0)