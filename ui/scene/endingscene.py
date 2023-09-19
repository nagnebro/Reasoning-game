class EndingScene:
    def __init__(self, variables_object=None):
        super().__init__()
        self.variables_object = variables_object
        self.script = None

        from ui.scene.renscene import RenScene
        if self.variables_object.crimer == 0:
            self.variables_object.second = True  # 엔딩 비디오 장면 나오게 하는 조건
            self.script = "correct_ending.txt"
        else:
            self.script = "wrong_ending1.txt"
            self.variables_object.fail = True

        self.variables_object.print_npc = False
        RenScene(
            background='black_screen',
            script=self.script,
            font="NanumSquareRoundR.ttf",
            variables_object=self.variables_object
        )
