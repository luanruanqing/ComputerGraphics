import tkinter as tk

# Đọc tọa độ các đỉnh của đa giác từ file dữ liệu
def read_polygon_data(filename):
    with open(filename, 'r') as file:
        polygon_data = [tuple(map(float, line.strip().split())) for line in file]
    return polygon_data

# Hàm xén đoạn thẳng bằng thuật toán chia nhị phân
def clip_line_binary(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    INSIDE = 0  # 0000
    LEFT = 1    # 0001
    RIGHT = 2   # 0010
    BOTTOM = 4  # 0100
    TOP = 8     # 1000

    def get_code(x, y):
        code = INSIDE
        if x < x_min:
            code |= LEFT
        elif x > x_max:
            code |= RIGHT
        if y < y_min:
            code |= BOTTOM
        elif y > y_max:
            code |= TOP
        return code

    code1 = get_code(x1, y1)
    code2 = get_code(x2, y2)

    while True:
        if not (code1 | code2):  # Đoạn thẳng nằm hoàn toàn trong vùng cắt
            return x1, y1, x2, y2
        if code1 & code2:  # Đoạn thẳng nằm hoàn toàn ngoài vùng cắt
            return None
        code_out = code1 if code1 else code2

        # Tìm điểm cắt
        if code_out & TOP:
            x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            y = y_max
        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            y = y_min
        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            x = x_max
        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            x = x_min

        if code_out == code1:
            x1, y1 = x, y
            code1 = get_code(x1, y1)
        else:
            x2, y2 = x, y
            code2 = get_code(x2, y2)

# Hàm vẽ đa giác và đoạn thẳng xén
def draw_polygon_and_clipped_line(canvas, polygon_data, x1, y1, x2, y2):
    # Vẽ đa giác
    canvas.create_polygon(polygon_data, outline='black', fill='lightgray')

    # Xén và vẽ đoạn thẳng
    x_min, y_min = min(x1, x2), min(y1, y2)
    x_max, y_max = max(x1, x2), max(y1, y2)
    clipped_line = clip_line_binary(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
    if clipped_line:
        x1, y1, x2, y2 = clipped_line
        canvas.create_line(x1, y1, x2, y2, fill='red')

# Xử lý sự kiện click chuột
def on_click(event):
    global click_count, x1, y1, x2, y2

    if click_count == 0:
        x1, y1 = event.x, event.y
        click_count = 1
    else:
        x2, y2 = event.x, event.y
        click_count = 0
        canvas.delete('all')
        draw_polygon_and_clipped_line(canvas, polygon_data, x1, y1, x2, y2)

# Main
if __name__ == "__main__":
    polygon_data = read_polygon_data("polygon_data.txt")

    root = tk.Tk()
    root.title("Clipping Algorithm - Binary")
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    click_count = 0
    x1, y1, x2, y2 = 0, 0, 0, 0

    draw_polygon_and_clipped_line(canvas, polygon_data, x1, y1, x2, y2)

    canvas.bind("<Button-1>", on_click)

    root.mainloop()
