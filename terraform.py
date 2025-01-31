# TO DO
# add onClick event to buttons (change color, highlight, etc)
# create new plant (tree)
# add tree button
# add start page
# add goal screen (make the landscape green)
# add exit button
# add reset button
# tidy code

import pygame
from pygame.sprite import Group
import plant_library # list of all plants

pygame.init()

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

canvas = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
pygame.display.set_caption("terraform")

background = pygame.image.load("land.png")
menu_background = pygame.image.load("menu_background.png").convert_alpha()
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
    def __init__(self, plant_type, x, y):
        super().__init__()
        self.age = 0
        self.plant_type = plant_type["images"]
        self.image = self.plant_type[self.age]
        self.start_point = plant_type["start_draw"]
        self.rect = self.image.get_rect()
        self.rect.center = (x + self.start_point, y) #plant_type should contain pixel value where drawing starts
        self.watered = True # SHOULD DEFAULT TO FALSE
        self._layer = y # allows for plants placed lower on the screen to overlap plants higher

    # update image according to the age of the plant
    def grow(self):
        if self.watered: # make sure plant is watered before growing
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

# text display constructor
class Text:
    def __init__(self, text, size):
        self.font = pygame.font.Font(typeface, size)
        self.text = text
        self.render = self.font.render(self.text, False, font_color)
        self.width, self.height = self.font.size(self.text)
    
    # update text & rerender
    def update(self, text):
        self.text = text
        self.render = self.font.render(self.text, False, font_color)
        self.width, self.height = self.font.size(self.text)

# group for plants
plants = pygame.sprite.LayeredUpdates()

# initalize plants (for testing)
#plant1 = Plant(plant_library.white_flower, 500,500)
#plants.add(plant1)
#plant2 = Plant(plant_library.white_flower, 600,300)
#plants.add(plant2)

# create day display instance
day_display = Text("day " + str(days), 32)

# create menu
menu = Text("choose plant", 16)
menuColor = (0,0,0)

# initalize canvas
canvas.fill(morning)

# initalize buttons
button_flower = Button(326, 555, pygame.image.load("button_flower.png"), pygame.image.load("button_flower_hover.png"))
button_fern = Button(500, 555, pygame.image.load("button_fern.png"), pygame.image.load("button_fern_hover.png"))

exit = False
current_plant = plant_library.fern

# game loop
while not exit:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    menu_x = 50 + day_display.width + 35

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for plant in plants:
                if plant.rect.collidepoint(mouse_x,mouse_y):
                    print('plant!')
            # draw flower if mouse is clicked on ground
            if mouse_y > CANVAS_HEIGHT/2 and mouse_y < 543:
                plants.add(Plant(current_plant, mouse_x, mouse_y - (current_plant['plant_height']/2)))
            # TO DO -> allow for user to choose different plants
            #if menu.rect.collidepoint(mouse_x,mouse_y):
                #pass
                #menuColor = (50,50,50)
                #print("change plant!")

                #90 543 699
            

    clock.tick(FPS)
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    game_hours += 1
    
    # for this stage of testing, 1 day equals 6 seconds
    if game_hours == 6*FPS:
        canvas.fill(morning)
        game_hours = 0
        days += 1
        day_display.update("day " + str(days))
        print(days)
        
        # update plants
        for plant in plants:
            plant.grow()

    elif game_hours == 2*FPS:
        canvas.fill(day)
    elif game_hours == 4*FPS:
        canvas.fill(evening)

    plants.update()

    canvas.blit(background, (0,0))  
    canvas.blit(menu_background, (0,0)) 

    # draw menu buttons
    if button_flower.draw():
        current_plant = plant_library.flower

    if button_fern.draw():
        current_plant = plant_library.fern

    # draw day counter
    #pygame.draw.rect(canvas, (0,0,0), pygame.Rect(45, 45, day_display.width + 15, day_display.height + 10))
    #canvas.blit(day_display.render, (50, 50))    

    # draw menu
    # add hover effect
    #pygame.draw.rect(canvas, menuColor, pygame.Rect(menu_x - 5, 45, 
    #                                              menu.width + 15, day_display.height + 10))
    #canvas.blit(menu.render, (menu_x, 60)) 
    
    plants.draw(canvas)

    pygame.display.update()