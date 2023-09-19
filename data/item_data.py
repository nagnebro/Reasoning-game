

class ItemData:
    def __init__(self, name, desc, chapter_no, texture):
        self.name = name
        self.desc = desc
        self.chapter_no = chapter_no
        self.texture = texture


class GameItemData:
    def __init__(self):
        self.item = {

            # 1. 학생회장의 단서.
            "떨어진 영수증": ItemData("떨어진 영수증", "샌드위치를 구매한 영수증이다.", 1, 'receipt'),
            "내려치기 딱 좋은 망치": ItemData("망치.", "내려치기에 좋은 망치다.", 1, 'hammer'),
            "화학약품": ItemData("화학약품", "쓰다만 화학약품 병이다. 굉장히 위험해 보인다.", 1, 'poison'),
            "휴대폰": ItemData("휴대폰", "학생회장의 휴대폰이다.", 1, 'galaxy_phone'),
            # "영수증": ItemData("영수증", "편의점 구매내역이 적혀있는 영수증이다.", 1, 'receipt'),
            # "휴대폰": ItemData("테스트 아이템2", "테스트 하려고 은만든 아이템이다2", 1, 'glass'),


            # 2. 졸업생의 단서
            "배터리": ItemData("배터리", "흔한 보조배터리이다.", 2, 'battery'),
            "책": ItemData("책", "살인마에 관한 내용을 담은 수기이다.", 2, 'book'),
            "벽돌": ItemData("벽돌", "내려치기 좋은 망치이다.", 2, 'brick1'),
            "롤 경기장 티켓": ItemData("롤 경기장 티켓", "롤 경기장 입장에 쓰이는 티켓이다.", 2, 'lol_ticket'),
            "ph 종이": ItemData("ph 종이", "과학실험에 쓰이는 ph종이다.", 2, 'ph_paper'),



            # 3. 동아리 선배의 단서
            "커터칼": ItemData("커터칼", "날카로운 커터칼이다.", 3, 'cutter_knife'),
            "쪽지": ItemData("쪽지", "누군가를 향한 집착이 담긴 쪽지이다.", 3, 'paper1'),
            "밧줄": ItemData("밧줄", "무엇인가 묶을 때 쓰는 밧줄이다.", 3, 'rope'),
            "후드티": ItemData("후드티", "동아리 선배가 입는 후드티다.", 3, 'hood'),
            # "마스터 키": ItemData("마스터 키", "마스커 키다.", 3, 'master_key'),



            # 4. 남교수님의 단서
            "비상용 망치": ItemData("비상용 망치", "유사시에 사용할 수 있는 작은 망치다.", 4, 'emergency_hammer'),
            "조교 리스트": ItemData("조교 리스트", "누군가에게 집착이 담긴 쪽지이다..", 4, 'student_list'),
            "블랙박스": ItemData("블랙박스", "차량용 블랙박스이다.", 4, 'black_box'),
            # "마스터 키": ItemData("마스터 키", "마스터 키다.", 3, 'master_key'),


            # 5. 전여친의 단서
            "커플사진": ItemData("커플사진", "인하군과 다른 여자가 함께 찍힌 사진이다.", 5, 'couple_paper'),
            "일기": ItemData("일기", "누군가가 작성한 일기이다.", 5, 'diary'),
            "아이폰": ItemData("아이폰", "팀쿡이 만든 훌륭한 아이폰이다.", 5, 'iphone'),
            "숫돌": ItemData("숫돌", "칼을 갈 때 쓰는 숫돌이다.", 5, 'stone'),




        }

