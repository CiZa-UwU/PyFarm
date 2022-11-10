import pygame, sys
import button
from settings import *
from level import Level

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# загружаем фоновую музыку
menu_music = pygame.mixer.Sound('music/menumusic.wav')
gameplay_music = pygame.mixer.Sound('music/gameplaymusic.wav')


# класс игры
class Game:
    def __init__(self):

        # инициализации библиотеки и игрового окна
        self.menu_runs = True
        self.gameplay_runs = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('PyFarm')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # выход из геймплея обратно в меню
                if self.gameplay_runs == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            gameplay_music.stop()
                            self.gameplay_runs = False
                            self.menu_runs = True

            # состояние геймплея
            if self.gameplay_runs == True:
                gameplay_music.set_volume(0.5)
                gameplay_music.play(-1)
                dt = self.clock.tick() / 1000
                self.level.run(dt)
                pygame.display.update()

            # состояние меню
            elif self.menu_runs == True:

                # загружаем фоновое изображение для меню
                menu_background = pygame.image.load('backgrounds/mainmenu_background.jpg')

                # загружаем png-изображения кнопок в переменные
                start_image = pygame.image.load('buttons/button_start.png').convert_alpha()
                load_image = pygame.image.load('buttons/button_load.png').convert_alpha()
                exit_image = pygame.image.load('buttons/button_exit.png').convert_alpha()

                # создание объектов-кнопок
                start_button = button.Button(451, 217, start_image)
                load_button = button.Button(451, 302, load_image)
                exit_button = button.Button(451, 387, exit_image)

                # создание меню и возможных вариантов сценариев нажатия на его кнопки
                self.screen.blit(menu_background, (0, 0))
                menu_music.set_volume(0.5)
                menu_music.play(-1)
                if start_button.draw(self.screen):
                    menu_music.stop()
                    self.menu_runs = False
                    self.gameplay_runs = True
                if load_button.draw(self.screen):
                    menu_music.stop()
                    self.menu_runs = False
                    self.gameplay_runs = True
                if exit_button.draw(self.screen):
                    self.menu_runs = False
                    menu_music.stop()
                    pygame.quit()
                    sys.exit()
                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
