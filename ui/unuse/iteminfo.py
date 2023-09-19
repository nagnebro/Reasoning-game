from ursina import *


class ItemInfo(Entity):

    def __init__(self, variables_object=None, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='white_cube',
            texture_scale=(1, 1),
            scale=(1, .6),
            origin=(0, 0),
            position=(0, 0, 7),
            color=color.color(0, 0, .1, .9)
        )

        icon = Entity(parent=self, model='quad', texture='paper', name='paper', color=color.white, origin=(-.5, .5),
                          scale=(.2, .2), x=-.4, y=.2, z=-1)

        item_name = Text(parent=camera.ui, font="NanumSquareRoundB.ttf", text="아이템:어쩌구저쩌구",
                         origin=(-.5, .5), scale=(1, 1), y=.2, z=-1)
