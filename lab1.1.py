import pygame
import sys

pygame.init()

# Kích thước cửa sổ đồ họa
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)

# Khởi tạo cửa sổ đồ họa
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham & Midpoint Line Drawing Algorithms")
screen.fill(BG_COLOR)

def draw_line_bresenham(start, end):
    x0, y0 = start
    x1, y1 = end
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while x0 != x1 or y0 != y1:
        draw_line_points((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def draw_line_midpoint(start, end):
    x0, y0 = start
    x1, y1 = end
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            draw_line_points((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            draw_line_points((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

def draw_line_points(point):
    pygame.draw.rect(screen, (0, 0, 0), (point[0], point[1], 1, 1))

def main():
    clock = pygame.time.Clock()
    running = True
    drawing = False
    start_pos = (0, 0)
    end_pos = (0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not drawing:
                    start_pos = event.pos
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    end_pos = event.pos
                    drawing = False

        screen.fill(BG_COLOR)

        if not drawing and start_pos != end_pos:
            # Vẽ đoạn thẳng bằng thuật toán Bresenham
            draw_line_bresenham(start_pos, end_pos)

            # Vẽ đoạn thẳng bằng thuật toán Midpoint
            # draw_line_midpoint(start_pos, end_pos)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
