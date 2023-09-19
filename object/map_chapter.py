from ursina import *

from object.fax import Fax
from object.find_place import FindPlace
from object.sprite_map import SpriteMap
from object.npc import Npc
from object.player import Player
from object.wall import Wall


class MapChapter(Entity):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.proviso = Entity()

        wall = Wall(parent=self)

        self.player = Player(game.player_data, wall)
        self.player.position = game.player_data.position
        # 여기서 player 객체를 생성, mapchapter는 새게임이나 계속하기 선택시 실행되는 파일임.
        # game.py 파일에서 계속 data를 저장하고 있는 상태.
        self.passed = False
        self.pro_passed = False

        # 맵 초기화
        camera.orthographic = True
        camera.position = (0, 0)
        camera.fov = 12
        Sky(color=color.hex('4A4C50'))

        hall1 = SpriteMap(parent=self, texture='map_hall1', player=self.player, position=(0, 0, 1))
        Npc(texture='px_stu_pr', parent=self, tileset_size=(12, 1), fps=4, animations={'idle': ((0, 0), (11, 0)),},
            name='stupr', image='stu_pr_0', background='entrance1', script2= 'chapter1/chapter1_ask.txt' ,
            script='chapter1/chapter1.txt', target=self.player, position=(-14, -1, -1), field=hall1)

        Npc(texture='px_gradu_back', parent=self, tileset_size=(6, 1), fps=3, animations={'idle': ((0, 0), (5, 0)),},
            name='gradu', image='gradu_0', background='third_floor',script2= 'chapter2/chapter2_ask.txt' ,
            script='chapter2/chapter2.txt', target=self.player, position=(-3, -1.4, -1), field=hall1)

        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=2,
                                 name='복도', model='cube', scale=(4, 1), position=(-6, -1.5),
                                 collider='box', color=color.white50, field=hall1)

        restroom = SpriteMap(parent=self, texture='map_restroom', player=self.player, position=(-14.1, 7.15, 1))
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=1,
                                 name='화장실', model='quad', position=(-14, 4),
                                 collider='box', color=color.white50, field=restroom)

        club_room = SpriteMap(parent=self, texture='map_club_room', player=self.player, position=(1.5, 9.85, 1))
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=3,
                                 name='동아리실', model='quad', scale=(1, 2), position=(1.6, 15),
                                 collider='box', color=color.white50, field=club_room)
        Npc(texture='px_club_leader', parent=self, tileset_size=(6, 1), fps=5, animations={'idle': ((0, 0), (5, 0)),},
            name='club_leader', image='club_leader_0', background='second_floor1',script2= 'chapter3/chapter3_ask.txt' ,
            script='chapter3/chapter3.txt', target=self.player, position=(3, 6.5, -1), field=club_room)

        # 인하군의 캐비넷 proviso 추가
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=6,
                                 name='동아리실 캐비넷', model='quad', position=(8, 13.5),
                                 collider='box', color=color.gray, field=club_room)

        hall2 = SpriteMap(parent=self, texture='map_hall2', player=self.player, position=(18.42, 5.35, 1))
        Npc(texture='px_ex_gf', parent=self, tileset_size=(6, 1), fps=3, animations={'idle': ((0, 0), (5, 0)), },
            name='ex_gf', image='ex_gf_0', background='gf1',script2= 'chapter5/chapter5_ask.txt' ,
            script='chapter5/chapter5.txt', target=self.player, position=(18, 6), field=hall2)

        dorm_room = SpriteMap(parent=self, texture='map_dorm_room', player=self.player, position=(24, 13.65))
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=5,
                                 name='자취방', model='cube', position=(22.5, 10),
                                 collider='box', color=color.white50, field=dorm_room)

        parking_lot = SpriteMap(parent=self, texture='map_parking_lot', player=self.player, position=(.5, -9.5, 1))
        Npc(texture='px_prof_nam', parent=self, tileset_size=(12, 1), fps=4, animations={'idle': ((3, 0), (6, 0)), },
            name='prof_nam', image='prof_nam_0', background='parking_lot',
            script='chapter4/chapter4.txt', target=self.player, position=(12, -10), field=parking_lot)
        self.proviso = FindPlace(parent=self, player=self.player, game=self.game, number=4,
                                 name='주차장', model='quad', scale=(2,3), position=(13.5, -14),
                                 collider='box', color=color.white50, field=parking_lot)

        SpriteMap(parent=self, texture='map_hall3', player=self.player, position=(23, 0.58, 1))

        office = SpriteMap(parent=self, texture='map_office', player=self.player, position=(33.5, -3.5, 1))
        Fax(parent=self, player=self.player, position=(39, 1))

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        camera.position = (self.player.x, self.player.y)
