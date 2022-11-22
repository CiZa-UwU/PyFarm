import pygame

#класс кнопка
class Button():

    #конструктор кнопки, поля: координаты кнопки на экране по x и y, переменная-изображение кнопки, 'нажата ли кнопка'
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    #метод проверки нажатия кнопки и её помещения на экран
    def draw(self, surface):

        #предварительная проверка: нахождение курсора мыши внутри кнопки и нажатие левой кнопки мыши в данный момент
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #помещение кнопки на экран
        surface.blit(self.image, (self.rect.x, self.rect.y))

        #если переменная action = true, даётся возможность описания различных сценариев действия различных кнопок в main
        return action