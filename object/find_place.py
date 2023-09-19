from ursina import *

from ui.scene.findproviso import FindProviso
from ui.scene.renscene import RenScene


class FindPlace(Entity):
    def __init__(self, player, game, number, field, **kwargs):
        super().__init__(**kwargs)
        self.player = player
        self.pro_passed = False
        self.number = number
        self.field = field

        self.proviso = FindProviso(self.player.data, game.item_data, number)
        self.proviso.disable()

    def input(self, key):
        # 단서수집 포탈 근처에 갔을 떄 키를 눌러야 동작하게끔(Npc와 말거는 거처럼)
        if self.intersects(self.player) and key == 'e':

            if self.number == 6 and not self.proviso.enabled:
                self.proviso.find_cabinet()
                print("실행")

            if not self.proviso.enabled:
                self.proviso.enable()

    def update(self):
        self.visible = self.field.visible
