from ursina import *

from ui.scene.renscene import RenScene
from ursina import audio


class Npc(SpriteSheetAnimation):
    def __init__(self, field, **kwargs):
        super().__init__(**kwargs)
        self.field = field
        self.play_animation('idle')
        self.z = -0.5
        self.scale_y = 1.5
        self.scale_x = 0.9
        self.count = 1  # 대화횟수를 세기 위한 count 횟수
        self.url = ""
        self.voice = None
        self.conversation = None
        self.collider = BoxCollider(self, size=(1, 1, 3))

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):

        if self.intersects(self.target) and key == 'e':
            self.url = self.name + str(self.count)  # count로 대화횟수 count
            Audio(self.url, loop=False)  # 말건 횟수에 맞게 보이스 재생
            self.conversation = RenScene(
                background=self.background,
                script=self.script,
                font="NanumSquareRoundR.ttf",
                variables_object=self.target.data
            )

            if self.count < 3:
                self.count += 1

        elif self.intersects(self.target) and key == 'r' and self.count > 1:
            self.url = self.name + str(self.count)  # count로 대화횟수 count
            Audio(self.url, loop=False)  # 말건 횟수에 맞게 보이스 재생
            self.conversation = RenScene(
                background=self.background,
                script=self.script2,
                font="NanumSquareRoundR.ttf",
                variables_object=self.target.data
            )
            if self.count < 3:
                self.count += 1

    def update(self):
        self.visible = self.field.visible
