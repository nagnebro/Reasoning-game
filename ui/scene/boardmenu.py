from ursina import Entity, camera, color, Draggable, Text, Mesh, destroy, Func
from ui.component.inventory import Inventory


class BoardMenu(Entity):

    def __init__(self, player_data=None, resume=None):
        super().__init__(parent=camera.ui)
        self.player_data = player_data
        self.inventory = None
        self.line = None
        self.item = None
        self.resume = resume
        Entity(parent=self, model='quad', texture='board', scale=(camera.aspect_ratio, 1),
               color=color.white, z=4, world_y=0)
        Text(parent=self, font="NanumSquareRoundB.ttf", text="확인하고 싶은 아이템을 Drop",
             position=(-.2, .4, -1))
        Text(parent=self, font="NanumSquareRoundB.ttf", text="'Z' 가방\t'X' 닫기",
             position=(-.2, -.425, -1))

    def append(self, item):
        if self.item is not None:
            self.item.disable()
        self.item = Draggable(parent=self, model='quad', texture=item.texture, name=item, color=color.white,
                              scale=(.8, .8), z=-1, x=.3)
        if item.name == '블랙박스':
            self.item.on_click = Func(self.open_blackbox)
        if item.name == '아이폰':
            self.item.on_click = Func(self.open_gf_kakao)
        if item.name == '휴대폰':
            self.item.on_click = Func(self.open_stupr_kakao)

    def open_blackbox(self):
        Entity(parent=self.item, model='quad', texture='black_box_video.mp4',
               color=color.white, z=-1)

    def open_stupr_kakao(self):
        Entity(parent=self.item, model='quad', texture='stupr_kakao',
               color=color.white, z=-1)

    def open_gf_kakao(self):
        Entity(parent=self.item, model='quad', texture='exgf_kakao',
               color=color.white, z=-1)

    def disable(self):
        self.resume()
        super().disable()

    def input(self, key):
        if key == 'z':
            if self.inventory:
                print(self.player_data.name)
                self.inventory.disable()
                self.inventory = None
            else:
                self.inventory = Inventory(parent=self, player_data=self.player_data)
        if key == 'x':
            self.disable()
