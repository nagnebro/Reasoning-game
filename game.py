import time

from ursina import Entity, Audio, camera, color, Func, invoke
from data.item_data import GameItemData
from object.map_chapter import MapChapter
from ui.component.note import Note
from ui.scene.boardmenu import BoardMenu
from ui.scene.escapemenu import EscapeMenu
from ui.scene.mainmenu import MainMenu
from ui.component.info import Info
from ui.scene.renscene import RenScene
import pickle
import threading


class Game(Entity):

    def __init__(self, player_name, menu=MainMenu):
        super().__init__()
        self.player_data = None
        self.item_data = GameItemData()
        self.load_player_data(player_name)
        self.menu = menu(game=self)

        self.ui = None
        self.chapter = None
        self.object_list = [self, self.menu]
        self.sound = Audio("_resources/sound/background_music.wav", loop=True, volume=.5)  # 배경음악 삽입.
        self.sound.play()  # 들으면서 하면 음침해서 꺼놨음. 정상작동함.

    def load_player_data(self, player_name):
        try:
            with open(player_name + '.pickle', 'rb') as file:
                self.player_data = pickle.load(file)
        except FileNotFoundError:
            return None

    def save_player_data(self, player_data):
        with open(player_data.name + '.pickle', 'wb') as file:
            pickle.dump(player_data, file)
        self.load_player_data(player_data.name)

    def start_prologue(self):
        self.player_data.print_npc = False
        RenScene(
            background='opening_background',
            script="prologue.txt",
            font="NanumSquareRoundR.ttf",
            variables_object=self.player_data,
        )

    def start_video(self):

        self.tmp = Entity(parent=camera.ui, model='quad', scale=(camera.aspect_ratio, 1), color=color.black)

        time.sleep(3)

        self.video = Entity(parent=camera.ui, model='quad', scale=(camera.aspect_ratio, 1), z=-3,
                            texture='prologue.mp4')
        self.sound = Audio("_resources/video/prologue.mp4", loop=False)
        time.sleep(8)
        self.start_prologue()
        self.tmp.disable()
        self.video.disable()
    # def start_video(self):  # --> invoke opening
    #     video = Entity(parent=camera.ui, model='quad', scale=(camera.aspect_ratio, 1), color=color.black)
    #     invoke(setattr, video, 'texture', 'prologue.mp4', delay=5)
    #     invoke(setattr, video, 'color', color.white, delay=5)
    #     invoke(Audio, 'prologue.mp4', delay=5)
    #
    #     invoke(Func(video.disable), delay=13)
    #     invoke(self.start_prologue, delay=13)

    def start_chapter(self, bool):
        if bool:  # 재시작일 경우 False , New Game True
            thread1 = threading.Thread(target=self.start_video)
            thread1.start()
            self.menu.disable()
            # print(self.menu)
            # self.menu.disable()
            self.ui = Info()
            self.chapter = MapChapter(self)
            self.player_data.screenlist = [self.ui, self.chapter, self.menu]

    def open_board(self):
        self.ui.disable()
        self.menu = BoardMenu(self.player_data, self.ui.enable)

    def open_note(self):
        self.ui.disable()
        self.menu = Note(self.player_data, self.ui.enable)

    def open_escape(self):
        self.ui.disable()
        self.menu = EscapeMenu(self.ui.enable, self.save_exit)

    def save_exit(self):
        self.save_player_data(player_data=self.player_data)
        print('save and exit')
        exit()

    def input(self, key):
        if key == 'q':
            self.open_board()
        elif key == 't':
            self.open_note()
        elif key == 'escape':
            self.open_escape()
        elif key == 'm':  # 배경음악끄기 mute
            if self.sound.loop:
                print('hi')
                self.sound.loop = False
                self.sound.stop()
                return
            self.sound.loop = True
            self.sound.play()
