from ursina import *
from copy import copy
import threading

from ui.scene.endingscene import EndingScene


class Node:
    __slots__ = ['index', 'indent_level', 'content', 'code', 'children', 'is_answer']

    # 인스턴스 변수를 제한한다. 위의 변수들만 node클래스의 인스턴스변수로 생성할 수 있다.

    def __str__(self):
        return 'Node:\n    ' + '\n    '.join([f'{e} = {getattr(self, e)}' for e in Node.__slots__])
    # node를 출력할 때 나옴. 객체의 toString이라 생각하면됨


class RenConversation(Entity):

    def __init__(self, font=None, variables_object=None, screenlist=None, **kwargs):
        super().__init__(y=-.1)
        self.image = None

        self.question = Button(parent=self, text_origin=(0, .25), scale=(camera.aspect_ratio, .3), model="quad",
                               origin=(0, 0),
                               texture='dialog',
                               color=color.white,
                               position=(0, -.25),
                               text='Question')
        self.question.text_entity.font = "NanumSquareRoundR.ttf"
        self.question.text_entity.line_height = 1.25
        self.question.text_entity.color = color.black
        self.question.text_entity.position = (0, 0)
        self.question.highlight_color = self.question.color
        self.check = False
        self.second_check = False
        self.variables_object = variables_object

        self.video = None

        if self.variables_object.print_npc:  # 객체 없을 떄, 마지막 엔딩 나올ㄹ는 npc 모델 생성안함

            self.npc = Entity(parent=self, model='quad', texture='', position=(0, .1),
                              scale=(camera.aspect_ratio / 3, camera.aspect_ratio / 3), z=3)

        self.more_indicator = Entity(parent=self.question, model=Circle(3), position=(.4, .2, -.1), rotation_z=180,
                                     color=color.azure, world_scale=.0, z=-1, disabled=True)
        # 우측 하단에 뜨는 토글 스위치 껐음 너무 크게나와서. world_scale 0.5 -> 0으로 변경

        self.list = []  # 객체(node)의 text나 content를 저장할 리스트

        def toggle():
            self.more_indicator.visible = not self.more_indicator.visible
            invoke(self.more_indicator.toggle, delay=.5)

        self.more_indicator.toggle = toggle
        self.more_indicator.toggle()
        self.spacing = 2.5 * .04
        self.wordwrap = 65
        self.button_model = Quad(radius=.5, aspect=1 / .075)

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.answer_0 = Button(parent=self, text='answer_0', x=0, y=.4, scale=(1, .075),
                               text_origin=(-.5, 0), model=copy(self.button_model))
        self.answer_1 = Button(parent=self, text='answer_1', x=self.answer_0.x, y=self.answer_0.y - self.spacing,
                               scale=(1, .075),
                               text_origin=(-.5, 0), model=copy(self.button_model))
        self.answer_2 = Button(parent=self, text='answer_2', x=self.answer_0.x, y=self.answer_1.y - self.spacing,
                               scale=(1, .075),
                               text_origin=(-.5, 0), model=copy(self.button_model))
        self.answer_3 = Button(parent=self, text='answer_2', x=self.answer_0.x, y=self.answer_2.y - self.spacing,
                               scale=(1, .075),
                               text_origin=(-.5, 0), model=copy(self.button_model))
        self.answer_4 = Button(parent=self, text='answer_2', x=self.answer_0.x, y=self.answer_3.y - self.spacing,
                               scale=(1, .075),
                               text_origin=(-.5, 0), model=copy(self.button_model))
        # self.answer3, 4 추가, 그러고 self.spacing 속성값을 조절했음. (버튼들간 간격조절)

        self.buttons = (self.answer_0, self.answer_1, self.answer_2, self.answer_3, self.answer_4)
        # 추가된 버튼 2개를 buttons 리스트에 추가 , 나머지 부분은 for문으로 알아서 초기화돼서 건든것 없음. 튜플 형태로 저장

        for b in self.buttons:
            b.text_entity.font = "NanumSquareRoundR.ttf"
            b.text_entity.line_height = 1.15
            b.text_entity.position = (-.45, 0)

        self.question_appear_sequence = None
        self.button_appear_sequence = None
        self.started = False

    # def createImg(self, value):
    #     Entity(parent = self, scale = .55, y = 0.175, model = 'quad', texture = value)
    #     print('hh')

    def ask(self, node, question_part=0):  # 여기서 node값은 conversation_nodes[0] 부터 시작한다.

        # print(node)
        self.current_node = node
        self.question_part = question_part
        self.question.text = node.content[question_part]
        self.question.text_entity.wordwrap = self.wordwrap
        self.more_indicator.enabled = False
        self.question_appear_sequence = self.question.text_entity.appear(delay=.1)

        if node.code:

            if '#' in node.code:
                self.variables_object.record_titles.add(node.code.strip('#'))
                print(self.variables_object.record_titles)
            elif '$' in node.code:
                node_tmp = node.code.replace("$", "")  ## 구분자를 제ㅓ거한 파일명을 저장한 임시변수
                Audio("_resources/sound/voice/police/" + node_tmp, loop=False)
                node.code = ""
            elif '@' in node.code:
                Draggable(parent=self, scale=0.8, origin=(5, 6), color=color.white,
                          y=.1, model='quad', texture=node.code[1:])
            else:
                self.npc.texture = node.code

        for b in self.buttons:
            b.enabled = False

        answers = []
        for i, child in enumerate(node.children):  # i는 index, child는 node의 정보가 담긴 node객체를 뜻한다.

            if self.variables_object and child.code and child.code.startswith('if'):
                try:
                    if not getattr(self.variables_object, child.code[3:]):
                        continue
                except Exception as e:
                    print('failed parsing conversation if statement:', e)

            answers.append(child)

        # multi page question
        if len(node.content) > 1 and self.question_part < len(node.content) - 1:
            if self.question_part < len(node.content):  # question not finished, so don't show answer buttons
                # print('question not finished')
                self.question_appear_sequence.append(Func(setattr, self.more_indicator, 'enabled', True))
                return

        self.button_appear_sequence = Sequence()
        invoke(self.button_appear_sequence.start, delay=self.question_appear_sequence.duration)

        def close_screen():

            self.disable()
            self.variables_object.screenlist[0].disable()
            self.variables_object.screenlist[1].disable()
            self.variables_object.screenlist[2].enable()

        def stop_ending():
            print("ending실행")
            time.sleep(54)
            self.video.disable()
            print("비디오정지")
            self.variables_object.first = False
            self.variables_object.second = False
            close_screen()

        def check_on_click(self):
            self.disable()
            self.variables_object.print_npc = True
            if self.variables_object.first and self.variables_object.second:
                self.video = Entity(parent=camera.ui, model='quad', scale=(camera.aspect_ratio, 1), z=-3,
                                    texture='ending.mp4')
                thread = threading.Thread(target=stop_ending)
                thread.start()
                print("비디오실행")
                self.disable()

                return

            elif self.variables_object.first and self.variables_object.fail:  # 잘못된 용의자를 골랐을 때
                self.variables_object.fail = False
                close_screen()

            elif self.variables_object.first:
                print("실행")
                EndingScene(self.variables_object)

        if not node.children:
            self.buttons[0].text = '확인'

            self.button_appear_sequence.append(Func(setattr, self.buttons[0], 'enabled', True))

            self.buttons[0].on_click = Func(check_on_click, self)
            # self.buttons[0].text = '확인'
            #
            # self.button_appear_sequence.append(Func(setattr, self.buttons[0], 'enabled', True))
            # # self.buttons[0].on_click = Func(setattr, self, 'enabled', False)
            # self.buttons[0].on_click = Func(check_on_click)

        for i, child in enumerate(answers):

            self.button_appear_sequence.append(Wait(i * .15))
            self.button_appear_sequence.append(Func(setattr, self.buttons[i], 'enabled', True))
            self.buttons[i].text = child.content[0]
            self.buttons[i].text_entity.wordwrap = self.wordwrap

            def on_click(node=child):

                select = node.content[0]  # 마지막 버튼의 content를 저장한다., index로 해도된다. 이 함수는 for문 안에 있음.
                self.list.append(select)  # 선택한 녀석들의 content나 text를 리스트에 저장해놓고 대화가 종료될 때 return

                if not node.children:
                    print('end conversation')
                    self.enabled = False
                    return select

                if node.code and not node.code.startswith('if '):
                    try:
                        if '+=' in node.code or '-=' in node.code or '*=' in node.code or '/=' in node.code or '==' in node.code:
                            var, operator, value = node.code.split()

                            # original_value = getattr(self.variables_object, var)
                            # data_type = type(original_value)
                            # value = data_type(value)
                            # if operator == '+=':    new_value = original_value + value
                            # if operator == '-=':    new_value = original_value - value
                            # if operator == '*=':    new_value = original_value * value
                            # if operator == '==':    self.createImg(value)

                        #     setattr(self.variables_object, var, new_value)
                        #
                        # print('executed code:', node.code)
                        # print(self.variables_object.sample_data)
                    except Exception as e:
                        print('failed executing code on node:', node, 'code:', node.code, 'error:', e)

                invoke(self.ask, node.children[0], 0, delay=.1)
                if len(node.children) > 1:
                    print('error at node:', node, '. node has multiple children, but should only have one (a question)')

            self.buttons[i].on_click = on_click  # 첫번째 on_click은 ㅇ아마도 진짜 버튼의 이벤트핸들러에 의한 메서드고 뒤쪽 on_click은
            # 여기 클래스에서 오버라이딩한 on_click인듯.
            # button이 클릭되면 이 함수의 on_click메서드를 실행하겠다는 것.

    def input(self, key):
        if key == 'left mouse down' or key == 'space' and not mouse.hovered_entity in self.buttons:
            self.next()

    def next(self):
        if not self.started:
            return

        if not self.question_appear_sequence.finished and self.question_appear_sequence.t > .1:
            self.question_appear_sequence.finish()
            if self.button_appear_sequence:
                self.button_appear_sequence.start()
            return

        if self.question_part < len(self.current_node.content) - 1:
            self.ask(self.current_node, self.question_part + 1)

    def start_conversation(self, conversation):
        self.conversation_nodes = self.parse_conversation(conversation)
        self.ask(self.conversation_nodes[0])
        # print(conversation)
        # print(self.conversation_nodes[2])
        # print(self.conversation_nodes[1].content)
        # conversation_nodes는 node list로 입력받은 conversation str을 node클래스의 content에 특정 문자를 기준으로(enter, *등)잘라져서 content에 보관된다.
        self.started = True

    def parse_conversation(self, convo):
        convo = convo.strip()
        nodes = list()
        prev_node = None
        node_index = 0

        for i, l in enumerate(convo.split('\n')):

            if not l:
                continue

            indent_level = len(l) - len(l.lstrip())

            indent_level //= 4

            content, code = l.strip(), None
            if '(' in l:
                content, code = l.split('(')
                content = content.strip()
                code = code[:-1]

                is_answer = content.startswith('* ')
                # print('code:', codeK)

            if prev_node and prev_node.indent_level == indent_level:
                prev_node.content.append(content)
                prev_node = n
                continue

            n = Node()
            n.index = node_index
            n.indent_level = indent_level
            n.is_answer = content.startswith('* ')
            if n.is_answer:
                content = content[2:]

            n.content = [content, ]
            n.children = list()
            n.code = code
            nodes.append(n)
            prev_node = n
            node_index += 1

            # look backwards through nodes to find current node's parent
            for j in range(node_index - 1, -1, -1):

                if nodes[j].indent_level == n.indent_level - 1:
                    nodes[j].children.append(n)
                    break

        return nodes
