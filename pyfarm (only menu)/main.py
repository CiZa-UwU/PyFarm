import pygame
import button
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#переменные: ширина и высота окна игры
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

#создаём окно игры с переменными выше и задаём имя окну
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('pyfarm demo')

#'состояния игры'
menu_runs = True

#загружаем png-изображения кнопок в переменные
start_image = pygame.image.load('buttons/button_start.png').convert_alpha()
load_image = pygame.image.load('buttons/button_load.png').convert_alpha()
quit_image = pygame.image.load('buttons/button_quit.png').convert_alpha()

#загружаем фоновые изображения для двух разных состояний игры
menu_background = pygame.image.load('backgrounds/mainmenu_background.jpg')
gameplay_background = pygame.image.load('backgrounds/maingame_state.jpg')

#загружаем фоновую музыку
menu_music = pygame.mixer.Sound('music/menumusic.wav')
gameplay_music = pygame.mixer.Sound('music/penismusic.wav')

#создание объектов-кнопок
start_button = button.Button(300, 180, start_image)
load_button = button.Button(300, 300, load_image)
quit_button = button.Button(300, 420, quit_image)

#цикл игры
run = True
while run:
    screen.fill((147, 112, 219))

    #создание меню и возможных вариантов сценариев нажатия на его кнопки
    if menu_runs == True:
        screen.blit(menu_background, (0, 0))
        menu_music.play(-1)
        if start_button.draw(screen):
            menu_music.stop()
            menu_runs = False
        if load_button.draw(screen):
            menu_music.stop()
            menu_runs = False
        if quit_button.draw(screen):
            menu_music.stop()
            run = False

    #состояние игры вне меню
    else:
        screen.blit(gameplay_background, (0, 0))
        gameplay_music.play(-1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                gameplay_music.stop()
                menu_runs = True
        if event.type == pygame.QUIT:
            gameplay_music.stop()
            run = False

    pygame.display.update()

pygame.quit()