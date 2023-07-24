import pygame
import sys

# Hàm tô màu theo đường biên
def boundary_fill(screen, x, y, fill_color, boundary_color, width, height):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if 0 <= x < width and 0 <= y < height:
            current_color = screen.get_at((x, y))

            if current_color != boundary_color and current_color != fill_color:
                screen.set_at((x, y), fill_color)

                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))

# Hàm đọc đa giác từ file dữ liệu
def read_polygon_from_file(filename):
    polygon = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            polygon.append((x, y))
    return polygon

def main():
    # Kích thước cửa sổ
    width, height = 800, 600
    # Màu sắc
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    
    # Đường dẫn đến file chứa đa giác
    polygon_filename = 'polygon_data.txt'
    
    # Khởi tạo Pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Boundary Fill Algorithm')
    screen.fill(white)
    
    # Đọc đa giác từ file
    polygon_points = read_polygon_from_file(polygon_filename)
    
    # Vẽ đa giác lên màn hình
    pygame.draw.polygon(screen, black, polygon_points, 1)
    pygame.display.flip()
    
    # Chờ người dùng nhấn chuột trái để chọn điểm bên trong đa giác
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                # Tô màu theo đường biên bằng hàm đã định nghĩa
                boundary_fill(screen, x, y, blue, black, x + 10, y + 10)
                pygame.display.flip()

if __name__ == '__main__':
    main()
