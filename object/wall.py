from ursina import Entity, color


class Wall(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 외벽
        ex_color = color.clear
        in_color = color.clear

        # 확인용 포인트
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(0, 0), color=color.azure)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(0, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(0, -20), color=ex_color)
        #
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(10, 10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(10, 0), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(10, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(10, -20), color=ex_color)
        #
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(20, 10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(20, 0), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(20, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(20, -20), color=ex_color)
        #
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(30, 10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(30, 0), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(30, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(30, -20), color=ex_color)
        #
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(40, 10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(40, 0), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(40, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(40, -20), color=ex_color)
        #
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-10, 10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-10, 0), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-10, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-10, -20), color=ex_color)
        #
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-20, 10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-20, 0), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-20, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-20, -20), color=ex_color)
        #
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-30, 10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-30, 0), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-30, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-30, -20), color=ex_color)
        #
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-40, 10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-40, 0), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-40, -10), color=ex_color)
        # Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(-40, -20), color=ex_color)

        # 화장실/세로
        Entity(parent=self, model='quad', scale=(1, 8), collider='box', position=(-19, 7), color=ex_color)
        Entity(parent=self, model='quad', scale=(1, 8), collider='box', position=(-9.1, 7), color=ex_color)
        # 화장실/가로
        Entity(parent=self, model='quad', scale=(10, 3), collider='box', position=(-14, 9.5), color=ex_color)
        Entity(parent=self, model='quad', scale=(4, 1), collider='box', position=(-11, 3), color=ex_color)
        Entity(parent=self, model='quad', scale=(4, 1), collider='box', position=(-17, 3), color=ex_color)

        # 동아리실/세로
        Entity(parent=self, model='quad', scale=(1, 14), collider='box', position=(-6.8, 11), color=ex_color)
        Entity(parent=self, model='quad', scale=(1, 14), collider='box', position=(10, 11), color=ex_color)
        Entity(parent=self, model='quad', scale=(3, 4), collider='box', position=(-0.5, 14), color=ex_color)
        # 동아리실/가로
        Entity(parent=self, model='quad', scale=(18, 1), collider='box', position=(2, 15), color=ex_color)
        # 동아리실/가로/하단
        Entity(parent=self, model='quad', scale=(6, 2), collider='box', position=(-5.5, 3.5), color=ex_color)
        Entity(parent=self, model='quad', scale=(10, 2), collider='box', position=(5, 3.5), color=ex_color)

        # 복도/세로
        Entity(parent=self, model='quad', scale=(1, 5), collider='box', position=(-15.5, 0), color=ex_color)
        Entity(parent=self, model='quad', scale=(6, 6), collider='box', position=(18.5, 0), color=ex_color)
        # 복도/가로
        Entity(parent=self, model='quad', scale=(11, 1), collider='box', position=(-8, 2.5), color=ex_color)
        Entity(parent=self, model='quad', scale=(13, 1), collider='box', position=(6.5, 2.5), color=ex_color)
        # 복도/가로/하단
        Entity(parent=self, model='quad', scale=(24.5, 3), collider='box', position=(0, -3.6), color=ex_color)
        Entity(parent=self, model='quad', scale=(3, 3), collider='box', position=(-15.5, -3.6), color=ex_color)
        Entity(parent=self, model='quad', scale=(3, 3), collider='box', position=(15.5, -3.6), color=ex_color)

        # 복도2/세로
        Entity(parent=self, model='quad', scale=(2, 5), collider='box', position=(11.5, 5), color=ex_color)
        Entity(parent=self, model='quad', scale=(1, 7), collider='box', position=(24, 6), color=ex_color)
        # 복도2/가로
        Entity(parent=self, model='quad', scale=(10, 3), collider='box', position=(17, 8), color=ex_color)

        # 기숙사/세로
        Entity(parent=self, model='quad', scale=(1, 10), collider='box', position=(17, 14), color=ex_color)
        Entity(parent=self, model='quad', scale=(1, 10), collider='box', position=(29, 14), color=ex_color)
        # 기숙사/가로
        Entity(parent=self, model='quad', scale=(15, 1), collider='box', position=(24, 17), color=ex_color)
        Entity(parent=self, model='quad', scale=(6, 1), collider='box', position=(27, 9), color=ex_color)
        # 기숙사/내벽
        Entity(parent=self, model='quad', scale=(2, 3), collider='box', position=(18.5, 14.5), color=in_color)
        Entity(parent=self, model='quad', scale=(3, 1.5), collider='box', position=(25, 12.5), color=in_color)

        # 복도3
        Entity(parent=self, model='quad', scale=(6, 2), collider='box', position=(23, -2), color=ex_color)
        Entity(parent=self, model='quad', scale=(2, 3), collider='box', position=(25, 3), color=ex_color)

        # 주차장/세로
        Entity(parent=self, model='quad', scale=(1, 16), collider='box', position=(-21, -13), color=ex_color)
        Entity(parent=self, model='quad', scale=(1, 16), collider='box', position=(21, -13), color=ex_color)
        # 주차장/가로
        Entity(parent=self, model='quad', scale=(4, 1), collider='box', position=(-18, -5), color=ex_color)
        Entity(parent=self, model='quad', scale=(4, 1), collider='box', position=(18, -5), color=ex_color)
        Entity(parent=self, model='quad', scale=(46, 1), collider='box', position=(0, -15), color=ex_color)

        # 사무실/세로
        Entity(parent=self, model='quad', scale=(1, 3), collider='box', position=(26.5, 3), color=ex_color)
        Entity(parent=self, model='quad', scale=(1, 4), collider='box', position=(26.5, -3.5), color=ex_color)
        Entity(parent=self, model='quad', scale=(2.5, 5), collider='box', position=(28.5, -7.5), color=ex_color)
        Entity(parent=self, model='quad', scale=(1, 15), collider='box', position=(40.5, -3.5), color=ex_color)
        # 사무실/가로
        Entity(parent=self, model='quad', scale=(15, 1), collider='box', position=(34, 4), color=ex_color)
        Entity(parent=self, model='quad', scale=(14, 1), collider='box', position=(35, -11), color=ex_color)
        # 사무실/내벽
        Entity(parent=self, model='quad', scale=(1, 1), collider='box', position=(39, 1), color=in_color)
        Entity(parent=self, model='quad', scale=(11, 1), collider='box', position=(33.5, -2.5), color=in_color)
        Entity(parent=self, model='quad', scale=(6, 1), collider='box', position=(32.2, -5.5), color=in_color)
        Entity(parent=self, model='quad', scale=(3, 1), collider='box', position=(38, -5.5), color=in_color)


