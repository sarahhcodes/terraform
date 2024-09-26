# TO DO
# add ability to change plants
# add challenge to plant growth
# tidy up code w/main function

import pygame
import os

# fuction to get subdirectories
def get_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

pygame.init()

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

# get list of image directories
image_directories = get_subdirectories('plants')
print(image_directories)

# TO DO -> fuction to put images for different plants into a list
for directory in image_directories:
    print(directory)
    for f in os.listdir(os.path.join('plants', directory)): # <----- put this into a numbered list (plant1, plant2, etc)
        if os.path.isfile(os.path.join(directory, f)):
            print(f)
            

canvas = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
pygame.display.set_caption("terraform")

background = pygame.image.load("land.png")
typeface = "SourceCodePro-VariableFont_wght.ttf"
font_color = (255, 255, 255)

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
        self.plant_type = plant_type
        self.image = self.plant_type[self.age]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._layer = y # allows for plants placed lower on the screen to overlap plants higher

    # update image according to the age of the plant
    def grow(self):
        if self.age < len(self.plant_type) - 1:
            self.age += 1
            self.image = self.plant_type[self.age]
        else:
            self.age += 1
            self.image = self.plant_type[len(self.plant_type) - 1]

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

# list of images for temporary plant
plant_width = 53
plant_height = 122

white_flower = [
    pygame.image.load("temp_plant/plant1.png"),
    pygame.image.load("temp_plant/plant2.png"),
    pygame.image.load("temp_plant/plant3.png"),
    pygame.image.load("temp_plant/plant4.png"),
    pygame.image.load("temp_plant/plant5.png"),
    pygame.image.load("temp_plant/plant6.png")
]

# group for plants
plants = pygame.sprite.LayeredUpdates()

# initalize plants (for testing)
plant1 = Plant(white_flower, 500,500)
plants.add(plant1)
plant2 = Plant(white_flower, 600,300)
plants.add(plant2)

# create day display instance
day_display = Text("day " + str(days), 32)

# create menu
menu = Text("choose plant", 16)

# define colours for different times of the day
morning = (255, 238, 130)
day = (130, 211, 255)
evening = (155, 130, 255)

# initalize canvas
canvas.fill(morning)

exit = False

# game loop
while not exit:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # draw flower if mouse is clicked on ground
            if mouse_y > CANVAS_HEIGHT/2:
                plants.add(Plant(white_flower, mouse_x, mouse_y - (plant_height/2)))
            # TO DO -> allow for user to choose different plants
            

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

    # draw day counter
    pygame.draw.rect(canvas, (0,0,0), pygame.Rect(45, 45, day_display.width + 15, day_display.height + 10))
    canvas.blit(day_display.render, (50, 50))    

    # draw menu
    # add hover effect
    pygame.draw.rect(canvas, (0,0,0), pygame.Rect(45 + day_display.width + 35, 45, 
                                                  menu.width + 15, day_display.height + 10))
    canvas.blit(menu.render, (50 + day_display.width + 35, 60)) 
    
    plants.draw(canvas)

    pygame.display.update()