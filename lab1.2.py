import pygame
import sys

pygame.init()

# Kích thước cửa sổ đồ họa
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)

# Khởi tạo cửa sổ đồ họa
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham & Midpoint Circle Drawing Algorithms")
screen.fill(BG_COLOR)

def draw_circle_bresenham(center, radius):
    x, y = radius, 0
    p = 1 - radius
    while x >= y:
        draw_circle_points(center, x, y)
        y += 1
        if p <= 0:
            p += 2 * y + 1
        else:
            x -= 1
            p += 2 * (y - x) + 1

def draw_circle_midpoint(center, radius):
    x, y = 0, radius
    p = 1 - radius
    while x <= y:
        draw_circle_points(center, x, y)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

def draw_circle_points(center, x, y):
    px, py = center
    pygame.draw.rect(screen, (0, 0, 0), (px + x, py + y, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px - x, py + y, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px + x, py - y, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px - x, py - y, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px + y, py + x, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px - y, py + x, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px + y, py - x, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px - y, py - x, 1, 1))

def main():
    clock = pygame.time.Clock()
    running = True
    drawing = False
    center = (0, 0)
    radius = 0
    start_pos = (0, 0)
    end_pos = (0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not drawing:
                    start_pos = event.pos
                    center = start_pos
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    end_pos = event.pos
                    radius = max(abs(end_pos[0] - center[0]), abs(end_pos[1] - center[1]))
                    drawing = False
        screen.fill(BG_COLOR)

        if not drawing:
            # Vẽ đường tròn bằng thuật toán Bresenham
            draw_circle_bresenham(center, radius)

            # Vẽ đường tròn bằng thuật toán Midpoint
            # draw_circle_midpoint(center, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
