# TO DO
# add z-index to plant class
# add argument for images list to Plant constructor
# add variable width to date display
# change font for day counter (numbers are not as readable as what they should)
# tidy up code w/main function

import pygame

pygame.init()

# game clock
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
days = 1
game_hours = 0
FPS = 60

# list of images for temporary plant
plant_width = 53
plant_height = 122

images = [
    pygame.image.load("temp_plant/plant1.png"),
    pygame.image.load("temp_plant/plant2.png"),
    pygame.image.load("temp_plant/plant3.png"),
    pygame.image.load("temp_plant/plant4.png"),
    pygame.image.load("temp_plant/plant5.png"),
    pygame.image.load("temp_plant/plant6.png")
]

# plant sprite constructor
class Plant(pygame.sprite.Sprite):
    # initalize constructor
    #TO DO -> add argument for images list (to allow for other plants)
    def __init__(self, x, y):
        super().__init__()
        self.age = 0
        self.image = images[self.age]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # update image according to the age of the plant
    def grow(self):
        if self.age < len(images) - 1:
            self.age += 1
            self.image = images[self.age]
        else:
            self.age += 1
            self.image = images[len(images) - 1]

# group for plants
plants = pygame.sprite.Group()

# initalize plants (for testing)
plant1 = Plant(500,500)
plants.add(plant1)
plant2 = Plant(600,300)
plants.add(plant2)

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

canvas = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
pygame.display.set_caption("terraform")

background = pygame.image.load("land.png")
font = pygame.font.Font("PixelifySans-VariableFont_wght.ttf", 32)
day_text = font.render("day " + str(days), False, (255,255,255))

# define colours for different times of the day
morning = (255, 238, 130)
day = (130, 211, 255)
evening = (155,130,255)

canvas.fill(morning)

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if y > CANVAS_HEIGHT/2:
                plants.add(Plant(x, y - (plant_height/2)))

    clock.tick(FPS)
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    game_hours += 1
    
    # for this stage of testing, 1 day equals 6 seconds
    if game_hours == 6*FPS:
        canvas.fill(morning)
        game_hours = 0
        days += 1
        day_text = font.render("day " + str(days), False, (255,255,255))
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
    # TO DO -> create adaptive width
    pygame.draw.rect(canvas, (0,0,0), pygame.Rect(45,45,95,50))
    canvas.blit(day_text, (50, 50))    
    
    plants.draw(canvas)

    pygame.display.update()