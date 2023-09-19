from ursina import *
from data.record_data import GameRecordData


class Note(Sprite):
    def __init__(self, player_data, resume=None):
        super().__init__('note_stu_pr', scale=.072, parent=camera.ui, z=5)

        self.guide = Text(parent=camera.ui, font="NanumSquareRoundB.ttf",
                          text="'Z' 이전 페이지      'X' 닫기      'C' 다음 페이지",
                          position=(-.2, -.425, -1))

        self.text_desc = Text(parent=camera.ui, font="NanumSquareRoundR.ttf", text='',
                              color=color.black, position=(.08, .35, -1))

        self.resume = resume

        self.index = 0
        self.items = []
        self.item_object = None
        self.inventoryData = player_data.inventory

        self.recordData = GameRecordData()
        self.playerRecordData = {'stu_pr': [], 'gradu': [], 'club_leader': [], 'prof_nam': [], 'ex_gf': []}

        for record_title in player_data.record_titles:
            record = self.recordData.record[record_title]
            self.playerRecordData[record.npc_name].append(record)
        if len(self.playerRecordData) != 0:
            self.print_record('stu_pr')
            self.print_proviso()

    def print_proviso(self):
        if self.item_object is not None:
            self.item_object.disable()
        self.item_object = Entity(parent=self, model='quad', scale=(1, 1), color=color.clear)
        count = 0
        for item in self.inventoryData:
            if item.proviso == self.index + 1:
                count += 1
                self.items.append(
                    Entity(parent=self.item_object, model='quad', texture=item.texture, name=item, color=color.white,
                           scale=(.08, .08), x=-.32 + count * 0.05, y=-.2, z=-1))

    def print_record(self, npc_name):
        self.texture = 'note_' + npc_name
        self.text_desc.text = ''

        for data in self.playerRecordData[npc_name]: # 단서 길이에 따른 자동 띄어쓰기 추가
            self.text_desc.text += data.title + ':\n'
            tmp = data.desc
            while len(tmp) > 33 :

                self.text_desc.text += '\n' + tmp[:32]

                tmp = tmp[32:]

            self.text_desc.text += '\n' + tmp + '\n\n'

    def next_page(self):
        # 인덱스가 전체 기록 수 보다 클 경유우, 다음 페이지 없음
        if self.index >= 4:
            return
        else:
            self.index += 1
            self.print_record(list(self.playerRecordData.keys())[self.index])
            self.print_proviso()

    def prev_page(self):
        # 인덱스가 0 보다 작을 경우, 이전 페이지 없음
        if self.index <= 0:
            return
        else:
            self.index -= 1
            self.print_record(list(self.playerRecordData.keys())[self.index])
            self.print_proviso()

    def disable(self):
        self.resume()
        self.guide.disable()
        self.text_desc.disable()
        super().disable()

    def input(self, key):
        if key == 'x':
            self.disable()
        if key == 'z':
            self.prev_page()
        if key == 'c':
            self.next_page()
