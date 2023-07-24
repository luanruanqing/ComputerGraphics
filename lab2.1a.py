import pygame
import sys

pygame.init()

# Kích thước cửa sổ đồ họa
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
POLYGON_COLOR = (255, 0, 0)

# Khởi tạo cửa sổ đồ họa
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cohen-Sutherland Clipping with Pygame")
screen.fill(BG_COLOR)

# Đọc đa giác từ tệp dữ liệu
def read_polygon_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        polygon_points = []
        for line in lines:
            x, y = map(int, line.strip().split())
            polygon_points.append((x, y))
    return polygon_points

# Vẽ đoạn thẳng
def draw_line(start, end):
    pygame.draw.line(screen, LINE_COLOR, start, end)

# Vẽ đa giác
def draw_polygon(polygon_points):
    pygame.draw.polygon(screen, POLYGON_COLOR, polygon_points)

# Thuật toán xén hình Cohen-Sutherland
def cohen_sutherland_clip(start, end, xmin, xmax, ymin, ymax):
    def get_code(p):
        code = 0
        if p[0] < xmin:
            code |= 1
        elif p[0] > xmax:
            code |= 2
        if p[1] < ymin:
            code |= 4
        elif p[1] > ymax:
            code |= 8
        return code

    code1 = get_code(start)
    code2 = get_code(end)

    while True:
        if not (code1 | code2):
            return start, end

        if code1 & code2:
            return None

        code_out = code1 if code1 else code2

        x, y = 0, 0
        if code_out & 1:
            x = xmin
            y = start[1] + (end[1] - start[1]) * (xmin - start[0]) / (end[0] - start[0])
        elif code_out & 2:
            x = xmax
            y = start[1] + (end[1] - start[1]) * (xmax - start[0]) / (end[0] - start[0])
        elif code_out & 4:
            y = ymin
            x = start[0] + (end[0] - start[0]) * (ymin - start[1]) / (end[1] - start[1])
        elif code_out & 8:
            y = ymax
            x = start[0] + (end[0] - start[0]) * (ymax - start[1]) / (end[1] - start[1])

        if code_out == code1:
            start = (int(x), int(y))
            code1 = get_code(start)
        else:
            end = (int(x), int(y))
            code2 = get_code(end)

# Chương trình chính
def main():
    clock = pygame.time.Clock()
    running = True
    drawing_line = False
    start_point = (0, 0)
    end_point = (0, 0)

    # Đọc đa giác từ tệp dữ liệu
    polygon_points = read_polygon_from_file("polygon_data.txt")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not drawing_line:
                    start_point = event.pos
                    drawing_line = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing_line:
                    end_point = event.pos
                    drawing_line = False

        screen.fill(BG_COLOR)

        # Vẽ đa giác
        draw_polygon(polygon_points)

        if drawing_line:
            # Vẽ đoạn thẳng và xén hình bằng thuật toán Cohen-Sutherland
            draw_line(start_point, end_point)
            clipped_start, clipped_end = cohen_sutherland_clip(
                start_point, end_point, 100, 700, 100, 500
            )
            if clipped_start and clipped_end:
                draw_line(clipped_start, clipped_end)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
