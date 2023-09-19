from ursina import *

from ui.component.proviso import Proviso
from ui.scene.renscene import RenScene


class FindProviso(Entity):
    def __init__(self, player_data, item_data, number, **kwargs):
        super().__init__(parent=camera.ui, **kwargs)
        self.item_data = item_data
        self.player_data = player_data
        self.pro_passed = False

        # Mybutton의 클래스 변수로 mapchapter에서 넘겨받은 player의 data를 넘겨준다.
        Proviso.player_data = player_data

        # x,y좌표는 2차원 좌표평면을 기준으로한다 따라서 x,y가 양수면 1사분면, 즉 우측위쪽으로 이동한다.
        # parent 속성은 카메라 시점을 선택한다.
        # camera.aspect_ratio 는 camera, 즉 창에 꽉차게끔 객체를 집어넣는다.
        # 현재 유저의 인벤토리와 증거끼리 비교해서 인벤토리에 있는 증거라면 단서 수집 화면에서 disable처리함.
        def compare_inventory(proviso_list):
            for i in proviso_list:
                for j in player_data.inventory:
                    if i.name == j.name:
                        i.disable()

        # proviso = 1의 속성은 각 용의자에 해당하는 단서의 아이디값으로 조합시에 이용하면 됨.
        if number == 1:
            background = Entity(parent=self, model='quad', texture='restroom', color=color.white,
                                scale=(camera.aspect_ratio, 1))
            self.item1_1 = item_data.item["떨어진 영수증"]
            self.item1_2 = item_data.item["내려치기 딱 좋은 망치"]
            self.item1_3 = item_data.item["화학약품"]
            self.item1_4 = item_data.item["휴대폰"]

            proviso1_1 = Proviso(parent=self, model='quad', texture=self.item1_1.texture, color=color.white, scale=0.05,
                                 position=(-.6, -.3, 0), name=self.item1_1.name, proviso=self.item1_1.chapter_no,
                                 desc=self.item1_1.desc)
            proviso1_2 = Proviso(parent=self, model='quad', texture=self.item1_2.texture, color=color.white, scale=.1,
                                 position=(-.4, .1, 0), name=self.item1_2.name, proviso=self.item1_2.chapter_no,
                                 desc=self.item1_2.desc)
            proviso1_3 = Proviso(parent=self, model='quad', texture=self.item1_3.texture, color=color.white, scale=.07,
                                 position=(-.85, .18, 0), name=self.item1_3.name, proviso=self.item1_3.chapter_no,
                                 desc=self.item1_3.desc)
            proviso1_4 = Proviso(parent=self, model='quad', texture=self.item1_4.texture, color=color.white, scale=.1,
                                 position=(0, -.2, 0), name=self.item1_4.name, proviso=self.item1_4.chapter_no,
                                 desc=self.item1_4.desc)

            proviso_list1 = [proviso1_1, proviso1_2, proviso1_3, proviso1_4]
            compare_inventory(proviso_list1)

        elif number == 2:
            self.item2_1 = item_data.item["책"]
            self.item2_2 = item_data.item["벽돌"]
            self.item2_3 = item_data.item["롤 경기장 티켓"]
            self.item2_4 = item_data.item["ph 종이"]
            self.item2_5 = item_data.item["배터리"]
            background = Entity(parent=self, model='quad', texture='inner_cabinet', colr=color.white,
                                scale=(camera.aspect_ratio, 1), )
            proviso2_1 = Proviso(parent=self, model='quad', texture=self.item2_1.texture, color=color.white, scale=.2,
                                 position=(-0.1, -0.2, 0), name=self.item2_1.name, proviso=self.item2_1.chapter_no,
                                 desc=self.item2_1.desc)
            proviso2_2 = Proviso(parent=self, model='quad', texture=self.item2_2.texture, color=color.white, scale=.4,
                                 position=(0.15, -0.25, -1), name=self.item2_2.name, proviso=self.item2_2.chapter_no,
                                 desc=self.item2_2.desc)
            proviso2_3 = Proviso(parent=self, model='quad', texture=self.item2_3.texture, color=color.white, scale=.1,
                                 position=(0.1, -0.1, 0), name=self.item2_3.name, proviso=self.item2_3.chapter_no,
                                 desc=self.item2_3.desc)
            proviso2_4 = Proviso(parent=self, model='quad', texture=self.item2_4.texture, color=color.white, scale=.1,
                                 position=(0, -0.3, 0), name=self.item2_4.name, proviso=self.item2_4.chapter_no,
                                 desc=self.item2_4.desc)
            proviso2_5 = Proviso(parent=self, model='quad', texture=self.item2_5.texture, color=color.white, scale=.3,
                                 position=(-0.2, -0.3, 0), name=self.item2_5.name, proviso=self.item2_5.chapter_no,
                                 desc=self.item2_5.desc)

            proviso_list2 = [proviso2_1, proviso2_2, proviso2_3, proviso2_4, proviso2_5]
            compare_inventory(proviso_list2)

        elif number == 3:

            self.item3_1 = item_data.item["커터칼"]
            self.item3_2 = item_data.item["쪽지"]
            self.item3_3 = item_data.item["밧줄"]
            self.item3_4 = item_data.item["후드티"]

            background = Entity(parent=self, model='quad', texture='big_cabinet_open1', colr=color.white,
                                scale=(camera.aspect_ratio, 1))

            proviso3_1 = Proviso(parent=self, model='quad', texture=self.item3_1.texture, color=color.white, scale=.2,
                                 position=(-0.4, -0.1, 0), name=self.item3_1.name, proviso=self.item3_1.chapter_no,
                                 desc=self.item3_1.desc)

            proviso3_2 = Proviso(parent=self, model='quad', texture=self.item3_2.texture, color=color.white, scale=.1,
                                 position=(-0.55, 0.15, 0), name=self.item3_2.name, proviso=self.item3_2.chapter_no,
                                 desc=self.item3_2.desc)

            proviso3_3 = Proviso(parent=self, model='quad', texture=self.item3_3.texture, color=color.white, scale=.3,
                                 rotation_z=90,
                                 position=(-0.4, 0.1, 0), name=self.item3_3.name, proviso=self.item3_3.chapter_no,
                                 desc=self.item3_3.desc)

            proviso3_4 = Proviso(parent=self, model='quad', texture=self.item3_4.texture, color=color.white, scale=.2,
                                 position=(-0.6, -0.1, 0), name=self.item3_4.name, proviso=self.item3_4.chapter_no,
                                 desc=self.item3_4.desc)

            proviso_list2 = [proviso3_1, proviso3_2, proviso3_3, proviso3_4]
            compare_inventory(proviso_list2)

        elif number == 4:

            self.item4_1 = item_data.item["비상용 망치"]
            self.item4_2 = item_data.item["조교 리스트"]
            self.item4_3 = item_data.item["블랙박스"]

            background = Entity(parent=self, model='quad', texture='under_car', colr=color.white,
                                scale=(camera.aspect_ratio, 1))

            proviso4_1 = Proviso(parent=self, model='quad', texture=self.item4_1.texture, color=color.white, scale=.2,
                                 position=(-.4, .1, 0), name=self.item4_1.name, proviso=self.item4_1.chapter_no,
                                 desc=self.item4_1.desc)

            proviso4_2 = Proviso(parent=self, model='quad', texture=self.item4_2.texture, color=color.white, scale=.2,
                                 position=(.0, .1, 0), name=self.item4_2.name, proviso=self.item4_2.chapter_no,
                                 desc=self.item4_2.desc)

            proviso4_3 = Proviso(parent=self, model='quad', texture=self.item4_3.texture, color=color.white, scale=.2,
                                 position=(.4, .1, 0), name=self.item4_3.name, proviso=self.item4_3.chapter_no,
                                 desc=self.item4_3.desc)

            proviso_list2 = [proviso4_1, proviso4_2, proviso4_3]
            compare_inventory(proviso_list2)

        elif number == 5:

            self.item5_1 = item_data.item["커플사진"]
            self.item5_2 = item_data.item["일기"]
            self.item5_3 = item_data.item["아이폰"]
            self.item5_4 = item_data.item["숫돌"]

            background = Entity(parent=self, model='quad', texture='gf1', colr=color.white,
                                scale=(camera.aspect_ratio, 1))

            proviso5_1 = Proviso(parent=self, model='quad', texture=self.item5_1.texture, color=color.white, scale=.2,
                                 position=(-.4, .4, 0), name=self.item5_1.name, proviso=self.item5_1.chapter_no,
                                 desc=self.item5_1.desc)

            proviso5_2 = Proviso(parent=self, model='quad', texture=self.item5_2.texture, color=color.white, scale=.1,
                                 position=(-.2, -.4, 0), name=self.item5_2.name, proviso=self.item5_2.chapter_no,
                                 desc=self.item5_2.desc)

            proviso5_3 = Proviso(parent=self, model='quad', texture=self.item5_3.texture, color=color.white, scale=.2,
                                 position=(.5, -.1, 0), name=self.item5_3.name, proviso=self.item5_3.chapter_no,
                                 desc=self.item5_3.desc)

            proviso5_4 = Proviso(parent=self, model='quad', texture=self.item5_4.texture, color=color.white, scale=.2,
                                 position=(0, -.3, 0), name=self.item5_4.name, proviso=self.item5_4.chapter_no,
                                 desc=self.item5_4.desc)

            proviso_list2 = [proviso5_1, proviso5_2, proviso5_3, proviso5_4]
            compare_inventory(proviso_list2)

        elif number == 6:  # 동아리실의 캐비넷 추가 , 단서는 따로 없고 사물함만 있다.

            background = Entity(parent=self, model='quad', texture='close_cabinet2', colr=color.white,
                                scale=(camera.aspect_ratio, 1), z=3)

            btn = Button(parent=self, model='quad', scale=0.18, position=(-0.07, -0.05, -1))

            # btn.hovered = False
            btn.color = color.rgba(1, 1, 1, 0)
            btn.pressed_color = color.rgba(1, 1, 1, 0)
            btn.highlight_color = color.rgba(1, 1, 1, 0)

            btn.on_click = Func(self.find_poison, background)

    def input(self, key):
        if key == 'x':
            print(key)
            self.disable()

    def find_poison(self, background):
        print(type(background.texture))
        if str(background.texture) == 'close_cabinet2.png':  # 예외처리
            background.texture = 'cabinet_poison'
            self.player_data.print_npc = False
            RenScene(
                background=None,
                script='open_cabinet.txt',
                font="NanumSquareRoundR.ttf",
                variables_object=self.player_data
            )

    def find_cabinet(self):
        print("실행")

        self.player_data.print_npc = False
        r = RenScene(
            background=None,
            script='find_cabinet.txt',
            font="NanumSquareRoundR.ttf",
            variables_object=self.player_data,

        )
