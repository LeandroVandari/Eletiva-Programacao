import pygame
import math


pygame.init()

WIDTH, HEIGHT =  800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

FONT = pygame.font.SysFont("comicsans", 16)
class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU  # 1AU = 100 pixels
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)

planets = []
earth = Planet(100, 100, 20, BLUE, 10)
planets.append(earth)
running = True
clock = pygame.time.Clock()
while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break

        if running:
            WIN.fill((0, 0, 0))
            # fill the screen with a color to wipe away anything from last frame
            for planet in planets:
                planet.draw()
                
                
                

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.update()

            clock.tick(60)