from ursina import *


class Combine(Entity):

    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=.8,
            texture='combine_table',
            origin=(.5, .5),
            position=(.8, .4, 1),
            color=color.white
        )

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.items = []

        item0 = Entity(parent=self, origin=(0, .5),
                       scale=(.2, .2), x=-.64, y=-.13, z=-1)
        item1 = Entity(parent=self, origin=(0, .5),
                       scale=(.2, .2), x=-.36, y=-.13, z=-1)
        item2 = Entity(parent=self, origin=(0, .5),
                       scale=(.2, .2), x=-.77, y=-.4, z=-1)
        result = Entity(parent=self, origin=(0, .5),
                        scale=(.2, .2), x=-.5, y=-.4, z=-1)
        item3 = Entity(parent=self, origin=(0, .5),
                       scale=(.2, .2), x=-.23, y=-.4, z=-1)
        item4 = Entity(parent=self, origin=(0, .5),
                       scale=(.2, .2), x=-.64, y=-.67, z=-1)
        item5 = Entity(parent=self, origin=(0, .5),
                       scale=(.2, .2), x=-.36, y=-.67, z=-1)

        guide = Text(parent=self, font="NanumSquareRoundB.ttf", text="'V' 길게 눌러서 조합",
                     origin=(.5, .5), position=(1, -.9, -1))

    def append(self, item_name):
        print('add item:', item_name)

        item = Draggable(
            parent=self,
            model='quad',
            texture=item_name,
            name=item_name,
            color=color.white,
            scale_x=.2,
            scale_y=.125,
            origin=(0, .5),
            x=-.8 + (len(self.items) * 0.3),
            y=-.2,
            z=-.5,
        )
        self.items.append(item)
        item.drop = Func(self.drop, item)

    def drop(self, item):
        if item.x < 0 or item.x >= 1 or item.y > 0 or item.y <= -1:
            self.parent.append(item.name)
            if item in self.items:
                self.items.remove(item)
            item.disable()
            return

    def input(self, key):
        if key == 'v':
            for item in self.items:
                item.disable()
            self.items.clear()
            result_item = Draggable(
                parent=self,
                model='quad',
                texture='blueprint',
                name='blueprint',
                color=color.white,
                scale_x=.2,
                scale_y=.125,
                origin=(0, .5),
                x=-.5,
                y=-.6,
                z=-.5,
            )
            result_item.drop = Func(self.drop, result_item)
