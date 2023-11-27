import pygame

# (x, y, w, h)

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 # 화면의 중심좌표.
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20) # 커서 크기를 20px x 20px크기로 함.
        self.offset = -120 # 시작 커서의 위치를 조정해주는 변수.
    
    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y) # *을 15사이즈로, x, y에 그린다.

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0)) # game의 display와 같은것을 그려 넣음.
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start" # 커서의 시작 위치.
        self.startx, self.starty = self.mid_w, self.mid_h + 40 # start 버튼의 위치 (중앙기준).
        self.optionx, self.optiony = self.mid_w, self.mid_h + 70 # option버튼의 위치.
        self.Creditx, self.Credity = self.mid_w, self.mid_h + 100 # Credit 버튼의 위치.
        self.exitx, self.exity = self.mid_w, self.mid_h + 130 # Exit 버튼의 위치
        self.menual_x, self.menual_y = 2*self.mid_w - 150, 20
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # 커서의 시작 위치.
        

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events() # 키가 눌렸다면 어떤 키가 눌렸는지 확인
            self.check_input() # 그 키가 어떤 거였는지 확인하고, 메인메뉴에서는 그에 해당하는 이벤트(커서 움직이기)를 한 뒤 enter가 입력되면 그에 맞는 일을 수행함.
            # 메인메뉴 화면 채우기.
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text("Main Menu", 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 60)
            self.game.draw_text("Start Game", 40, self.startx, self.starty)
            self.game.draw_text("Options", 40, self.optionx, self.optiony)
            self.game.draw_text("Credits", 40, self.Creditx, self.Credity)
            self.game.draw_text("Exits", 40, self.exitx, self.exity)
            self.game.draw_text(f"W / UP : move to cursor up", 20, self.menual_x, self.menual_y)
            self.game.draw_text(f"S / DOWN : move to cursor down", 20, self.menual_x, self.menual_y+20)
            self.game.draw_text(f"BackSpace / ESC : back to previous Menu", 20, self.menual_x-20, self.menual_y+40)
            self.game.draw_text(f"Enter / Space bar : select it", 20, self.menual_x, self.menual_y+60)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self): 
        if self.game.DOWN_KEY or self.game.S_KEY: # 아레 키가 눌렸을 때
            if self.state == 'Start': # start에 있었다면 
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony) # option위치로 커서를 옮김.
                self.state = 'Options' 
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.Creditx + self.offset, self.Credity) # Credit으로
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity) # start로 다시
                self.state = 'Exits'
            elif self.state == 'Exits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # start로 다시
                self.state = 'Start'
        elif self.game.UP_KEY or self.game.W_KEY: # 위 키가 눌렸을 때
            if self.state == 'Start': # start에 있었다면 
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity) # Credit위치로 커서를 옮김.
                self.state = 'Exits' 
            elif self.state == 'Options': # option에 있었다면
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # start로
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionx + self.offset, self.optiony) # option으로
                self.state = 'Options'
            elif self.state == 'Exits':
                self.cursor_rect.midtop = (self.Creditx + self.offset, self.Credity) # start로 다시
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor() # 커서를 움직이거나 함.
        if self.game.START_KEY or self.game.SPACE: # enter키가 눌리면?
            if self.state == 'Start': # Start였다면? 
                self.game.curr_menu = self.game.games # game 메뉴로 이동
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options # option 메뉴로 이동
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits # credit 메뉴로 이동.
            elif self.state == 'Exits':
                self.game.playing = False
                self.game.running = False
            self.run_display = False # 이 메인 메뉴를 닫음.


class GameMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'SpaceGame' # 커서의 시작 포인터
        self.firstx, self.firsty = self.mid_w, self.mid_h + 30 # 화면의 정중앙 mid_w, mid_h
        self.secondx, self.secondy = self.mid_w, self.mid_h + 70
        self.thirdx, self.thirdy = self.mid_w, self.mid_h + 110
        self.fourthx, self.fourthy = self.mid_w, self.mid_h + 150
        self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty) # 시작커서 위치. SpaceGame이 가장 위에 있기 때문에
        self.menual_x, self.menual_y = 2*self.mid_w - 150, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text('Games', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 60)
            self.game.draw_text('SpaceGame', 40, self.firstx, self.firsty)
            self.game.draw_text('BrickBreaking', 40, self.secondx, self.secondy)
            self.game.draw_text('EscapePoo', 40, self.thirdx, self.thirdy)
            self.game.draw_text('Mouse Maze', 40, self.fourthx, self.fourthy)
            self.game.draw_text(f"W / UP : move to cursor up", 20, self.menual_x, self.menual_y)
            self.game.draw_text(f"S / DOWN : move to cursor down", 20, self.menual_x, self.menual_y+20)
            self.game.draw_text(f"BackSpace / ESC : back to previous Menu", 20, self.menual_x-20, self.menual_y+40)
            self.game.draw_text(f"Enter / Space bar : select it", 20, self.menual_x, self.menual_y+60)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY or self.game.ESC: # backspace나 ESC가 눌리면
            self.game.curr_menu = self.game.main_menu # 현재 메뉴를 메인메뉴로 바꿈.
            self.run_display = False # 현재 메뉴상태를 False로 바꿈.
        elif self.game.DOWN_KEY or self.game.S_KEY:
            if self.state == 'SpaceGame':
                self.state = 'BrickBreaking'
                self.cursor_rect.midtop = (self.secondx + self.offset, self.secondy)
            elif self.state == 'BrickBreaking':
                self.state = 'EscapePoo'
                self.cursor_rect.midtop = (self.thirdx + self.offset, self.thirdy)
            elif self.state == 'EscapePoo':
                self.state = 'MouseMaze'
                self.cursor_rect.midtop = (self.fourthx + self.offset, self.fourthy)
            elif self.state == 'MouseMaze':
                self.state = 'SpaceGame'
                self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
        elif self.game.UP_KEY or self.game.W_KEY:
            if self.state == 'SpaceGame':
                self.state = 'MouseMaze'
                self.cursor_rect.midtop = (self.fourthx + self.offset, self.fourthy)
            elif self.state == 'BrickBreaking':
                self.state = 'SpaceGame'
                self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
            elif self.state == 'EscapePoo':
                self.state = 'BrickBreaking'
                self.cursor_rect.midtop = (self.secondx + self.offset, self.secondy)
            elif self.state == 'MouseMaze':
                self.state = 'EscapePoo'
                self.cursor_rect.midtop = (self.thirdx + self.offset, self.thirdy)
        elif self.game.START_KEY or self.game.SPACE:
            if self.state == 'SpaceGame': # SpaceGame에서 엔터를 누르면 FirstGame 으로 이동.
                self.game.curr_menu = self.game.space
                # Space Game을 누른다면 그쪽 메뉴로 보내버림.
            elif self.state == 'BrickBreaking':
                self.game.curr_menu = self.game.brick
            elif self.state == 'EscapePoo':
                self.game.curr_menu = self.game.poo
            elif self.state == 'MouseMaze':
                self.game.curr_menu = self.game.mouse
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'bgMode' # 커서의 시작 위치
        self.bgModex, self.bgModey = self.mid_w, self.mid_h+30 # 화면의 정중앙 mid_w, mid_h
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.bgModex + self.offset, self.bgModey) # 볼륨 커서 위치. 볼륨이 가장 위에 있기 때문에
        self.bgColor = 'White Mode'
        self.menual_x, self.menual_y = 2*self.mid_w - 150, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text('Options', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 60)
            self.game.draw_text(self.bgColor, 40, self.bgModex, self.bgModey)
            self.game.draw_text('Controls', 40, self.controlsx, self.controlsy)
            self.game.draw_text(f"W / UP : move to cursor up", 20, self.menual_x, self.menual_y)
            self.game.draw_text(f"S / DOWN : move to cursor down", 20, self.menual_x, self.menual_y+20)
            self.game.draw_text(f"BackSpace / ESC : back to previous Menu", 20, self.menual_x-20, self.menual_y+40)
            self.game.draw_text(f"Enter / Space bar : select it", 20, self.menual_x, self.menual_y+60)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY or self.game.ESC: # backspace가 눌리면
            self.game.curr_menu = self.game.main_menu # 현재 메뉴를 메인메뉴로 바꿈.
            self.run_display = False # 현재 메뉴상태를 False로 바꿈.
        elif self.game.UP_KEY or self.game.W_KEY or self.game.DOWN_KEY or self.game.S_KEY:
            if self.state == 'bgMode':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'bgMode'
                self.cursor_rect.midtop = (self.bgModex + self.offset, self.bgModey)
        elif self.game.START_KEY or self.game.SPACE:
            if self.state == 'bgMode':
                if self.bgColor == 'White Mode':
                    self.game.bgColor = self.game.WHITE
                    self.game.textColor = self.game.BLACK
                    self.bgColor = 'Black Mode'
                elif self.bgColor == 'Black Mode':
                    self.game.bgColor = self.game.BLACK
                    self.game.textColor = self.game.WHITE
                    self.bgColor = 'White Mode'
                # bgMode일 때 할 일을 수행하게 함.
            elif self.state == 'Controls':
                pass
                # Controls일 때 할 일을 수행하게 함.


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menual_x, self.menual_y = 2*self.mid_w - 150, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY or self.game.ESC or self.game.SPACE:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text(f"Enter / ESC / SPACE Bar : back to previous Menu", 20, self.menual_x, self.menual_y)
            self.game.draw_text('Credits', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 60)
            self.game.draw_text('Made by me', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 40 )
            self.blit_screen()



class SpaceGameMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = '1p' # 커서의 시작 위치
        self._1px, self._1py = self.mid_w, self.mid_h + 30 # 화면의 정중앙 mid_w, mid_h
        self._2px, self._2py = self.mid_w, self.mid_h + 60
        self.GameMenualx, self.GameMenualy = self.mid_w, self.mid_h + 90
        self.GameMenual2x, self.GameMenual2y = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self._1px + self.offset, self._1py) # 1p의 위치
        self.menual_x, self.menual_y = 2*self.mid_w - 150, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text('Space Games', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 60)
            self.game.draw_text('1Person Mode', 40, self._1px, self._1py)
            self.game.draw_text('2Person Mode', 40, self._2px, self._2py)
            self.game.draw_text('GameMenual 1p', 40, self.GameMenualx, self.GameMenualy)
            self.game.draw_text('GameMenual 2p', 40, self.GameMenual2x, self.GameMenual2y)
            self.game.draw_text(f"W / UP : move to cursor up", 20, self.menual_x, self.menual_y)
            self.game.draw_text(f"S / DOWN : move to cursor down", 20, self.menual_x, self.menual_y+20)
            self.game.draw_text(f"BackSpace / ESC : back to previous Menu", 20, self.menual_x-20, self.menual_y+40)
            self.game.draw_text(f"Enter / Space bar : select it", 20, self.menual_x, self.menual_y+60)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY or self.game.ESC: # backspace가 눌리면
            self.game.curr_menu = self.game.games # 현재 메뉴를 게임메뉴로 바꿈.
            self.run_display = False # 현재 메뉴상태를 False로 바꿈.
            self.game.reset_keys()
        elif self.game.UP_KEY or self.game.W_KEY:
            if self.state == '1p':
                self.state = 'GM2'
                self.cursor_rect.midtop = (self.GameMenual2x + self.offset, self.GameMenual2y)
            elif self.state == '2p':
                self.state = '1p'
                self.cursor_rect.midtop = (self._1px + self.offset, self._1py)
            elif self.state == 'GM1':
                self.state = '2p'
                self.cursor_rect.midtop = (self._2px + self.offset, self._2py)
            elif self.state == 'GM2':
                self.state = 'GM1'
                self.cursor_rect.midtop = (self.GameMenualx + self.offset, self.GameMenualy)
        elif self.game.DOWN_KEY or self.game.S_KEY:
            if self.state == '1p':
                self.state = '2p'
                self.cursor_rect.midtop = (self._2px + self.offset, self._2py)
            elif self.state == '2p':
                self.state = 'GM1'
                self.cursor_rect.midtop = (self.GameMenualx + self.offset, self.GameMenualy)
            elif self.state == 'GM1':
                self.state = 'GM2'
                self.cursor_rect.midtop = (self.GameMenual2x + self.offset, self.GameMenual2y)
            elif self.state == 'GM2':
                self.state = '1p'
                self.cursor_rect.midtop = (self._1px + self.offset, self._1py)
        elif self.game.START_KEY or self.game.SPACE:
            if self.state == '1p':
                self.game.game_select = 'space game 1p'
                self.game.playing = True
                self.game.curr_menu = 'NULL'
            elif self.state == '2p':
                self.game.game_select = 'space game 2p'
                self.game.playing = True
                self.game.curr_menu = 'NULL'
            elif self.state == 'GM1':
                self.game.curr_menu = self.game.spaceMenual_1p
            elif self.state == 'GM2':
                self.game.curr_menu = self.game.spaceMenual_2p
            self.run_display = False

