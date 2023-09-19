from ursina import *


class SpriteMap(Sprite):
    def __init__(self, player, **kwargs):
        super().__init__(model='quad', collider='box', scale=2, **kwargs)
        self.player = player

    def update(self):
        if self.intersects(self.player):
            self.visible = True
        else:
            self.visible = False
