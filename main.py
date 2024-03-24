from microbit import *
import random

# Define the initial position of the player
player_x = 2

# Define the obstacle speed (higher value = slower speed)
obstacle_speed = 20  # Decreased for easier testing

# Initialize the game
obstacles = []
game_over = False
obstacle_timer = 0  # Timer to control obstacle generation
score = 0  # Initialize the score

# Draw the player on the LED matrix
def draw_player():
    display.set_pixel(player_x, 4, 9)

# Draw the obstacles on the LED matrix
def draw_obstacles():
    for obstacle in obstacles:
        display.set_pixel(obstacle[0], obstacle[1], 9)

# Move the obstacles downwards
def move_obstacles():
    global game_over, score
    new_obstacles = []
    for obstacle in obstacles:
        x, y = obstacle
        if y == 4:  # Check for collision with player row
            if x == player_x:
                game_over = True
                return
            else:
                score += 1  # Increment score for dodged obstacle
        if y < 4:  # Keep obstacles above player row
            new_obstacles.append((x, y + 1))
    obstacles[:] = new_obstacles

# Generate a new obstacle
def generate_obstacle():
    obstacles.append((random.randint(0, 4), 0))

# Game loop
while not game_over:
    # Clear the display
    display.clear()

    # Draw the player, obstacles, and score
    draw_player()
    draw_obstacles()

    # Move the obstacles
    move_obstacles()

    # Generate new obstacles
    obstacle_timer += 1
    if obstacle_timer >= obstacle_speed:
        generate_obstacle()
        obstacle_timer = 0

    # Check for player input
    if button_a.was_pressed() and player_x > 0:
        player_x -= 1
    elif button_b.was_pressed() and player_x < 4:
        player_x += 1

    # Update the display
    sleep(100)

# Game over
display.scroll("Game Over!")
display.scroll("Score: " + str(score))  # Display the final score
