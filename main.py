from ursina import *

from ui.scene.mainmenu import MainMenu
from game import Game

app = Ursina()
# 상단 바 설정
window.borderless = False
# 해상도 고정
window.size = (1280, 720)
# fadeout 을 위한 기본 창 색깔 설정
window.color = color.black

# 타이틀 화면
menu = MainMenu

camera = EditorCamera()
camera.target_fov = 15

# 게임 초기화
game = Game('김이조', menu)

# 게임 시작
app.run()

