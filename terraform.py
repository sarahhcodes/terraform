# TO DO
# add plants

import pygame

pygame.init()

#game clock
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
days = 0
game_hours = 0

canvas = pygame.display.set_mode((800,600))
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
    clock.tick(60)
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    game_hours += 1
    
    # for this stage of testing, 1 day equals 15 seconds (900 frames)
    if game_hours == 900:
        canvas.fill(morning)
        game_hours = 0
        days += 1
        day_text = font.render("day " + str(days), False, (255,255,255))
        print(days)
    elif game_hours == 300:
        canvas.fill(day)
    elif game_hours == 600:
        canvas.fill(evening)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    canvas.blit(background, (0,0))  
    # TO DO -> create adaptive width
    pygame.draw.rect(canvas, (0,0,0), pygame.Rect(45,45,95,50))
    canvas.blit(day_text, (50, 50))    

    pygame.display.update()