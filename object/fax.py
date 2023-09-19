from ursina import *

from ui.component.fax_paper import FaxPaper


class Fax(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(scale=2, model='plane', collider='box', color=color.white, **kwargs)
        self.ui = None
        self.player = player
        for key, value in kwargs.items():
            setattr(self, key, value)

    def disable(self):
        self.ui.disable()
        super().disable()

    def input(self, key):
        if self.intersects(self.player) and key == 'e':
            self.ui = FaxPaper(player_data=self.player.data)
