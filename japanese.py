WHITE_BG = "\033[48;5;15m"
RED_BG = "\033[48;5;1m"
RESET = "\033[0m" 

# flag size
width = 45
height = 30

circle_center_x = width // 2
circle_center_y = height // 2
circle_radius = min(width, height) // 4

for y in range(height):
    for x in range(width):
        distance_from_center = ((x - circle_center_x) ** 2 + (y - circle_center_y) ** 2) ** 0.5
        if distance_from_center <= circle_radius:
            print(RED_BG + "  ", end="")  # two spaces to keep aspect ratio
        else: 
            print(WHITE_BG + "  ", end="")  # two spaces to keep aspect ratio
    print(RESET)