from ursina import *

from data.record_data import GameRecordData
from ui.scene.renscene import RenScene


class FaxPaper(Entity):
    def __init__(self, player_data, resume=None):
        super().__init__(parent=camera.ui, model='quad', texture='note_stu_pr',
                         scale=(1, 1.2),
                         color=color.white)
        self.weapon = None
        background = Entity(parent=self, model='quad',
                            scale=(camera.aspect_ratio, 1),
                            color=color.black, z=4, world_y=0)

        self.resume = resume
        self.guide = Text(parent=camera.ui, font="NanumSquareRoundB.ttf",
                          text="'Z' 이전 페이지      'X' 닫기      'C' 다음 페이지      'V' 전송",
                          position=(-.2, -.425, -1))

        self.index = 0
        self.text_desc = Text(parent=camera.ui, font="NanumSquareRoundR.ttf", scale=.8, text='',
                              color=color.black, position=(.08, 0, -1))

        self.items = []
        self.item_object = None
        self.inventoryData = player_data.inventory

        self.recordData = GameRecordData()
        self.playerRecordData = {'stu_pr': [], 'gradu': [], 'club_leader': [], 'prof_nam': [], 'ex_gf': []}


        self.player_data = player_data

        for record_title in player_data.record_titles:
            record = self.recordData.record[record_title]
            self.playerRecordData[record.npc_name].append(record)
        if len(self.playerRecordData) != 0:
            self.print_record('stu_pr')
            self.print_proviso()

    def append(self, item):
        if self.weapon is not None:
            self.weapon.disable()
        self.weapon = Entity(parent=self, model='quad', texture=item.texture, name=item, color=color.white,
                             scale=(.2, .2), z=-1, x=-.2, y=-.1)

    def set_draggable(self, item, count):
        icon = Draggable(parent=self.item_object, model='quad', texture=item.texture, name=item,
                         color=color.white,
                         scale=(.12, .12), z=-1, x=-.2 + count * 0.1, y=-.25)
        icon.org_pos = (icon.x, icon.y)

        def drop():
            print(icon.x, icon.y)
            # if outside, return to original position
            if icon.x < -.25 or icon.x >= .25 or icon.y > -.16:
                self.append(icon)
                icon.position = icon.org_pos

        icon.drop = drop

    def print_proviso(self):
        if self.item_object is not None:
            self.item_object.disable()
        self.item_object = Entity(parent=self, model='quad', scale=(1, 1), color=color.clear)
        count = 0
        for item in self.inventoryData:
            if item.proviso == self.index + 1:
                count += 1
                self.set_draggable(item, count)
                self.items.append(item)

    def print_record(self, npc_name):
        self.texture = 'fax_' + npc_name
        self.text_desc.text = ''
        for data in self.playerRecordData[npc_name]:
            self.text_desc.text += data.title + '\n\n'

    def next_page(self):
        # 인덱스가 전체 기록 수 보다 클 경우, 다음 페이지 없음
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

    def send_fax(self):
        if self.weapon is None  or len(self.items) < 3 :  # 팩스 제출 거부
            print("gh")
            print(self.index)



            self.player_data.print_npc = False
            RenScene(
                no_background=True,
                background='ending_background',
                script='not_enough.txt',
                font="NanumSquareRoundR.ttf",
                variables_object=self.player_data

            )
            self.disable()
        else:

            self.player_data.crimer = self.index # 제출 선택한 용의자 프로파일의 번호를 저장(0번이 범인)
            print(self.player_data.crimer)
            self.disable()
            self.player_data.first = True
            self.player_data.print_npc = False
            RenScene(
                background='ending_background',

                script="ending.txt",
                font="NanumSquareRoundR.ttf",
                variables_object=self.player_data,

            )




    def disable(self):
        self.guide.disable()
        self.text_desc.disable()
        super().disable()

    def input(self, key):
        if key == 'x':
            self.disable()
        elif key == 'z':
            self.prev_page()
        elif key == 'c':
            self.next_page()
        elif key == 'v':
            self.send_fax()


