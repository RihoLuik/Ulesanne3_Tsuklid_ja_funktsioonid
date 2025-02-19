import pygame

# Initialise pygame
pygame.init()

# Screen setup & Window name
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Ülesanne 3 - Ruudud :D")

# Background colour
LIME = (50, 205, 50)

# User input for square size, rows and column sizes
def get_int_input(prompt, default):
    try:
        return max(1, int(input(prompt)))  # Ensure value is at least 1
    except ValueError:
        print(f"Invalid input! Using default value: {default}")
        return default

# User input for square colour
def get_rgb_input():
    while True:
        user_input = input("Enter grid line color as R,G,B (e.g., 255,0,255 for magenta): ").strip()
        try:
            r, g, b = map(int, user_input.split(",")) # Convert input to three integers
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return (r, g, b)
        except ValueError:
            pass
        print("Invalid color! Please enter three numbers between 0-255, separated by commas.")

square_size = get_int_input("Enter square size (e.g., 40): ", 40)
rows = get_int_input("Enter number of rows: ", screen_size[1] // square_size)
cols = get_int_input("Enter number of columns: ", screen_size[0] // square_size)
line_color = get_rgb_input()

# Function to draw the grid
def draw_grid(surface, square_size, rows, cols, line_color):
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(surface, line_color, rect, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(LIME) # Background color
    draw_grid(screen, square_size, rows, cols, line_color)
    pygame.display.flip()

pygame.quit()