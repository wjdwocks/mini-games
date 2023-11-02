import pygame
import random

pygame.init()
fps = pygame.time.Clock()

background = pygame.display.set_mode((960,720))
pygame.display.set_caption("재찬이의 슈팅게임")
## 이미지 로드
# 배경
img_bg = pygame.image.load(r"우주게임\image\Moon.png")

# 캐릭터
img_character_r = pygame.image.load(r"우주게임\image\image2.png")
img_character_l = pygame.image.load(r"우주게임\image\image2.png")
# img_character_death = pygame.image.load(r"")
img_character = img_character_r

# 내 체력
my_hp = "my hp : "
my_hp_point = 10
my_hp_font = pygame.font.SysFont('한글폰트.ttf', 30)


# 적
img_enemy = pygame.image.load(r"우주게임\image\enemy.svg")

# 적 체력
enemy_hp = "enemy hp : "
enemy_hp_point = 10
# 적 폰트, render, blit
enemy_hp_font = pygame.font.SysFont('한글폰트.ttf', 30)

# GameOver Font
gameover_font = pygame.font.SysFont(None, 60)
youwin_font = pygame.font.SysFont(None, 60)

# 총알
img_bullet_my = pygame.image.load(r"우주게임\image\panty (1).png")
img_bullet_enemy = pygame.image.load(r"우주게임\image\Lightning.svg")

## 사이즈 정리
# 이미지 별 사이즈 정리
bg_size_x, bg_size_y = img_bg.get_rect().size
character_size_x, character_size_y = img_character.get_rect().size
enemy_size_x, enemy_size_y = img_enemy.get_rect().size
bullet_my_size_x, bullet_my_size_y = img_bullet_my.get_rect().size
bullet_enemy_size_x, bullet_enemy_size_y = img_bullet_enemy.get_rect().size

## 위치 정리
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

## 적의 위치를 랜덤으로 움직이게 하기.
# 적이 갈 수 있는 위치를 랜덤으로 발생시켜 거기로 가게 하고, 도착하면 다시 랜덤을 발생시켜 움직이게 한다.
random_pos = random.randrange(0, bg_size_x - enemy_size_x) // 8 * 8 + 1
enemy_spd = 8

# 내 이동
character_spd = 8
character_to = 0

# 내 총알
my_bullet = []
rect_my_bullet = []
my_bullet_spd = 6

# 적 총알
enemy_bullet = []
rect_enemy_bullet = []
enemy_bullet_time = 0
random_time = random.randrange(50,200)
enemy_bullet_spd = 6

# 나와 적의 rect
rect_character = img_character.get_rect()
rect_enemy = img_enemy.get_rect()


## 게임 시작
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                img_character = img_character_r
                character_to = character_spd
            if event.key == pygame.K_LEFT:
                img_character = img_character_l
                character_to = -character_spd
            if event.key == pygame.K_SPACE:
                bullet_my_pos_x = character_pos_x + character_size_x/2 - bullet_my_size_x/2
                bullet_my_pos_y = character_pos_y - bullet_my_size_y
                my_bullet.append([bullet_my_pos_x, bullet_my_pos_y])
                rect_my_bullet.append(img_bullet_my.get_rect())
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                character_to = 0
            if event.key == pygame.K_LEFT:
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
    print(character_size_x, character_size_y)
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
    background.blit(text_enemy_hp, (bg_size_x - text_my_hp_x - 40, 10))

    if my_hp == 0:
        background.blit(text_gameover, (bg_size_x / 2 - text_gameover_x / 2, bg_size_y/2 - text_gameover_y))
        pygame.display.update()
        play = False
        pygame.time.delay(3000)
    elif enemy_hp == 0:
        background.blit(text_youwin, (bg_size_x / 2 - text_youwin_x / 2, bg_size_y/2 - text_youwin_y))
        pygame.display.update()
        play = False
        pygame.time.delay(3000)


    pygame.display.update()

pygame.quit()