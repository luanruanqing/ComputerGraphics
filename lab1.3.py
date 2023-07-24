import pygame
import sys

pygame.init()

# Kích thước cửa sổ đồ họa
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)

# Khởi tạo cửa sổ đồ họa
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Ellipse with Pygame")
screen.fill(BG_COLOR)

def main():
    clock = pygame.time.Clock()
    running = True
    drawing = False
    center = (0, 0)
    radius_a, radius_b = 0, 0

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
                radius_a = x_diff
                radius_b = y_diff

        screen.fill(BG_COLOR)

        if drawing:
            # Vẽ ellipse bằng Pygame
            pygame.draw.ellipse(screen, (0, 0, 0), (center[0] - radius_a, center[1] - radius_b, 2 * radius_a, 2 * radius_b), 1)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
