import pygame

import math

#initialize pygame window
pygame.init()
screenWidth = 1000
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Chaikin curves')

#fps display
clock = pygame.time.Clock()
def displayFPS(screen, font_size):
    font = pygame.font.SysFont(None, font_size)
    fps = round(clock.get_fps(), 1)
    fps_text = font.render(f"{fps}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

#CLASS DEFINITION -----------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION DEFINITION - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def chaikin(points):
    #create new points array
    newPoints = []

    #go through each line segment / pair of points
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]  #loop from last to first point for closed loop

        #get first fourth and last fourht vector points
        vecTo = (p2[0] - p1[0], p2[1] - p1[1])
        vecFourth = (vecTo[0] / 4, vecTo[1] / 4)

        np1 = (p1[0] + vecFourth[0], p1[1] + vecFourth[1])
        np2 = (p1[0] + vecFourth[0] * 3, p1[1] + vecFourth[1] * 3)

        #add new points to the newpoints array ... forget parent points
        newPoints.append(np1)
        newPoints.append(np2)

    return newPoints

#VARIABLE INITIALIZATION -----------------------------------------------------------------------------------------------------------------------------------------

#get initial ticks
prevT = pygame.time.get_ticks()

constraints = [(249, 139), (318, 399), (782, 103)]

#run the iterations on the initial constraint points to get a list of point to form the smooth curve
iterations = 10
points = constraints
for i in range(iterations):
    points = chaikin(points)

#WHILE LOOP - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

running = True
while running:

    #update delta time
    currT = pygame.time.get_ticks()
    dTms = currT - prevT
    dTs = dTms / 1000.0

    #fill screen
    screen.fill((20, 20, 20))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw smoothed curve
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]  #loop from last to first point for closed loop

        pygame.draw.line(screen, (255, 255, 255), p1, p2, 2)

    #draw constraint points
    for constraint in constraints:
        pygame.draw.circle(screen, (255, 0, 0), constraint, 4)

    # Update the display (buffer flip)
    displayFPS(screen, 25)
    pygame.display.flip()
    clock.tick(60)

    #update delta time
    prevT = currT

# Quit Pygame
pygame.quit()
