from ursina import Entity, camera, color, Func
from ursina.prefabs.draggable import Draggable


class FindScene(Entity):

    def __init__(self):
        super().__init__(parent=camera.ui, model='quad', texture='inha_ware6_hall',
                         scale=(camera.aspect_ratio, 1), color=color.white, z=8)

        item1 = Draggable(model='quad', texture='paper', name='paper', color=color.white, origin=(-.5, .5),
                          scale=(.1, .1), z=-1)

        item2 = Draggable(model='quad', texture='glass', name='glass', color=color.white, origin=(-.5, .5),
                          scale=(.1, .1), z=-1)

        item1.parent = self
        item2.parent = self

    def input(self, key):
        if key == 'x':
            self.disable()
            Func(setattr, self, 'enabled', False)
