from game import Game
from menu import MainMenu

g = Game()
while g.running: # 전체 게임의 프로그램 루프.
    g.curr_menu.display_menu() # 시작하자마자 메인 메뉴를 틀어줌.
    g.game_loop() # 메인메뉴에서 start버튼을 눌렀을 때 game loop로 들어감.

    # 폰트 저작권 : self.font_name = r'SSAnt1family\SSAntRegular.ttf  : 상상토끼.
    # 똥 그림 저작권 : Pixel perfect
    # space game의 사진들 저작권 : scratch
    # 똥 캐릭터 그림 저작권 : 어반브러시 (urbanbrush) 