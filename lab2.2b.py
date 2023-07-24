import pygame
import sys

# Các màu cơ bản
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tô màu theo dòng quét")

def fill_polygon(surface, points, color):
    if len(points) < 3:
        raise ValueError("A polygon must have at least 3 points.")

    # Tìm cạnh trái và cạnh phải của đa giác
    left_edge = min(points, key=lambda p: p[0])[0]
    right_edge = max(points, key=lambda p: p[0])[0]

    # Khởi tạo danh sách chứa các cạnh của đa giác
    min_y, max_y = min(points, key=lambda p: p[1])[1], max(points, key=lambda p: p[1])[1]
    edges = [[] for _ in range(max_y + 1)]

    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]

        if y1 != y2:
            m = (x2 - x1) / (y2 - y1)
            min_y, max_y = sorted([y1, y2])
            edges[min_y].append((max_y, x1, m))

    active_edges = []
    for y in range(len(edges)):
        active_edges.extend(edges[y])
        active_edges = sorted(active_edges, key=lambda x: x[1])

        for i in range(0, len(active_edges), 2):
            if i + 1 < len(active_edges):
                x_start = int(active_edges[i][1])
                x_end = int(active_edges[i + 1][1])

                pygame.draw.line(surface, color, (x_start, y), (x_end, y))

        # Xóa các cạnh đã qua y hiện tại khỏi danh sách active_edges
        active_edges = [edge for edge in active_edges if edge[0] > y]


def main():
    points = []
    with open('points.txt', 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split(','))
            points.append((x, y))

    # Vòng lặp chính của game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Tô màu khi nhấp chuột trái
                if event.button == 1:
                    fill_polygon(screen, points, GREEN)
                # Xóa màu khi nhấp chuột phải
                elif event.button == 3:
                    fill_polygon(screen, points, WHITE)

        pygame.display.flip()

if __name__ == "__main__":
    main()
