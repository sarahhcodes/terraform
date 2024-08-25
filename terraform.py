# TO DO
# count days
# add plants

import pygame

pygame.init()
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

canvas = pygame.display.set_mode((800,600))
pygame.display.set_caption("terraform")

background = pygame.image.load("land.png")

# define colours for different times of the day
morning = (255, 238, 130)
day = (130, 211, 255)
evening = (155,130,255)

canvas.fill(morning)

exit = False

while not exit:
    clock.tick(60)
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    print(seconds)

    # TO DO -> reset clock every "day"; count days
    # for this stage of testing, 1 day equals 15 seconds
    if int(seconds) == 15:
        canvas.fill(morning)
    elif int(seconds) == 5:
        canvas.fill(day)
    elif int(seconds) == 10:
        canvas.fill(evening)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    canvas.blit(background, (0,0))       
    pygame.display.update()