class SpaceMenual_1p(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menual_x, self.menual_y = 2*self.mid_w - 200, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY or self.game.ESC or self.game.SPACE:
                self.game.curr_menu = self.game.space
                self.run_display = False
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text(f"Enter / ESC : back to previous Menu", 20, self.menual_x, self.menual_y)
            self.game.draw_text('Space Game Menual 1p', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 120)
            self.game.draw_text('A key and LEFT arrow key is move left', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 20 )
            self.game.draw_text('D key and RIGHT arrow key is move right', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 60 )
            self.game.draw_text('Space bar is shoot your bullet', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 100 )
            self.blit_screen()

class SpaceMenual_2p(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menual_x, self.menual_y = 2*self.mid_w - 200, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY or self.game.ESC or self.game.SPACE:
                self.game.curr_menu = self.game.space
                self.run_display = False
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text(f"Enter / ESC / SPACE bar: back to previous Menu", 20, self.menual_x, self.menual_y)
            self.game.draw_text('Space Game Menual 2p', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 120)
            self.game.draw_text('1P : RIGHT and LEFT arrow to move', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 20 )
            self.game.draw_text('1P : number 0 in number pad to shot bullet', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 60 )
            self.game.draw_text('2P : A and D key to move', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 100 )
            self.game.draw_text('2P : space bar to shot bullet', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 140 )
            self.blit_screen()


class BrickBreakingMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'BrickStart' # 커서의 시작 위치
        self.startx, self.starty = self.mid_w, self.mid_h + 50 # 화면의 정중앙 mid_w, mid_h
        self.GameMenualx, self.GameMenualy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # start 버튼의 위치
        self.menual_x, self.menual_y = 2*self.mid_w - 150, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text('BrickBreaking Games', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 60)
            self.game.draw_text('Start', 40, self.startx, self.starty)
            self.game.draw_text('GameMenual', 40, self.GameMenualx, self.GameMenualy)
            self.game.draw_text(f"W / UP : move to cursor up", 20, self.menual_x, self.menual_y)
            self.game.draw_text(f"S / DOWN : move to cursor down", 20, self.menual_x, self.menual_y+20)
            self.game.draw_text(f"BackSpace / ESC : back to previous Menu", 20, self.menual_x-20, self.menual_y+40)
            self.game.draw_text(f"Enter / Space bar : select it", 20, self.menual_x, self.menual_y+60)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY or self.game.ESC: # backspace가 눌리면
            self.game.curr_menu = self.game.games # 현재 메뉴를 게임메뉴로 바꿈.
            self.run_display = False # 현재 메뉴상태를 False로 바꿈.
            self.game.reset_keys()
        elif self.game.UP_KEY or self.game.W_KEY or self.game.DOWN_KEY or self.game.S_KEY:
            if self.state == 'BrickStart':
                self.state = 'BrickMenual'
                self.cursor_rect.midtop = (self.GameMenualx + self.offset, self.GameMenualy)
            elif self.state == 'BrickMenual':
                self.state = 'BrickStart'
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        elif self.game.START_KEY or self.game.SPACE:
            if self.state == 'BrickStart':
                self.game.game_select = 'BrickStart'
                self.game.playing = True
                self.game.curr_menu = 'NULL'
            elif self.state == 'BrickMenual':
                self.game.curr_menu = self.game.brickMenual
            self.run_display = False


class BrickMenual(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menual_x, self.menual_y = 2*self.mid_w - 200, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY or self.game.ESC or self.game.SPACE:
                self.game.curr_menu = self.game.brick
                self.run_display = False
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text(f"Enter / ESC / BACKSPACE : back to previous Menu", 20, self.menual_x, self.menual_y)
            self.game.draw_text('BrickBreaking Game Menual', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 120)
            self.game.draw_text('This Game use only mouse.', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 20 )
            self.game.draw_text('You can move the pedal your mouse move.', 40, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 60 )
            
            self.blit_screen()



class EscapePooMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'PooStart' # 커서의 시작 위치
        self.startx, self.starty = self.mid_w, self.mid_h + 50 # 화면의 정중앙 mid_w, mid_h
        self.GameMenualx, self.GameMenualy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # start 버튼의 위치
        self.menual_x, self.menual_y = 2*self.mid_w - 150, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text('EscapePoo Games', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 60)
            self.game.draw_text('Start', 40, self.startx, self.starty)
            self.game.draw_text('GameMenual', 40, self.GameMenualx, self.GameMenualy)
            self.game.draw_text(f"W / Up : move to cursor up", 20, self.menual_x, self.menual_y)
            self.game.draw_text(f"S / Down : move to cursor down", 20, self.menual_x, self.menual_y+20)
            self.game.draw_text(f"BackSpace / ESC : back to previous Menu", 20, self.menual_x-20, self.menual_y+40)
            self.game.draw_text(f"Enter / Space bar : select it", 20, self.menual_x, self.menual_y+60)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY or self.game.ESC: # backspace가 눌리면
            self.game.curr_menu = self.game.games # 현재 메뉴를 게임메뉴로 바꿈.
            self.run_display = False # 현재 메뉴상태를 False로 바꿈.
            self.game.reset_keys()
        elif self.game.UP_KEY or self.game.W_KEY or self.game.DOWN_KEY or self.game.S_KEY:
            if self.state == 'PooStart':
                self.state = 'PooMenual'
                self.cursor_rect.midtop = (self.GameMenualx + self.offset, self.GameMenualy)
            elif self.state == 'PooMenual':
                self.state = 'PooStart'
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        elif self.game.START_KEY or self.game.SPACE:
            if self.state == 'PooStart':
                self.game.game_select = 'PooStart'
                self.game.playing = True
                self.game.curr_menu = 'NULL'
            elif self.state == 'PooMenual':
                self.game.curr_menu = self.game.pooMenual
            self.run_display = False

class PooMenual(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menual_x, self.menual_y = 2*self.mid_w - 200, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY or self.game.ESC or self.game.SPACE:
                self.game.curr_menu = self.game.poo
                self.run_display = False
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text(f"Enter / ESC / BACKSPACE : back to previous Menu", 20, self.menual_x, self.menual_y)
            self.game.draw_text('EscapePoo Game Menual', 70, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 120)
            self.game.draw_text('You can move your character left to A Key and Left Arrow.', 30, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 20 )
            self.game.draw_text('Also you can move your character right to D Key and Right Arrow.', 30, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 60 )
            self.game.draw_text('You have 3 chance to hit the falling poo.', 30, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 100 )
            
            self.blit_screen()



class MouseMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'MouseStart' # 커서의 시작 위치
        self.startx, self.starty = self.mid_w, self.mid_h + 50 # 화면의 정중앙 mid_w, mid_h
        self.GameMenualx, self.GameMenualy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # start 버튼의 위치
        self.menual_x, self.menual_y = 2*self.mid_w - 150, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text('MouseMaze Games', 80, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 60)
            self.game.draw_text('Start', 40, self.startx, self.starty)
            self.game.draw_text('GameMenual', 40, self.GameMenualx, self.GameMenualy)
            self.game.draw_text(f"W / UP : move to cursor up", 20, self.menual_x, self.menual_y)
            self.game.draw_text(f"S / DOWN : move to cursor down", 20, self.menual_x, self.menual_y+20)
            self.game.draw_text(f"BackSpace / ESC : back to previous Menu", 20, self.menual_x-20, self.menual_y+40)
            self.game.draw_text(f"Enter / Space bar : select it", 20, self.menual_x, self.menual_y+60)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY or self.game.ESC: # backspace가 눌리면
            self.game.curr_menu = self.game.games # 현재 메뉴를 게임메뉴로 바꿈.
            self.run_display = False # 현재 메뉴상태를 False로 바꿈.
            self.game.reset_keys()
        elif self.game.UP_KEY or self.game.W_KEY or self.game.DOWN_KEY or self.game.S_KEY:
            if self.state == 'MouseStart':
                self.state = 'MouseMenual'
                self.cursor_rect.midtop = (self.GameMenualx + self.offset, self.GameMenualy)
            elif self.state == 'MouseMenual':
                self.state = 'MouseStart'
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        elif self.game.START_KEY or self.game.SPACE:
            if self.state == 'MouseStart':
                self.game.game_select = 'MouseStart'
                self.game.playing = True
                self.game.curr_menu = 'NULL'
            elif self.state == 'MouseMenual':
                self.game.curr_menu = self.game.mouseMenual
            self.run_display = False

class MouseMenual(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.menual_x, self.menual_y = 2*self.mid_w - 200, 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY or self.game.ESC or self.game.SPACE:
                self.game.curr_menu = self.game.poo
                self.run_display = False
            self.game.display.fill(self.game.bgColor)
            self.game.draw_text(f"Enter / ESC / BACKSPACE : back to previous Menu", 20, self.menual_x, self.menual_y)
            self.game.draw_text('MouseMaze Game Menual', 70, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 120)
            self.game.draw_text('This game only use your mouse', 30, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 20 )
            self.game.draw_text('Your mouse only can stay in colored area.', 30, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 60 )
            self.game.draw_text('If your mouse over the colored area, GAME OVER', 30, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 100 )
            
            self.blit_screen()