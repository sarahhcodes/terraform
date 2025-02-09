import pygame

pygame.init()

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

canvas = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
pygame.display.set_caption("terraform")
start_background = pygame.image.load("images/start_background.png")

# button constructor
class Button:
    def __init__(self, x, y, main_image, hover_image):
        self.image = main_image
        self.hover = hover_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        # set up image so that it changes depending on button state
    
    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover condition
        if self.rect.collidepoint(pos):
            # draw hover image
            canvas.blit(self.hover, (self.rect.x, self.rect.y))

            # check click condition
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            # draw image
            canvas.blit(self.image, (self.rect.x, self.rect.y))

        return action

button_start = Button(56, 362, pygame.image.load("images/button_start.png"), pygame.image.load("images/button_start_hover.png"))

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    canvas.blit(start_background, (0,0))

    if button_start.draw():
        pass
                
    pygame.display.update()