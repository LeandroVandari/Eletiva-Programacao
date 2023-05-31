# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

class Snake():
    def __init__(self, head: (int, int)):
        self.body: [(int, int)] = [head]
        self.direction: str = "right"
        self.square_to_add_segment: (int, int) = head
        self.length: int = 0

    def move(self, direction: str):
        previous_sqr_pos: (int, int) = self.body[0]
        match direction:
            case "right":
                for index, segment in enumerate(self.body):
                    
                    

                    

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
            

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.update()

            clock.tick(60)  # limits FPS to 60

if __name__ == '__main__':
    main()