import pygame
import sys
import math

pygame.init()

# Kích thước cửa sổ đồ họa
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)

# Khởi tạo cửa sổ đồ họa
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Hyperbola with Pygame")
screen.fill(BG_COLOR)

def draw_hyperbola(center, a, b):
    if a == 0 or b == 0:
        return

    x = 0
    y = b
    a_sqr, b_sqr = a * a, b * b

    while x * b_sqr <= y * a_sqr:
        draw_hyperbola_points(center, x, y)

        x += 1
        y = int(b * math.sqrt(1 + (x * x) / a_sqr))

    x = a
    y = 0

    while y * a_sqr <= x * b_sqr:
        draw_hyperbola_points(center, x, y)

        y += 1
        x = int(a * math.sqrt(1 + (y * y) / b_sqr))

def draw_hyperbola_points(center, x, y):
    px, py = center
    pygame.draw.rect(screen, (0, 0, 0), (px + x, py + y, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px - x, py + y, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px + x, py - y, 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (px - x, py - y, 1, 1))

def main():
    clock = pygame.time.Clock()
    running = True
    drawing = False
    center = (0, 0)
    a, b = 0, 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not drawing:
                    center = event.pos
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP and drawing:
                x_diff = abs(event.pos[0] - center[0])
                y_diff = abs(event.pos[1] - center[1])
                a = x_diff
                b = y_diff

        screen.fill(BG_COLOR)

        if drawing:
            # Vẽ hyperbol bằng cách vẽ các điểm
            draw_hyperbola(center, a, b)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
