from ursina import *


class Player(SpriteSheetAnimation):
    def __init__(self, data, wall, **kwargs):  # 여기서 data는 player_data클래스의 player_data 객체를 뜻한다.
        super().__init__('px_detective', tileset_size=(24, 3), fps=8, animations={
            'idle_up': ((1, 2), (1, 2)),
            'idle_down': ((3, 2), (3, 2)),
            'idle_left': ((2, 2), (2, 2)),
            'idle_right': ((0, 2), (0, 2)),

            'walk_down': ((18, 0), (23, 0)),
            'walk_up': ((6, 0), (11, 0)),
            'walk_left': ((12, 0), (17, 0)),
            'walk_right': ((0, 0), (5, 0)),
        })
        self.wall = wall

        self.collider = BoxCollider(self, size=(1, 1, 3))
        self.data = data
        self.position = (1, 0)
        self.origin = (0, 0, 1)
        self.play_animation('idle_right')
        self.scale_y = 1.5
        self.scale_x = 0.9
        self.scale_z = 1

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'w up':
            self.play_animation('idle_up')
        elif key == 's up':
            self.play_animation('idle_down')
        elif key == 'a up':
            self.play_animation('idle_left')
        elif key == 'd up':
            self.play_animation('idle_right')
        elif key == 'd':
            self.play_animation('walk_right')
        elif key == 'a':
            self.play_animation('walk_left')
        elif key == 'w':
            self.play_animation('walk_up')
        elif key == 's':
            self.play_animation('walk_down')

    def update(self):
        if not self.intersects(self.wall):
            self.y += held_keys['w'] * time.dt * 8
            self.y -= held_keys['s'] * time.dt * 8
            self.x += held_keys['d'] * time.dt * 8
            self.x -= held_keys['a'] * time.dt * 8
        else:
            if self.intersects(self.wall).normal != Vec3(0, -1, 0):
                self.y += held_keys['w'] * time.dt * 8
            if self.intersects(self.wall).normal != Vec3(0, 1, 0):
                self.y -= held_keys['s'] * time.dt * 8
            if self.intersects(self.wall).normal != Vec3(-1, 0, 0):
                self.x += held_keys['d'] * time.dt * 8
            if self.intersects(self.wall).normal != Vec3(1, 0, 0):
                self.x -= held_keys['a'] * time.dt * 8
