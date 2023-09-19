from ursina import *


class Info(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)

        gradient_v = Entity(model='quad', texture='vertical_gradient', parent=self,
                            rotation_z=180,
                            scale=(2, 1),
                            color=color.rgba(0, 0, 0, 180), z=8)

        guide_t = Text(parent=self, font="NanumSquareRoundB.ttf", text="'Q' 보드      'T' 노트",
                       origin=(-.5, .5), scale=(1, 1), x=-.4, y=.4, z=8)

        guide_b = Text(parent=self, font="NanumSquareRoundB.ttf", text="'W,A,S,D' 이동      'E' 상호작용:     "
                                                                       "'R' 추궁      'M' 배경음악 On/Off      'ESC' 메뉴선택",
                       origin=(-.5, .5), scale=(1, 1), x=-.4, y=-.45, z=8)

        title = Entity(parent=self, model='quad', texture='chapter_info', name='paper', color=color.white,
                       scale=(.4, .2), x=-.65, y=.36, z=8)

        clock = Entity(parent=self, model='quad', texture='clock', name='paper', color=color.white, origin=(-.5, .5),
                       scale=(.2, .14), x=.6, y=.45, z=8)

        tab = Entity(parent=self, model='quad', texture='tab_menu', name='paper', color=color.white,
                     origin=(0, .5), scale=(.5, .6), x=1.06, y=.25, z=8)
