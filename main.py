import pygame
import heapq

pygame.init()

# =========================
# WINDOW SETTINGS
# =========================
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Warehouse Robot")

# =========================
# COLORS
# =========================
WHITE = (255, 255, 255)
LIGHT_GRAY = (235, 235, 235)
GRAY = (180, 180, 180)
DARK = (60, 60, 60)
GREEN = (60, 180, 75)
RED = (220, 60, 60)
BLUE = (50, 100, 220)
ORANGE = (240, 150, 40)
BLACK = (20, 20, 20)

# =========================
# GRID SETTINGS
# =========================
ROWS = 12
COLS = 16
CELL_SIZE = 40

GRID_X = 30
GRID_Y = 100

start = (1, 1)
goal = (10, 14)

obstacles = {
    (2, 3), (2, 4), (2, 5),
    (3, 5), (4, 5), (5, 5),
    (5, 6), (5, 7), (5, 8),
    (7, 10), (8, 10), (9, 10),
    (8, 11), (8, 12), (8, 13)
}

# =========================
# FONTS
# =========================
title_font = pygame.font.SysFont("Arial", 28, bold=True)
font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 16)

# =========================
# A* HEURISTIC
# =========================
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# =========================
# GET NEIGHBORS
# =========================
def get_neighbors(node):
    row, col = node

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if (
            0 <= new_row < ROWS
            and 0 <= new_col < COLS
            and (new_row, new_col) not in obstacles
        ):
            neighbors.append((new_row, new_col))

    return neighbors


# =========================
# A* SEARCH
# =========================
def a_star(start, goal):

    open_set = []

    heapq.heappush(
        open_set,
        (heuristic(start, goal), 0, start)
    )

    came_from = {}

    g_score = {
        start: 0
    }

    closed_set = set()

    nodes_explored = 0

    while open_set:

        _, current_g, current = heapq.heappop(open_set)

        # Skip nodes already processed
        if current in closed_set:
            continue

        closed_set.add(current)

        # Count explored node
        nodes_explored += 1

        # Goal reached
        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            path.reverse()

            return path, nodes_explored

        # Explore neighbors
        for neighbor in get_neighbors(current):

            tentative_g = g_score[current] + 1

            if (
                neighbor not in g_score
                or tentative_g < g_score[neighbor]
            ):

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = (
                    tentative_g
                    + heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_set,
                    (f_score, tentative_g, neighbor)
                )

    return [], nodes_explored


# =========================
# DRAW GRID
# =========================
def draw_grid(path, robot_position):

    screen.fill(WHITE)

    # Title
    title = title_font.render(
        "Smart Warehouse Robot",
        True,
        BLACK
    )

    screen.blit(title, (30, 25))

    # Algorithm information
    algorithm_text = font.render(
        "Algorithm: A*",
        True,
        DARK
    )

    screen.blit(
        algorithm_text,
        (30, 65)
    )

    # Grid
    for row in range(ROWS):

        for col in range(COLS):

            x = GRID_X + col * CELL_SIZE
            y = GRID_Y + row * CELL_SIZE

            rect = pygame.Rect(
                x,
                y,
                CELL_SIZE,
                CELL_SIZE
            )

            # Normal cell
            pygame.draw.rect(
                screen,
                LIGHT_GRAY,
                rect
            )

            # Obstacles
            if (row, col) in obstacles:

                pygame.draw.rect(
                    screen,
                    DARK,
                    rect
                )

            # Path
            elif (row, col) in path:

                pygame.draw.rect(
                    screen,
                    BLUE,
                    rect
                )

            # Start
            if (row, col) == start:

                pygame.draw.rect(
                    screen,
                    GREEN,
                    rect
                )

            # Goal
            if (row, col) == goal:

                pygame.draw.rect(
                    screen,
                    RED,
                    rect
                )

            # Grid border
            pygame.draw.rect(
                screen,
                GRAY,
                rect,
                1
            )

    # Robot
    robot_x = (
        GRID_X
        + robot_position[1] * CELL_SIZE
        + CELL_SIZE // 2
    )

    robot_y = (
        GRID_Y
        + robot_position[0] * CELL_SIZE
        + CELL_SIZE // 2
    )

    pygame.draw.circle(
        screen,
        ORANGE,
        (robot_x, robot_y),
        14
    )

    # =========================
    # INFORMATION PANEL
    # =========================

    panel_x = 700
    panel_y = 110

    info1 = font.render(
        "Path Length: " + str(max(len(path) - 1, 0)) + " cells",
        True,
        DARK
    )

    info2 = font.render(
        "Nodes Explored: " + str(nodes_explored),
        True,
        DARK
    )

    info3 = font.render(
        "Robot: Autonomous",
        True,
        DARK
    )

    screen.blit(info1, (panel_x, panel_y))
    screen.blit(info2, (panel_x, panel_y + 35))
    screen.blit(info3, (panel_x, panel_y + 70))

    # =========================
    # STATUS
    # =========================

    status_text = font.render(
        status,
        True,
        BLACK
    )

    screen.blit(
        status_text,
        (700, 260)
    )

    # =========================
    # BUTTONS
    # =========================

    start_button = pygame.Rect(
        700,
        330,
        220,
        50
    )

    reset_button = pygame.Rect(
        700,
        400,
        220,
        50
    )

    pygame.draw.rect(
        screen,
        GREEN,
        start_button,
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        RED,
        reset_button,
        border_radius=8
    )

    start_text = font.render(
        "START ROBOT",
        True,
        WHITE
    )

    reset_text = font.render(
        "RESET",
        True,
        WHITE
    )

    screen.blit(
        start_text,
        (start_button.x + 45, start_button.y + 12)
    )

    screen.blit(
        reset_text,
        (reset_button.x + 75, reset_button.y + 12)
    )

    # =========================
    # LEGEND
    # =========================

    legend_y = 490

    legend_items = [
        (GREEN, "Start"),
        (RED, "Goal"),
        (DARK, "Obstacle"),
        (BLUE, "A* Path"),
        (ORANGE, "Robot")
    ]

    for color, text in legend_items:

        pygame.draw.rect(
            screen,
            color,
            (700, legend_y, 20, 20)
        )

        label = small_font.render(
            text,
            True,
            DARK
        )

        screen.blit(
            label,
            (730, legend_y)
        )

        legend_y += 30

    pygame.display.flip()


# =========================
# INITIAL A* SEARCH
# =========================
path, nodes_explored = a_star(start, goal)

robot_position = start

robot_index = 0

robot_running = False

status = "Ready - Press START ROBOT"

clock = pygame.time.Clock()

last_move_time = pygame.time.get_ticks()

running = True


# =========================
# MAIN LOOP
# =========================
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Start button
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            start_button = pygame.Rect(
                700,
                330,
                220,
                50
            )

            reset_button = pygame.Rect(
                700,
                400,
                220,
                50
            )

            # START
            if start_button.collidepoint(mouse_pos):

                robot_running = True
                status = "Robot Moving..."

            # RESET
            elif reset_button.collidepoint(mouse_pos):

                robot_position = start
                robot_index = 0

                robot_running = False

                status = "Ready - Press START ROBOT"

    # =========================
    # ROBOT MOVEMENT
    # =========================

    if robot_running:

        current_time = pygame.time.get_ticks()

        if current_time - last_move_time >= 250:

            if robot_index < len(path) - 1:

                robot_index += 1

                robot_position = path[robot_index]

                last_move_time = current_time

            else:

                robot_running = False

                status = "Destination Reached!"

    draw_grid(path, robot_position)

    clock.tick(60)

pygame.quit()