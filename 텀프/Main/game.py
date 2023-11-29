import pygame
from menu import *
import random

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False # running은 게임이 실행될 때, playing은 플레이가 되고 있을 때 True
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.W_KEY, self.A_KEY, self.S_KEY, self.D_KEY, self.ESC, self.SPACE = False, False, False, False, False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 960, 720
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = r'SSAnt1family\SSAntRegular.ttf' # 폰트 저작권 : 상상토끼.
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        self.bgColor, self.textColor = self.BLACK, self.WHITE

        self.main_menu = MainMenu(self) # MainMenu에 game객체를 넘겨줌 

        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.games = GameMenu(self)
        
        self.space = SpaceGameMenu(self)
        self.spaceMenual_1p = SpaceMenual_1p(self)
        self.spaceMenual_2p = SpaceMenual_2p(self)
        self.brick = BrickBreakingMenu(self)
        self.brickMenual = BrickMenual(self)
        self.poo = EscapePooMenu(self)
        self.pooMenual = PooMenual(self)
        self.mouse = MouseMenu(self)
        self.mouseMenual = MouseMenual(self)

        self.curr_menu = self.main_menu
        self.game_select = 'oh my god'


    def game_loop(self):
        while self.playing: # 게임이 실행되는 동안
            if self.game_select == 'space game 1p': # Game 메뉴에서 선택된게 SpaceGame이라면 SpaceGame을 실행함.
                self.SpaceGame1p()
                self.game_select = 'NULL'
                self.playing = False
                self.curr_menu = self.games
                self.curr_menu.display_menu()
            elif self.game_select == 'space game 2p':
                self.SpaceGame2p() # 구현해야함.
                self.game_select = 'NULL'
                self.playing = False
                self.curr_menu = self.games
                self.curr_menu.display_menu()
            elif self.game_select == 'BrickStart':
                self.BrickBreaking()
                self.game_select = 'NULL'
                self.playing = False
                self.curr_menu = self.games
                self.curr_menu.display_menu()
            elif self.game_select == 'PooStart':
                self.escape_poo()
                self.game_select = 'NULL'
                self.playing = False
                self.curr_menu = self.games
                self.curr_menu.display_menu()
            elif self.game_select == 'MouseStart':
                self.mouseGame()
                self.game_select = 'NULL'
                self.playing = False
                self.curr_menu = self.games
                self.curr_menu.display_menu()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                if self.curr_menu != 'NULL':
                    self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN: # 키가 눌렸다면 바로 처리하지 않고 어떤 키가 눌렸는지 확인을 함. 
                if event.key == pygame.K_RETURN: # enter.
                    self.START_KEY = True # 
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_w:
                    self.W_KEY = True
                if event.key == pygame.K_a:
                    self.A_KEY = True
                if event.key == pygame.K_s:
                    self.S_KEY = True
                if event.key == pygame.K_d:
                    self.D_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC = True
                if event.key == pygame.K_SPACE:
                    self.SPACE = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.W_KEY, self.A_KEY, self.S_KEY, self.D_KEY, self.ESC, self.SPACE = False, False, False, False, False, False, False, False, False, False

    def draw_text(self, text, size, x, y): # text = 텍스트 문자열, size : 크기, (x,y) : 텍스트의 위치.
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.textColor)
        text_rect = text_surface.get_rect() # 텍스트의 x,y, w, h를 알려줌
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

    def SpaceGame1p(self):
        fps = pygame.time.Clock()

        background = self.window
        pygame.display.set_caption("SpaceGame 1p")
        ### 이미지 로드
        # 배경
        img_bg = pygame.image.load(r"image\Moon.png")

        ### 캐릭터 이미지 로드
        # img_character_r = pygame.image.load(r"우주게임\image\character_walk_r_1.svg")
        img_character_r = pygame.image.load(r"image\character_walk_r_1.svg")
        img_character_l = pygame.image.load(r"image\character_walk_l_1.svg")
        # img_character_death = pygame.image.load(r"")
        # 플레이어 캐릭터
        img_character = img_character_r
        # 적 캐릭터
        img_enemy = pygame.image.load(r"image\enemy.svg")

        ### 플레이어 캐릭터
        # 내 체력
        my_hp = "my hp : "
        my_hp_point = 10
        my_hp_font = pygame.font.SysFont(self.font_name, 30)
        # 적 체력
        enemy_hp = "enemy hp : "
        enemy_hp_point = 10
        # 적 폰트, render, blit
        enemy_hp_font = pygame.font.SysFont(self.font_name, 30)

        # GameOver Font
        gameover_font = pygame.font.SysFont(self.font_name, 60)
        youwin_font = pygame.font.SysFont(self.font_name, 60)
        gameover = False

        # 총알
        img_bullet_my = pygame.image.load(r"image\crystal-b.svg")
        img_bullet_enemy = pygame.image.load(r"image\Lightning.svg")

        ## 사이즈 정리
        # 이미지 별 사이즈 정리
        bg_size_x, bg_size_y = img_bg.get_rect().size
        character_size_x, character_size_y = img_character.get_rect().size
        enemy_size_x, enemy_size_y = img_enemy.get_rect().size
        bullet_my_size_x, bullet_my_size_y = img_bullet_my.get_rect().size
        bullet_enemy_size_x, bullet_enemy_size_y = img_bullet_enemy.get_rect().size

        ### 위치 정리
        # 캐릭터 위치
        character_pos_x = bg_size_x/2 - character_size_x/2
        character_pos_y = bg_size_y - character_size_y

        # 적 위치
        enemy_pos_x = bg_size_x/2 - enemy_size_x/2
        enemy_pos_y = 0

        # 내 탄환 위치
        bullet_my_pos_x = character_pos_x + character_size_x/2 - bullet_my_size_x/2
        bullet_my_pos_y = character_pos_y - bullet_my_size_y

        # 적 탄환 위치
        bullet_enemy_pos_x = enemy_pos_x + enemy_size_x/2 - bullet_enemy_size_x/2
        bullet_enemy_pos_y = enemy_size_y

        ### 적의 위치를 랜덤으로 움직이게 하기.
        # 적이 갈 수 있는 위치를 랜덤으로 발생시켜 거기로 가게 하고, 도착하면 다시 랜덤을 발생시켜 움직이게 한다.
        random_pos = random.randrange(0, bg_size_x - enemy_size_x) // 8 * 8 + 1
        enemy_spd = 8

        # 내 이동
        character_spd = 8
        character_to = 0

        # 내 총알
        my_bullet = []
        rect_my_bullet = []
        my_bullet_spd = 8

        # 적 총알
        enemy_bullet = []
        rect_enemy_bullet = []
        enemy_bullet_time = 0
        random_time = random.randrange(50,200)
        enemy_bullet_spd = 8

        # 나와 적의 rect
        rect_character = img_character.get_rect()
        rect_enemy = img_enemy.get_rect()


        def game_text(word, x, y): # x, y위치에 word를 출력함.
            font = pygame.font.Font(None, 100)
            text = font.render(word, True, (0, 255, 255))

            size_width_text, size_height_text = text.get_rect().size
            background.blit(text, (x - size_width_text/2, y - size_height_text/2))


        ## 게임 시작
        first = True
        play = True
        while play:
            fps.tick(60)
            if first:
                for i in range(3, 0, -1):
                    first = False
                    background.fill((0, 0, 0))
                    game_text(str(i), self.DISPLAY_W/2, self.DISPLAY_H/2)
                    pygame.display.update()
                    pygame.time.delay(1000)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        img_character = img_character_r
                        character_to = character_spd
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        img_character = img_character_l
                        character_to = -character_spd
                    if event.key == pygame.K_SPACE:
                        bullet_my_pos_x = character_pos_x + character_size_x/2 - bullet_my_size_x/2
                        bullet_my_pos_y = character_pos_y - bullet_my_size_y
                        my_bullet.append([bullet_my_pos_x, bullet_my_pos_y])
                        rect_my_bullet.append(img_bullet_my.get_rect())
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if(character_to > 0):
                            character_to = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if(character_to < 0):
                            character_to = 0

            # 내 최대최소 거리 구현
            if character_pos_x > bg_size_x-character_size_x:
                character_pos_x = bg_size_x-character_size_x
            elif character_pos_x < 0:
                character_pos_x = 0
            else:
                character_pos_x += character_to
            # 적 움직임 구현
            if enemy_pos_x < random_pos:
                enemy_pos_x += enemy_spd
            elif enemy_pos_x > random_pos:
                enemy_pos_x -= enemy_spd
            else:
                random_pos = random.randrange(0, bg_size_x-enemy_size_x) // 8 * 8 + 1

            # 적 총알 생성
            enemy_bullet_time += 1
            if enemy_bullet_time == random_time:
                random_time = random.randrange(20,40)
                enemy_bullet_time = 0
                enemy_bullet.append([enemy_pos_x + enemy_size_x/2 - bullet_enemy_size_x/2, enemy_size_y])
                rect_enemy_bullet.append(img_bullet_enemy.get_rect())

            background.blit(img_bg, (0,0))
            background.blit(img_character, (character_pos_x, character_pos_y))
            background.blit(img_enemy, (enemy_pos_x, enemy_pos_y))
            # background.blit(img_bullet_enemy, (bullet_enemy_pos_x, bullet_enemy_pos_y))
            # background.blit(img_bullet_my, (bullet_my_pos_x, bullet_my_pos_y))

            # 캐릭터가 이동할 때마다 rect위치를 바꿈.
            rect_character.topleft = (character_pos_x, character_pos_y)
            rect_enemy.topleft = (enemy_pos_x, enemy_pos_y)


            # 내 총알 구현
            if len(my_bullet):
                for itr, bullet in enumerate(my_bullet):
                    bullet[1] -= my_bullet_spd
                    background.blit(img_bullet_my, (bullet[0], bullet[1]))
                    # 내 총알을 하나하나씩 rect값을 넣어주고 충돌 시 처리
                    rect_my_bullet[itr].topleft = (bullet[0], bullet[1])
                    if rect_my_bullet[itr].colliderect(rect_enemy):
                        my_bullet.remove(bullet)
                        rect_my_bullet.remove(rect_my_bullet[itr])
                        enemy_hp_point -= 1

                    if bullet[1] < -bullet_my_size_y:
                        my_bullet.remove(bullet)
            # 적 총알 구현
            if len(enemy_bullet):
                for itr, bullet in enumerate(enemy_bullet):
                    bullet[1] += enemy_bullet_spd
                    background.blit(img_bullet_enemy, (bullet[0], bullet[1]))

                    rect_enemy_bullet[itr].topleft = (bullet[0], bullet[1])
                    if rect_enemy_bullet[itr].colliderect(rect_character):
                        enemy_bullet.remove(bullet)
                        rect_enemy_bullet.remove(rect_enemy_bullet[itr])
                        my_hp_point -= 1

                    if bullet[1] > bg_size_y:
                        enemy_bullet.remove(bullet)

            text_my_hp = my_hp_font.render((my_hp + str(my_hp_point)), True, (255,255,255))
            text_enemy_hp = enemy_hp_font.render(enemy_hp + str(enemy_hp_point), True, (255,255,255))
            text_gameover = gameover_font.render("GAME OVER", True, (255,0,0))
            text_youwin = youwin_font.render("You Win", True, (255,102,0))

            text_my_hp_x, text_my_hp_y = text_my_hp.get_rect().size
            text_enemy_hp_x, text_enemy_hp_y = text_enemy_hp.get_rect().size
            text_gameover_x, text_gameover_y = text_gameover.get_rect().size
            text_youwin_x, text_youwin_y = text_youwin.get_rect().size

            background.blit(text_my_hp, (10, 10))
            background.blit(text_enemy_hp, (bg_size_x - text_my_hp_x - 50, 10))

            if my_hp_point == 0:
                background.blit(text_gameover, (bg_size_x / 2 - text_gameover_x / 2, bg_size_y/2 - text_gameover_y))
                pygame.display.update()
                play = gameover
                pygame.time.delay(3000)
            elif enemy_hp_point == 0:
                background.blit(text_youwin, (bg_size_x / 2 - text_youwin_x / 2, bg_size_y/2 - text_youwin_y))
                pygame.display.update()
                play = gameover
                pygame.time.delay(3000)
            pygame.display.update()

    
    def SpaceGame2p(self):
        pygame.init()
        fps = pygame.time.Clock()

        background = self.window
        pygame.display.set_caption("2p space game")
        ## 이미지 로드
        # 배경
        img_bg = pygame.image.load(r"image\Moon.png")

        # 캐릭터
        # img_character_r = pygame.image.load(r"C:\Users\user\Desktop\텀프\우주게임\image\character_walk_r_1.svg")
        img_1p_r = pygame.image.load(r"image\character_walk_r_1.svg")
        img_1p_l = pygame.image.load(r"image\character_walk_l_1.svg")
        # img_character_death = pygame.image.load(r"")
        img_1p = img_1p_r

        # 내 체력
        _1p_hp = "1P hp : "
        _1p_hp_point = 10
        _1p_hp_font = pygame.font.SysFont('한글폰트.ttf', 30)


        # 적
        img_2p = pygame.image.load(r"image\enemy.svg")

        # 적 체력
        _2p_hp = "2P hp : "
        _2p_hp_point = 10
        # 적 폰트, render, blit
        _2p_hp_font = pygame.font.SysFont('한글폰트.ttf', 30)

        # GameOver Font
        gameover_font = pygame.font.SysFont(None, 60)
        youwin_font = pygame.font.SysFont(None, 60)
        gameover = False

        # 총알
        img_bullet_1p = pygame.image.load(r"image\crystal-b.svg")
        img_bullet_2p = pygame.image.load(r"image\Lightning.svg")

        ## 사이즈 정리
        # 이미지 별 사이즈 정리
        bg_size_x, bg_size_y = img_bg.get_rect().size
        _1p_size_x, _1p_size_y = img_1p.get_rect().size
        _2p_size_x, _2p_size_y = img_2p.get_rect().size
        bullet_1p_size_x, bullet_1p_size_y = img_bullet_1p.get_rect().size
        bullet_2p_size_x, bullet_2p_size_y = img_bullet_2p.get_rect().size

        ## 위치 정리
        # 캐릭터 위치
        _1p_pos_x = bg_size_x/2 - _1p_size_x/2
        _1p_pos_y = bg_size_y - _1p_size_y

        # 적 위치
        _2p_pos_x = bg_size_x/2 - _2p_size_x/2
        _2p_pos_y = 0

        # 내 탄환 위치
        bullet_1p_pos_x = _1p_pos_x + _1p_size_x/2 - bullet_1p_size_x/2
        bullet_1p_pos_y = _1p_pos_y - bullet_1p_size_y
        
        # 적 탄환 위치
        bullet_2p_pos_x = _2p_pos_x + _2p_size_x/2 - bullet_2p_size_x/2
        bullet_2p_pos_y = _2p_size_y

        ## 적의 위치를 랜덤으로 움직이게 하기.
        # 적이 갈 수 있는 위치를 랜덤으로 발생시켜 거기로 가게 하고, 도착하면 다시 랜덤을 발생시켜 움직이게 한다.
        _2p_to = 0
        _2p_spd = 8

        # 내 이동
        _1p_spd = 8
        _1p_to = 0

        # 내 총알
        _1p_bullet = []
        rect_1p_bullet = []
        _1p_bullet_spd = 8

        # 적 총알
        _2p_bullet = []
        rect_2p_bullet = []
        _2p_bullet_spd = 8

        # 1p와 2p의 rect
        rect_1p = img_1p.get_rect()
        rect_2p = img_1p.get_rect()

        def game_text(word, x, y): # x, y위치에 word를 출력함.
            font = pygame.font.Font(None, 100)
            text = font.render(word, True, (0, 255, 255))

            # size_width_text = text.get_rect().size[0]
            # size_height_text = text.get_rect().size[1]

            size_width_text, size_height_text = text.get_rect().size
            background.blit(text, (x - size_width_text/2, y - size_height_text/2))



        ## 게임 시작
        cursor = 0
        play = True
        first = True
        while play:
            fps.tick(60)
            if first:
                first = False
                for i in range(3, 0, -1):
                    background.fill((255, 255, 255))
                    game_text(str(i), bg_size_x / 2, bg_size_y/2)
                    pygame.display.update()
                    pygame.time.delay(1000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        img_1p = img_1p_r
                        _1p_to = _1p_spd
                    if event.key == pygame.K_LEFT:
                        img_1p = img_1p_l
                        _1p_to = -_1p_spd
                    if event.key == pygame.K_d:
                        _2p_to = _2p_spd
                    if event.key == pygame.K_a:
                        _2p_to = -_2p_spd
                    if event.key == pygame.K_SPACE:
                        bullet_2p_pos_x = _2p_pos_x + _2p_size_x/2 - bullet_2p_size_x/2
                        bullet_2p_pos_y = _2p_pos_y + _2p_size_y
                        _2p_bullet.append([bullet_2p_pos_x, bullet_2p_pos_y])
                        rect_2p_bullet.append(img_bullet_2p.get_rect())

                    if event.key == pygame.K_KP_0:
                        bullet_1p_pos_x = _1p_pos_x + _1p_size_x/2 - bullet_1p_size_x/2
                        bullet_1p_pos_y = _1p_pos_y - bullet_1p_size_y
                        _1p_bullet.append([bullet_1p_pos_x, bullet_1p_pos_y])
                        rect_1p_bullet.append(img_bullet_1p.get_rect())
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        if(_1p_to > 0):
                            _1p_to = 0
                    if event.key == pygame.K_LEFT:
                        if(_1p_to < 0):
                            _1p_to = 0
                    if event.key == pygame.K_d:
                        if(_2p_to > 0):
                            _2p_to = 0
                    if event.key == pygame.K_a:
                        if(_2p_to < 0):
                            _2p_to = 0

            # 내 최대최소 거리 구현
            if _1p_pos_x > bg_size_x-_1p_size_x:
                _1p_pos_x = bg_size_x-_1p_size_x
            elif _1p_pos_x < 0:
                _1p_pos_x = 0
            else:
                _1p_pos_x += _1p_to
            # 적 움직임 구현
            if _2p_pos_x > bg_size_x-_2p_size_x:
                _2p_pos_x = bg_size_x-_2p_size_x
            elif _2p_pos_x < 0:
                _2p_pos_x = 0
            else:
                _2p_pos_x += _2p_to

            # 캐릭터가 이동할 때마다 rect위치를 바꿈.
            rect_1p.topleft = (_1p_pos_x, _1p_pos_y)
            rect_2p.topleft = (_2p_pos_x, _2p_pos_y)


            background.blit(img_bg, (0,0))
            # background.fill((0, 0, 0))
            background.blit(img_1p, (_1p_pos_x, _1p_pos_y))
            background.blit(img_2p, (_2p_pos_x, _2p_pos_y))

            # 내 총알 구현
            if len(_1p_bullet):
                for itr, bullet in enumerate(_1p_bullet):
                    bullet[1] -= _1p_bullet_spd
                    background.blit(img_bullet_1p, (bullet[0], bullet[1]))
                    # 내 총알을 하나하나씩 rect값을 넣어주고 충돌 시 처리
                    rect_1p_bullet[itr].topleft = (bullet[0], bullet[1])
                    if rect_1p_bullet[itr].colliderect(rect_2p):
                        _1p_bullet.remove(bullet)
                        rect_1p_bullet.remove(rect_1p_bullet[itr])
                        _2p_hp_point -= 1

                    if bullet[1] < -bullet_1p_size_y:
                        _1p_bullet.remove(bullet)
            # 적 총알 구현
            if len(_2p_bullet):
                for itr, bullet in enumerate(_2p_bullet):
                    bullet[1] += _2p_bullet_spd
                    background.blit(img_bullet_2p, (bullet[0], bullet[1]))

                    rect_2p_bullet[itr].topleft = (bullet[0], bullet[1])
                    if rect_2p_bullet[itr].colliderect(rect_1p):
                        _2p_bullet.remove(bullet)
                        rect_2p_bullet.remove(rect_2p_bullet[itr])
                        _1p_hp_point -= 1

                    if bullet[1] > bg_size_y:
                        _2p_bullet.remove(bullet)
            

            text_my_hp = _1p_hp_font.render((_1p_hp + str(_1p_hp_point)), True, (255,255,255))
            text_enemy_hp = _2p_hp_font.render(_2p_hp + str(_2p_hp_point), True, (255,255,255))
            text_gameover = gameover_font.render("2P WIN", True, (255,0,0))
            text_youwin = youwin_font.render("1P WIN", True, (255,102,0))

            text_my_hp_x, text_my_hp_y = text_my_hp.get_rect().size
            text_enemy_hp_x, text_enemy_hp_y = text_enemy_hp.get_rect().size
            text_gameover_x, text_gameover_y = text_gameover.get_rect().size
            text_youwin_x, text_youwin_y = text_youwin.get_rect().size

            background.blit(text_my_hp, (10, 10))
            background.blit(text_enemy_hp, (bg_size_x - text_my_hp_x - 50, 10))

            if _1p_hp_point == 0:
                background.blit(text_gameover, (bg_size_x / 2 - text_gameover_x / 2, bg_size_y/2 - text_gameover_y))
                pygame.display.update()
                play = gameover
                pygame.time.delay(3000)
            elif _2p_hp_point == 0:
                background.blit(text_youwin, (bg_size_x / 2 - text_youwin_x / 2, bg_size_y/2 - text_youwin_y))
                pygame.display.update()
                play = gameover
                pygame.time.delay(3000)


            pygame.display.update()


    def BrickBreaking(self):
        pygame.init()
        fps = pygame.time.Clock()
        background = self.window
        pygame.display.set_caption("Brick Breaking")

        # 배경 사이즈
        size_width_bg = background.get_size()[0]
        size_height_bg = background.get_size()[1]

        ### 페달 정의
        # 페달의 사이즈
        size_width_pedal = 150
        size_height_pedal = 20
        # 페달의 좌표
        # 사각형의 기준점은 좌측 상단.
        x_pos_pedal = size_width_bg // 2 - size_width_pedal // 2
        y_pos_pedal = size_height_bg - size_height_pedal
        # 페달의 Rect
        rect_pedal = pygame.Rect(x_pos_pedal, y_pos_pedal, size_width_pedal, size_height_pedal)
        # 페달의 이동방향
        to_x_pedal = 0


        ### 공 정의
        # 공의 사이즈, 좌표, Rect
        size_radius_ball = 20
        # 공의 좌표
        # 공은 기준점이 원의 중심임.
        x_pos_ball = size_width_bg // 2
        y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball
        # 공의 Rect
        # 공의 rect는 중심을 기준으로 지름으로 둘러싼 정사각형이기 때문에 rect_ball.center로 공의 중심을 추가로 지정해줌.
        rect_ball = pygame.Rect(x_pos_ball, y_pos_ball, size_radius_ball*2, size_radius_ball*2)
        rect_ball.center = (x_pos_ball, y_pos_ball)
        # 공의 방향과 속도
        x_speed_ball = 10
        y_speed_ball = 10


        ### 블록 정의
        # 블록 사이즈, 좌표, Rect
        size_width_block = size_width_bg // 10
        size_height_block = 50
        # 블록 좌표(시작좌표)
        x_pos_block = 0
        y_pos_block = 0
        # 블록의 Rect들을 담을 리스트
        rect_block = [[] for _ in range (10)] # 리스트 안에 비어있는 리스트가 10개 생김.
        color_block = [[] for _ in range (10)] # 그 내부 리스트 안에 rect를 5개씩 넣음.
        # 각 행에 해당하는 Rect들을 이중리스트로 담음.
        for i in range(10):
            for j in range(5):
                rect_block[i].append(pygame.Rect(i*size_width_block, j*size_height_block, size_width_block, size_height_block))
                color_block[i].append((random.randrange(255), random.randrange(150, 255), random.randrange(150, 255)))
        # G B를 낮게하면 눈이 아파서

        ### 마우스 정의
        # 마우스 좌표
        x_pos_mouse, y_pos_mouse = 0,0


        ### 끝내는 조건 - 점수(없앤 패달의 개수)
        point = 0

        ## 시작 변수
        start = True

        ## 글자를 화면 중앙에 출력하는 함수 구현

        def game_text(word, x, y): # x, y위치에 word를 출력함.
            font = pygame.font.Font(self.font_name, 100)
            text = font.render(word, True, (0, 255, 255))

            # size_width_text = text.get_rect().size[0]
            # size_height_text = text.get_rect().size[1]

            size_width_text, size_height_text = text.get_rect().size
            background.blit(text, (x - size_width_text/2, y - size_height_text/2))


        play = True
        while play:
            # 첫 루프인 것을 확인하기 위해서 start를 이용
            fps.tick(60)
            if start:
                start = False
                for i in range(3, 0, -1):
                    background.fill((255, 255, 255))
                    game_text(str(i), size_width_bg/2, size_height_bg/2)
                    pygame.display.update()
                    pygame.time.delay(1000)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False

                ## 마우스 이동 추적. (마우스의 위치가 페달의 위치임.)
                if event.type == pygame.MOUSEMOTION:
                    # 마우스 위치를 받아옴.
                    x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos() 
                    # 마우스의 x위치 - pedal_x//2 >= 0으로 패달이 화면 좌측 이후로 넘어가지 않게 함. && 마우스의 x좌표 + 페달_x//2 <= 전체화면 크기로 우측을 넘어가지 않게 함.
                    if x_pos_mouse - size_width_pedal // 2 >= 0 and x_pos_mouse + size_width_pedal//2 <= size_width_bg:
                        # 마우스의 위치에 페달의 정중앙이 오게함.
                        x_pos_pedal = x_pos_mouse - size_width_pedal//2         
                        rect_pedal.left = x_pos_mouse - size_width_pedal//2

            # 배경은 기본 색상으로
            background.fill((0, 0, 0))

            # 페달 그리기
            pygame.draw.rect(background, (255, 255, 0) ,rect_pedal)


            ## 공의 좌표를 계산.
            # 공이 좌우측 벽에 닿는다면 공들의 x좌표속도를 반대로 해줌.
            if x_pos_ball - size_radius_ball <= 0:
                x_speed_ball = - x_speed_ball
            elif x_pos_ball >= size_width_bg-size_radius_ball:
                x_speed_ball = -x_speed_ball
            # 공이 위아레 벽에 닿는다면 공들의 y좌표 속도를 반대로 해줌.
            if y_pos_ball - size_radius_ball <= 0:
                y_speed_ball = -y_speed_ball
            elif y_pos_ball >= size_height_bg - size_radius_ball: # 게임 오버 조건.
                background.fill((0, 0, 0))
                game_text("GAME OVER", size_width_bg/2 , size_height_bg/2)
                pygame.display.update()
                pygame.time.delay(1000)
                return # 끝내버리기 게임을. 


            # 공의 움직임 표현.
            x_pos_ball += x_speed_ball
            y_pos_ball += y_speed_ball 


            # 공 그리기
            rect_ball.center = (x_pos_ball, y_pos_ball) # 매 순간 공의 중심을 추적해서 계속 업데이트 해야함.
            pygame.draw.circle(background, (255, 255, 0), (x_pos_ball, y_pos_ball), size_radius_ball)

            
            ### 공과 페달이 충돌했을 때
            if rect_ball.colliderect(rect_pedal):
                y_speed_ball = -y_speed_ball # y축 방향을 반대로 바꿔줌.


            # 블록 그리기 (for문으로 10 x 5 개를 쌓아 만듦.)
            for i in range(10):
                for j in range(5):
                    if rect_block[i][j]:
                        pygame.draw.rect(background, color_block[i][j], rect_block[i][j])
                        rect_block[i][j].topleft = (i*size_width_block, j*size_height_block)

                    if rect_block[i][j] is not None and rect_ball.colliderect(rect_block[i][j]):
                        # 블록의 상하좌우 경계
                        block_top = rect_block[i][j].top
                        block_bottom = rect_block[i][j].bottom
                        block_left = rect_block[i][j].left
                        block_right = rect_block[i][j].right

                        # 볼의 상하좌우 경계
                        ball_top = rect_ball.top
                        ball_bottom = rect_ball.bottom
                        ball_left = rect_ball.left
                        ball_right = rect_ball.right

                        # 충돌 여부 확인 및 처리
                        if ball_bottom > block_top:
                            # 볼이 블록의 위 또는 아래에 있는 경우
                            y_speed_ball = abs(y_speed_ball)
                        elif ball_top < block_bottom:
                            y_speed_ball = -y_speed_ball
                        if ball_right < block_left:
                            # 볼이 블록의 좌우에 있는 경우
                            x_speed_ball = -x_speed_ball
                        elif ball_left > block_right:
                            x_speed_ball = - x_speed_ball

                        rect_block[i][j] = None
                        point += 1

                            
            ## 게임 클리어 조건
            if point == 50:
                background.fill((0, 0, 0))
                game_text("GAME CLEAR", size_width_bg/2, size_height_bg/2)
                pygame.display.update()
                pygame.time.delay(1000)
                play = False

            pygame.display.update()


    def escape_poo(self):
        pygame.init()
        fps = pygame.time.Clock()
        background = self.window
        pygame.display.set_caption("똥 피하기 게임")

        ## 글자를 화면 중앙에 출력하는 함수 구현
        def game_text(word, x, y, size): # x, y위치에 word를 출력함.
            font = pygame.font.Font(self.font_name, size)
            text = font.render(word, True, (0, 255, 255))

            size_width_text, size_height_text = text.get_rect().size
            background.blit(text, (x - size_width_text/2, y - size_height_text/2))

        img_character_rlist = [pygame.image.load(rf'image\poo_character_r_{i}.png') for i in range(1, 4, 1)]
        img_character_llist = [pygame.image.load(rf'image\poo_character_l_{i}.png') for i in range(1, 4, 1)]
        
        # 시작 그림.
        img_character_r = img_character_rlist[0]
        img_character_l = img_character_llist[0]
        img_character = img_character_r
        # 플레이어 체력
        my_hp = 3
        # 플레이어 사이즈, Rect정리
        character_rect = img_character.get_rect()
        character_rect.left 
        character_size_x, character_size_y = character_rect.size
        # 플레이어 이동속도
        character_spd = 12
        character_to = 0
        # 플레이어 위치(시작위치)
        character_pos_x = self.DISPLAY_W/2 - character_size_x/2
        character_pos_y = self.DISPLAY_H - character_size_y

        ### 휴지 구현
        img_tissue = pygame.image.load(rf'image\휴지.png')
        tissues = []
        rect_tissue = []
        tissue_rect = img_tissue.get_rect()
        tissue_size_x, tissue__size_y = tissue_rect.size
        tissue_spd = 8
        tissue_time = 10
        tissue_rand_time = random.randrange(300, 600)

        ### 똥 구현.
        img_poo = pygame.image.load(r'image\poo_img.png') # 
        # 똥들은 계속 화면에 머물러야하기 때문에 리스트의 형태로 구현.
        poos = [] 
        rect_poos = [] # rect들도 계속 리스트로 유지해야함. 플레이어와의 충돌을 알기 위해서.
        poo_time = 0 # 시간을 이용해서 발사 속도를 관리함.
        rand_time = random.randrange(3, 5) # 랜덤으로 50ms ~ 200ms사이로 발사.
        poo_spd = 12
        # 똥의 Rect, size
        poo_rect = img_poo.get_rect()
        poo_size_x, poo_size_y = poo_rect.size

        ### 게임 타이머 설정.
        start_time = 0
        second = 0
        clock = pygame.time.Clock()

        ## 게임 시작
        play = True
        start = True
        while play:
            fps.tick(60)
            if start:
                start = False
                for i in range(3, 0, -1):
                    background.fill((0, 0, 0))
                    game_text(str(i), self.DISPLAY_W/2, self.DISPLAY_H/2, 100)
                    pygame.display.update()
                    pygame.time.delay(1000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                    # 강제종료 조건
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        img_character = img_character_r
                        character_to = character_spd
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        img_character = img_character_l
                        character_to = -character_spd
                    # 키 입력 수행
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if(character_to > 0):
                            character_to = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if(character_to < 0):  
                            character_to = 0
                    # 다른 키를 눌렀을 때 수행. 키 떼면 멈춰야함.

            ## 내가 움직일 수 있는 최대 / 최소 거리 구현
            if character_pos_x < 0:
                character_pos_x = 0
            elif character_pos_x > 960 - character_size_x:
                character_pos_x = 960 - character_size_x
            else:
                character_pos_x += character_to

            ### 하늘에서 떨어지는 응가를 랜덤 위치에 생성하게 함.
            poo_time += 1
            if poo_time == rand_time:
                rand_time = random.randrange(4, 8)
                poo_time = 0
                poos.append([random.randrange(0, self.DISPLAY_W-poo_size_x), 0])
                rect_poos.append(poo_rect)

            tissue_time += 1
            if tissue_time == tissue_rand_time:
                tissue_rand_time = random.randrange(300, 600)
                tissue_time = 0
                tissues.append([random.randrange(0, self.DISPLAY_W - tissue_size_x), 0])
                rect_tissue.append(tissue_rect)

            background.fill((0, 0, 0))
            background.blit(img_character, (character_pos_x, character_pos_y))

            character_rect.topleft = (character_pos_x, character_pos_y)

            already = True # 똥이 바닥에 떨어지는 동시에 캐릭터에 닿으면 없는 똥을 지우려는 문제가 생긴다.
            # 그렇기 때문에 이미 없어졌는 확인할 boolean 변수 생성.

            ### 떨어지는 응가 구현.
            # 떨어지는 똥이 리스트 안에 들어있다면
            if len(poos):
                for itr, poo in enumerate(poos): # poo는 x,y좌표를 가짐.
                    poo[1] += poo_spd # y축 좌표를 계속 증가시킴.
                    background.blit(img_poo, (poo[0], poo[1]))
                    rect_poos[itr].topleft = (poo[0], poo[1]) # 그 똥의 현제 Rect를 최신화.
                    already = True
                    if rect_poos[itr].colliderect(character_rect.inflate(-60, 0)): # 판정범위 축소.
                        poos.remove(poo)
                        already = False # 밑의 if문을 통과하지 못하게 함.
                        rect_poos.remove(rect_poos[itr])
                        my_hp -= 1
                        if my_hp == 0:
                            play = False
                            # 게임 종료 후 띄울 메시지.
                            game_text(f'GAME OVER', self.DISPLAY_W/2, self.DISPLAY_H/2 - 30, 100)
                            game_text(f'Your Point : {second:.1f}s', self.DISPLAY_W/2, self.DISPLAY_H/2 + 80, 100)
                            pygame.display.update()
                            pygame.time.delay(3000)
                            return
                        # 이미지를 조금씩 갈색으로 묻힐거임. 추가.
                        img_character_r = img_character_rlist[3-my_hp]
                        img_character_l = img_character_llist[3-my_hp]
                    if already and poo[1]+poo_size_y > self.DISPLAY_H: # 화면 밑으로 내려가면 없애버림.
                        poos.remove(poo) # 이 응가를 지움.
            if len(tissues):
                for itr, tissue in enumerate(tissues):
                    tissue[1] += tissue_spd
                    background.blit(img_tissue, (tissue[0], tissue[1]))
                    rect_tissue[itr].topleft

            ### 떨어지는 휴지
            # 떨어지는 휴지가 리스트 안에 들어있다면
            if len(tissues):
                for itr, tissue in enumerate(tissues): # poo는 x,y좌표를 가짐.
                    tissue[1] += tissue_spd # y축 좌표를 계속 증가시킴.
                    background.blit(img_tissue, (tissue[0], tissue[1]))
                    rect_tissue[itr].topleft = (tissue[0], tissue[1]) # 그 똥의 현제 Rect를 최신화.
                    if rect_tissue[itr].colliderect(character_rect): # 판정범위 축소.
                        tissues.remove(tissue)
                        rect_tissue.remove(rect_tissue[itr])
                        if my_hp == 3:
                            continue
                        else :
                            my_hp += 1
                            img_character_r = img_character_rlist[3-my_hp]
                            img_character_l = img_character_llist[3-my_hp]
                        
                    if tissue[1] + tissue__size_y > self.DISPLAY_H: # 화면 밑으로 내려가면 없애버림.
                        tissues.remove(tissue) # 이 응가를 지움.

            # 게임 종료 조건.

                
            ### 타이머와 체력 표시.
            # 타이머 설정
            time_since_enter = pygame.time.get_ticks() - start_time
            if time_since_enter > 100:
                start_time = pygame.time.get_ticks()
                second += 0.1
            # 타이머와 체력 폰트 및 
            game_text(f'Your HP : {my_hp}', self.DISPLAY_W - 80, 20, 30)
            game_text(f'Timer : {second:.1f}', 67, 20, 30)

            pygame.display.update()

    def mouseGame(self):

        pygame.init()
        fps = pygame.time.Clock()
        background = self.window
        pygame.display.set_caption("마우스 충돌 게임")
        # 960 * 720
        # 도형들의 rect 리스트
        shapes = [pygame.Rect(0, 620, 100, 100),
                pygame.Rect(100, 620, 860, 100),  # 사각형
                pygame.Rect(900, 480, 60, 140),  # 사각형
                pygame.Rect(150, 720 - 290, 810 ,50),
                pygame.Rect(110, 720 - 380, 40, 140),
                pygame.Rect(110, 720 - 380 - 30, 700 ,30 ),
                pygame.Rect(810, 240, 25 ,100 ),
                pygame.Rect(410, 225, 425 ,15 ),
                pygame.Rect(400, 190, 10 ,50 ),#
                pygame.Rect(400, 180, 300 ,10 ),
                pygame.Rect(700, 140, 8 ,50 ),
                pygame.Rect(500, 134, 208 ,6 ),
                pygame.Rect(480, 134, 20 ,6 )]  # 사각형

        # 마우스 커서의 rect
        x_pos_mouse = 0
        y_pos_mouse = 0
        mouse_rect = pygame.Rect(0, 0, 1, 1)
        # 마우스가 도형 안에 있다면 condition = True
        condition = True

        def game_text(word, x, y, size, color=(0, 255, 255)): # x, y위치에 word를 출력함.
            font = pygame.font.Font(self.font_name, size)
            text = font.render(word, True, color)

            size_width_text, size_height_text = text.get_rect().size
            background.blit(text, (x - size_width_text/2, y - size_height_text/2))


        # 게임 루프
        playing = True
        first = True
        while playing:
            fps.tick(60)
            if first :
                background.fill((0, 0, 0))
                pygame.draw.rect(background, (255, 255, 255), shapes[0])
                game_text("If you want to start Game", self.DISPLAY_W/2, self.DISPLAY_H/2 - 30, 50)
                game_text("Click your mouse white rectangle", self.DISPLAY_W/2, self.DISPLAY_H/2 + 20, 50)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                        return                  
                    if event.type == pygame.MOUSEMOTION:
                        # 마우스 위치를 받아옴.
                        x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()     
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if x_pos_mouse >= 0 and x_pos_mouse <= 100 and y_pos_mouse <= 720 and y_pos_mouse >= 620:  
                            first = False
                            continue
                continue



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  
                if event.type == pygame.MOUSEMOTION:
                    # 마우스 위치를 받아옴.
                    x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos() 
                    if x_pos_mouse < 0:
                        x_pos_mouse = 0
                    elif x_pos_mouse > self.DISPLAY_W:
                        x_pos_mouse = self.DISPLAY_W
                    if y_pos_mouse < 0:
                        y_pos_mouse = 0
                    elif y_pos_mouse > self.DISPLAY_H:
                        y_pos_mouse = self.DISPLAY_H

            # 마우스 위치 업데이트
            mouse_rect.topleft = x_pos_mouse, y_pos_mouse

            # 화면 지우기
            background.fill((0, 0, 0))

            # 도형 그리기
            for shape in shapes:
                if shape == shapes[0]:
                    pygame.draw.rect(background, (255, 255, 255), shape)
                    continue
                if shape == shapes[12]:
                    pygame.draw.rect(background, (255, 255, 255), shape)
                    continue
                pygame.draw.rect(background, (0, 255, 255), shape)
            pygame.draw.circle(background, (0, 0, 0), (x_pos_mouse, y_pos_mouse), 1)
            # 마우스와 도형 충돌 검사
            condition = False # False로 바꾸고 도형들을 돌면서 안에 들어있다면 True로 바꿔줌.
            win = False
            for shape in shapes:
                if shape.colliderect(mouse_rect):
                    condition = True
                if shape == shapes[12]:
                    if shape.colliderect(mouse_rect):
                        win = True

            if not condition: # 도형에서 나간다면
                playing = False
                background.fill((0, 0, 0))
                game_text("You Lose", self.DISPLAY_W/2, self.DISPLAY_H/2, 100, (255, 0, 0))
                pygame.display.update()
                pygame.time.delay(1000)

            if win: # 마지막에 도달한다면 성공조건
                playing = False
                background.fill((0, 0, 0))
                game_text("You Win", self.DISPLAY_W/2, self.DISPLAY_H/2, 100, (255, 0, 0))
                pygame.time.delay(1000)
                win_img = pygame.image.load(r'image\mouse_win.jpg')
                background.blit(win_img, (0,0))
                pygame.display.update()
                pygame.time.delay(3000)



            # 화면 업데이트
            pygame.display.update()