# TO DO
# change color of plant button when selected
# clean up background pixels of trees images
# do something with empty spaces on either side of the menu
# add start page
# add goal screen (make the landscape green)
# tidy code

import pygame
from pygame.sprite import Group
import plant_library # list of all plants

pygame.init()

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

canvas = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
pygame.display.set_caption("terraform")

background = pygame.image.load("images/land.png")
menu_background = pygame.image.load("images/menu_background.png").convert_alpha()
typeface = "SourceCodePro-VariableFont_wght.ttf"
font_color = (255, 255, 255)

# define background colours for different times of the day
morning = (255, 238, 130)
day = (130, 211, 255)
evening = (155, 130, 255)

# game clock
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
days = 1
game_hours = 0
FPS = 60

# plant sprite constructor
class Plant(pygame.sprite.Sprite):
    # initalize constructor
    def __init__(self, plant_type, x, y, click):
        super().__init__()
        self.age = 0
        self.plant_type = plant_type["images"]
        self.image = self.plant_type[self.age]
        self.start_point = plant_type["start_draw"]
        self.rect = self.image.get_rect()
        self.rect.center = (x + self.start_point, y) #plant_type should contain pixel value where drawing starts
        self._layer = click # allows for plants placed lower on the screen to overlap plants higher

    # update image according to the age of the plant
    def grow(self):
        if self.age < len(self.plant_type) - 1:
            self.age += 1
            self.image = self.plant_type[self.age]
        else:
            self.age += 1
            self.image = self.plant_type[len(self.plant_type) - 1]

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

# group for plants
plants = pygame.sprite.LayeredUpdates()

# initalize canvas
canvas.fill(morning)

# initalize buttons
button_tree = Button(200, 555, pygame.image.load("images/button_tree.png"), pygame.image.load("images/button_tree_hover.png"))
button_flower = Button(326, 555, pygame.image.load("images/button_flower.png"), pygame.image.load("images/button_flower_hover.png"))
button_fern = Button(500, 555, pygame.image.load("images/button_fern.png"), pygame.image.load("images/button_fern_hover.png"))

button_exit = Button(7, 5, pygame.image.load("images/button_exit.png"), pygame.image.load("images/button_exit_hover.png"))
button_reset = Button(670, 5, pygame.image.load("images/button_reset.png"), pygame.image.load("images/button_reset_hover.png"))

exit = False
current_plant = plant_library.fern # start game with fern
time_of_day = morning # start game in the morning

# game loop
while not exit:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # draw plant if mouse is clicked on ground
            if mouse_y > CANVAS_HEIGHT/2 and mouse_y < 543:
                plants.add(Plant(current_plant, mouse_x, mouse_y - (current_plant['plant_height']/2), mouse_y))
            
    # in game clock
    clock.tick(FPS)
    #seconds = (pygame.time.get_ticks()-start_ticks)/1000
    game_hours += 1
    
    # action for the end of each day
    # for this stage of testing, 1 day equals 6 seconds
    if game_hours == 6*FPS:
        time_of_day = morning
        game_hours = 0
        days += 1
        print(days)
        
        # update plants
        for plant in plants:
            plant.grow()

    elif game_hours == 2*FPS:
        time_of_day = day
    elif game_hours == 4*FPS:
        time_of_day = evening

    plants.update()

    # draw background
    canvas.fill(time_of_day)
    canvas.blit(background, (0,0))  
    canvas.blit(menu_background, (0,0)) 

    # draw menu buttons
    if button_tree.draw():
        current_plant = plant_library.tree
    if button_flower.draw():
        current_plant = plant_library.flower
    if button_fern.draw():
        current_plant = plant_library.fern
    
    plants.draw(canvas)

    # draw exit & reset buttons
    if button_exit.draw():
        exit = True # quit game
    if button_reset.draw():
        plants = pygame.sprite.LayeredUpdates() # reset plants

    pygame.display.update()