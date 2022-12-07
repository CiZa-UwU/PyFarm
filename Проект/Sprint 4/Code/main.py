import pygame, sys
import button
from settings import *
from level import Level
from player import *
import cv2

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# game
class Game:
    def __init__(self):

        # initialization
        self.menu_runs = False
        self.gameplay_runs = False
        self.intro_runs = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('PyFarm')
        self.clock = pygame.time.Clock()
        self.level = Level()

        #music
        self.menu_music = pygame.mixer.Sound('music/menumusic.wav')
        self.gameplay_music = pygame.mixer.Sound('music/gameplaymusic.wav')
        self.intro_music = pygame.mixer.Sound('music/game_intro_music.wav')

    def run(self):
        while True:
            clock = pygame.time.Clock()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # exit
                if self.gameplay_runs == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.gameplay_music.stop()
                            self.gameplay_runs = False
                            self.menu_runs = True

            #intro-video status
            if self.intro_runs == True:
                introname = 'videos/game_intro.mp4'
                cap = cv2.VideoCapture(introname)
                ret, img = cap.read()
                if not ret:
                    print("Can't read stream")
                    pygame.quit()
                    sys.exit()
                img = cv2.resize(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
                img = cv2.transpose(img)
                surface = pygame.surface.Surface((img.shape[0], img.shape[1]))
                clock = pygame.time.Clock()
                vFPS = 30
                self.intro_music.play(0)
                intro_running = True
                while intro_running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            intro_running = False
                            self.intro_runs = False
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                intro_running = False
                                self.intro_runs = False
                                self.menu_runs = True
                    ret, img = cap.read()
                    if not ret:
                        intro_running = False
                        break
                    else:
                        img = cv2.resize(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        img = cv2.transpose(img)
                        pygame.surfarray.blit_array(surface, img)
                        self.screen.blit(surface, (0, 0))
                    pygame.display.flip()
                    clock.tick(vFPS)
                if intro_running == False:
                    self.intro_music.stop()

            # gameplay status
            if self.gameplay_runs == True:
                self.gameplay_music.set_volume(0.1)
                self.gameplay_music.play(-1)
                dt = self.clock.tick() / 1000
                self.level.run(dt)
                pygame.display.update()

            # menu status
            elif self.menu_runs == True:

                # menu
                menu_background = pygame.image.load('backgrounds/mainmenu_background.jpg')

                # buttons
                start_image = pygame.image.load('buttons/button_start.png').convert_alpha()
                load_image = pygame.image.load('buttons/button_load.png').convert_alpha()
                exit_image = pygame.image.load('buttons/button_exit.png').convert_alpha()

                # buttons-object
                start_button = button.Button(451, 217, start_image)
                load_button = button.Button(451, 302, load_image)
                exit_button = button.Button(451, 387, exit_image)

                # menu click
                self.screen.blit(menu_background, (0, 0))
                self.menu_music.set_volume(0.5)
                self.menu_music.play(-1)
                if start_button.draw(self.screen):
                    self.menu_music.stop()
                    self.menu_runs = False
                    self.gameplay_runs = True
                if load_button.draw(self.screen):
                    self.menu_music.stop()
                    self.menu_runs = False
                    self.gameplay_runs = True
                if exit_button.draw(self.screen):
                    self.menu_runs = False
                    self.menu_music.stop()
                    pygame.quit()
                    sys.exit()
                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
