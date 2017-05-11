import pygame # Imports pygame package

pygame.init() #Initializes pygame
screen = pygame.display.set_mode((600, 400)) #Creates a screen

green = (0,128,0) #RGB for color green
red = (255,0,0) #Rgb for color red

running = True
while running:
    for event in pygame.event.get(): #get events from the queue
        if event.type == pygame.QUIT:
            running = False

    screen.fill(green) #fill up screen with green
    pygame.draw.circle(screen, red, (220,200), 100)
    # position (220,200), radius = 100 , makes the circle filled
    #with color red

    pygame.display.flip()
    #Update the full display Surface to the screen

    
