class PlayerData:
    def __init__(self, name, chapter=1):
        self.name = name
        self.position = (32.5, -8)
        self.inventory = []
        self.record_titles = set()
        self.chapter = chapter
        self.sample_data = 0
        self.first = False  # 마지막 팩스로 제출했는지 확인하기 위함
        self.second = False
        # renconversation 중 뒤에 npc를 생성하지 않아도 되는 경우의 조건값을 위한 변수,  사용할떄만 True로 바꿔주고
        # 대화 끝날시 False로 변경
        self.print_npc = True

        self.fail = False  # 실패 조건
        self.crimer = None  # 팩스 제출에 사용한 용의자 번호
        self.screenlist = []  # 게임 시작시 띄운 화면 목록을 저장할 데이터
