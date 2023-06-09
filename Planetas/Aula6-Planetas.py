# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

def main(): 
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break

        if running:
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("grey")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.update()

            clock.tick(60)  # limits FPS to 60

if __name__ == '__main__':
    main()