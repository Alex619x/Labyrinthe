import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mon Premier Jeu avec Pygame")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 20, 60)
green = (0, 255, 0)

# Function to draw a maze on a given surface
def draw_maze(surface):
    maze = [
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    cell_width = width // len(maze[0])
    cell_height = height // len(maze)

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            cell_color = black if maze[row][col] == 1 else white
            pygame.draw.rect(surface, cell_color, (col * cell_width, row * cell_height, cell_width, cell_height))

    return maze

# Function to draw the character on a given surface
def draw_character(surface, character_pos):
    character_color = red
    cell_width = width // len(maze[0])
    cell_height = height // len(maze)
    character_rect = pygame.Rect(character_pos[0] * cell_width, character_pos[1] * cell_height, cell_width, cell_height)
    pygame.draw.rect(surface, character_color, character_rect)

# Function to draw the finish line on a given surface
def draw_finish(surface, finish_pos):
    finish_color = white
    cell_width = width // len(maze[0])
    cell_height = height // len(maze)
    finish_rect = pygame.Rect(finish_pos[0] * cell_width, finish_pos[1] * cell_height, cell_width, cell_height)
    pygame.draw.rect(surface, finish_color, finish_rect)

# Function to handle another window
def open_another_window(maze):
    another_window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Labyrinthe")

    character_pos = [1, 1]  # Initial position of the character
    finish_pos = [len(maze[0]) - 2, len(maze) - 2]  # Position of the finish line
    draw_maze(another_window)
    draw_character(another_window, character_pos)
    draw_finish(another_window, finish_pos)
    pygame.display.flip()

    # Keep the new window open until it is manually closed or the character reaches the finish line
    while character_pos != finish_pos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Handle character movement
                if event.key == pygame.K_LEFT and maze[character_pos[1]][character_pos[0] - 1] == 0:
                    character_pos[0] -= 1
                elif event.key == pygame.K_RIGHT and maze[character_pos[1]][character_pos[0] + 1] == 0:
                    character_pos[0] += 1
                elif event.key == pygame.K_UP and maze[character_pos[1] - 1][character_pos[0]] == 0:
                    character_pos[1] -= 1
                elif event.key == pygame.K_DOWN and maze[character_pos[1] + 1][character_pos[0]] == 0:
                    character_pos[1] += 1

                # Redraw the maze, character, and finish line after movement
                another_window.fill(white)
                draw_maze(another_window)
                draw_character(another_window, character_pos)
                draw_finish(another_window, finish_pos)
                pygame.display.flip()

    # Display congratulatory message when the character reaches the finish line
    congratulation_window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Partie Terminée - Félicitations")
    congratulation_font = pygame.font.Font(None, 50)
    congratulation_text = congratulation_font.render("Partie Terminée - Félicitations!", True, red)
    congratulation_text_rect = congratulation_text.get_rect(center=(width // 2, height // 2))
    congratulation_window.blit(congratulation_text, congratulation_text_rect)
    pygame.display.flip()

    # Keep the congratulation window open until it is manually closed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Set up the button
button_rect = pygame.Rect(300, 250, 200, 100)
button_color = black

# Set up font
font = pygame.font.Font(None, 40)
text = font.render("Démarrer", True, white)
text_rect = text.get_rect(center=button_rect.center)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Start Button Clicked!")
                maze = draw_maze(screen)
                open_another_window(maze)

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
