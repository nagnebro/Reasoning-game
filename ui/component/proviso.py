from ursina import *

double_check = True


class Proviso(Button):
    player_data = None  # 클래스 변수를 이용해 모든 Button이 공통된 player_data를 공유한다

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.double_check = True  # 단서를 클릭 시 처음 한번만 창이 뜨게끔 한다.

        self.check = True

        self.screen = None

    def close_screen(self):  # 창을 닫으면서 단서를 추가한다.
        # 전역변수를 함수내에서 사용할 때 global 제어자?를 붙여주지 않으면 컴파일 에러가 발생한다.
        # 밖의 전역변수를 사용하는 것인지, 함수내에서 선언한 지역변수인지 헷갈려하기 때문이다.수

        # 여기서 중요한 것은 단서를 중복해서 클릭했을 때는 창이 띄워져서는 안된다는 것.

        global double_check
        Proviso.player_data.inventory.append(self)
        # self.player_data.inventory.append(self) # 현재 창을 띄운 proviso의 객체를 저장

        double_check = True
        self.disable()
        self.enabled = False

        self.screen.disable()

        # on_click이 발생했는데 doublc_check가 false라는 것은 창이 꺼졌을떄이므로 double_check를 true로 바꿔 다음번 클릭 떄 창이 열리게끔 한다.

    def on_click(self):  # mybutton으로 만든 객체들이 클릭됐을때 실행되는 메서드. , Button클래스의 on_click 오버라이딩, 이벤트핸들러로 동작한다.
        # list가 None이면 for문 돌릴때 에러발생할 거다. 근데 어차피 list는 우리가 추가해줄 거기 때문에 괜찮음.

        global double_check
        # 전역변수를 함수내에서 사용할 때 global 제어자?를 붙여주지 않으면 컴파일 에러가 발생한다.
        # 밖의 전역변수를 사용하는 것인지, 함수내에서 선언한 지역변수인지 헷갈려하기 때문이다.
        # 기본적으로는 이름이 같은 전역변수와 지역변수가 있을 떄 당연하게도 지역변수의 우선순위가 더 높다.
        # 유효범위가 좁을수록 그 범위안에서는 우선순위가 높다 생각하면 됨.

        # 여기서 중요한 것은 단서를 중복해서 클릭했을 때는 창이 띄워져서는 안된다는 것.

        if double_check:
            double_check = False
            self.screen = Draggable(
                parent=camera.ui,
                model=Quad(radius=.015),
                texture='white_cube',

                scale=(1.2, .9),
                z=-1, world_y=0,  # 화면을 정면으로 바라봤을 떄 우리가 일반적으로 생각하는 수학의 좌표평면이 있다. 그리고 현재 내가 바라보는 위치에서 원점으로 갈수록
                # z축의 값은 +가 되고 나와 가까워질수록 -값이 된다. 즉 z의 속성값을 +로 설정할 시 객체들(texture)들 밑에 묻히기 때문에
                # 보이지 않게 되는 것이다. 따라서 -로 설정하면 거의 절대적으로 보인다고 할 수 있겠다. (z-index)

                color=color.color(0, 0, .1, .9),

                disabled=True,
                # Draggable클래스 역시 button클래스를 상속받으므로 이 기능을 추가하지 않으면 창이 클릭이 되는 이상한 상황이 발생하므로 True로 버튼의 기능을 disable시켜준다.
                # draggin -> drag 가능 유무를 결정하는 속성값

            )  # Entity 객체에서는 text 속성이없음. button속성에 있기 때문에 draggable 클래스나 button클래스에서만 지정해야 text가 보인다.
            # 결론적으로 단서들을 button이나 draggable 타입으로 만들어야 할 이유가 명확한 것.

            # print(self.desc)
            # self.screen.text_entity.font = "NanumSquareRoundR.ttf"

            btn = Button(  # 여기서도 MyButton으로 생성할 시 그 버튼을 클릭할떄도 위에 draggable 객체가 생성됨.
                # 따라서 button 타입으로 객체 생성, 위의 방법으로 할거면 on_click 함수의 if조건으로 단서수집 객체들을 클래스에 집어넣던지 해서
                # Mybutton 이면서 단서인것만 클릭했을때 이벤트가 발생하게 해야한다.

                parent=camera.ui,
                model='quad',
                scale=(.15, .1),
                radius=1,
                z=-1,
                text='확인',
                color=color.gray,

            )

            img = Entity(
                parent=camera.ui,
                model='quad',
                scale=(.7, .7),
                z=-1,
                texture=self.texture,
                color=color.white,

            )
            text = Text(text=self.desc, origin=(0, 0))
            text.font = "NanumSquareRoundR.ttf"

            btn.text_entity.font = "NanumSquareRoundR.ttf"
            # text.text_entity.font = "NanumSquareRoundR.ttf"
            btn.parent = self.screen  # entity요소끼리 서로 부모 자식 관계를 맺어주면 객체끼리 상대적인 포지션을 가지고 붙어다닐 수 있다.
            img.parent = self.screen  # img 요소도 스크린과 묶어놓는다.
            text.parent = self.screen  # 텍스트 박스 생성.
            img.position = (0, 0.15, -1)
            btn.position = (0, -.35, -1)
            text.position = (0, -.2, -1)
            btn.on_click = self.close_screen

            #  Mybutton 클래스는 화면에서
            # 예외처리는 다음과 같이 한다.단서들로만 정해져있기 때문에 단서들이라는 특정성과 단 1개만 실행됐을 때 더이상 실행되지 않게끔 해야함

## 나중에 MyButton 클래스 만들지말고 기존의 on_click 오버라이딩하고 단서에 해당하는 버튼객체들과 창에 해당하는 버튼, 창을 닫는 버튼 객체들끼리의 공통점을 묶어줄수 있는
# 클래스나, 인터페이스 따위로 연결지으면 어떻게 될 거 같긴함. on_click메서드 하나에서 실행되는 조건을 다 다르게 주면 하나로 처리 가능.하지않을까


# class MyButtonChild(MyButton):
