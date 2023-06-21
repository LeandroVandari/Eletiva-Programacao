import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the initial position of the snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the initial position of the food
food_position = [random.randrange(1, (width//10)) * 10,
                 random.randrange(1, (height//10)) * 10]
food_spawned = True

# Set the initial position of the special apple
special_apple_position = [random.randrange(1, (width//10)) * 10,
                          random.randrange(1, (height//10)) * 10]
special_apple_spawned = False

# Set the initial direction of the snake
direction = 'RIGHT'
change_to = direction

# Set the initial score
score = 0

# Set the initial snake speed and special apple effect duration
snake_speed = 10
special_apple_effect_duration = 5  # In seconds

# Set the clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Define the font for the score display
font = pygame.font.Font(None, 36)


def game_over():
    """Function to display game over message."""
    game_over_text = font.render("Game Over!", True, white)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.midtop = (width/2, height/4)
    window.fill(black)
    window.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Allow the snake to change direction using arrow keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Validate the direction of the snake
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    # Update the position of the snake based on the chosen direction
    if direction == 'UP':
        snake_position[1] -= snake_speed
    if direction == 'DOWN':
        snake_position[1] += snake_speed
    if direction == 'LEFT':
        snake_position[0] -= snake_speed
    if direction == 'RIGHT':
        snake_position[0] += snake_speed

    # Increase the length of the snake when it eats the food
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawned = False
        special_apple_spawned = False
    else:
        snake_body.pop()

    # Spawn new food when the old one is eaten
    if not food_spawned:
        food_position = [random.randrange(1, (width//10)) * 10,
                         random.randrange(1, (height//10)) * 10]
    food_spawned = True

    # Check if special apple should be spawned
    if not special_apple_spawned and random.random() < 0.02:  # 2% chance of special apple spawn
        special_apple_position = [random.randrange(1, (width//10)) * 10,
                                  random.randrange(1, (height//10)) * 10]
        special_apple_spawned = True

    # Draw the background and snake
    window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, red, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    # Draw the special apple
    if special_apple_spawned:
        pygame.draw.rect(window, blue, pygame.Rect(
            special_apple_position[0], special_apple_position[1], 10, 10))

    # Check for collision with boundaries or self
    if snake_position[0] < 0 or snake_position[0] > width-10:
        game_over()
        break
    if snake_position[1] < 0 or snake_position[1] > height-10:
        game_over()
        break
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            break

    # Check if snake ate the special apple
    if snake_position[0] == special_apple_position[0] and snake_position[1] == special_apple_position[1]:
        score += 2
        special_apple_spawned = False
        snake_speed = 5  # Reduce snake speed
        pygame.time.set_timer(pygame.USEREVENT, special_apple_effect_duration * 1000)  # Set timer to revert snake speed

    # Update the score display
    score_text = font.render(f"Score: {score}", True, white)
    score_rect = score_text.get_rect()
    score_rect.midtop = (width/2, 10)
    window.blit(score_text, score_rect)

    # Refresh the game display
    pygame.display.flip()

    # Control the game's frame rate
    clock.tick(20)

    # Check if the special apple effect duration has ended
    if pygame.USEREVENT in pygame.event.get():
        snake_speed = 10  # Restore snake speed
