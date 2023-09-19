from ursina import *

from data.record_data import GameRecordData
from ui.unuse.sprite_sheet_animation_unloop import SpriteSheetAnimationUnloop


class NoteAnim(SpriteSheetAnimationUnloop):
    def __init__(self, player_data, resume=None):
        super().__init__('Note', tileset_size=(17, 3), y=.05,
                         scale=1.6, fps=8, parent=camera.ui, animations={
            'open': ((1, 2), (16, 2)),
            'flip_left': ((1, 1), (8, 1)),
            'flip_right': ((1, 0), (8, 0)),
        })
        self.play_animation('open')

        self.index = 0

        self.text_title = Text(parent=self, font="NanumSquareRoundB.ttf", text='', position=(0, .2, -1))
        self.text_desc = Text(parent=self, font="NanumSquareRoundR.ttf", text='', position=(0, .1, -1))

        self.resume = resume
        print(player_data.record_titles)

        self.recordData = GameRecordData()
        self.playerRecordData = []
        for record_title in player_data.record_titles:
            self.playerRecordData.append(self.recordData.record[record_title])
        if len(self.playerRecordData) != 0:
            self.print_record(0)

    def print_record(self, index):
        self.text_title.text = self.playerRecordData[index].name
        self.text_desc.text = self.playerRecordData[index].desc

    def next_page(self):
        self.play_animation('flip_left')
        # 인덱스가 전체 기록 수 보다 클 경우, 다음 페이지 없음
        if self.index >= len(self.playerRecordData):
            return
        else:
            self.print_record(self.index)

    def prev_page(self):
        self.play_animation('flip_right')
        # 인덱스가 0 보다 작을 경우, 이전 페이지 없음
        if self.index >= 0:
            return
        else:
            self.print_record(self.index)

    def disable(self):
        self.resume()
        super().disable()

    def input(self, key):
        if key == 'x':
            self.disable()
        if key == 'z':
            self.next_page()
        if key == 'c':
            self.prev_page()