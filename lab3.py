import matplotlib.pyplot as plt
import math

# Hàm thực hiện phép tịnh tiến
def translation(x, y, x0, y0):
    return x + x0, y + y0

# Hàm thực hiện phép tỉ lệ
def scale(x, y, x0, y0, sx, sy):
    return (x - x0) * sx + x0, (y - y0) * sy + y0

# Hàm thực hiện phép quay
def rotate(x, y, x0, y0, theta):
    dx, dy = x - x0, y - y0
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    x_new = x0 + dx * cos_theta - dy * sin_theta
    y_new = y0 + dx * sin_theta + dy * cos_theta
    return x_new, y_new

# Hàm thực hiện phép đối xứng
def reflection(x, y, a, b):
    x_new = (x + a * (y - b)) / (1 + a**2)
    y_new = b + a * (x - x_new)
    return x_new, y_new

# Điểm ban đầu
x_points = [1, 2, 3, 4, 5]
y_points = [2, 3, 1, 5, 5]

# Điểm tâm tịnh tiến, tỉ lệ, quay và điểm tâm đối xứng
x0, y0 = 2, 2
sx, sy = 1.5, 0.5
theta = math.pi / 4
a, b = 1, 3

# Thực hiện các phép biến đổi
translated_points = [translation(x, y, x0, y0) for x, y in zip(x_points, y_points)]
scaled_points = [scale(x, y, x0, y0, sx, sy) for x, y in zip(x_points, y_points)]
rotated_points = [rotate(x, y, x0, y0, theta) for x, y in zip(x_points, y_points)]
reflected_points = [reflection(x, y, a, b) for x, y in zip(x_points, y_points)]

# Vẽ các điểm ban đầu
plt.scatter(x_points, y_points, label='Original Points', color='blue')

# Vẽ các điểm sau khi biến đổi
translated_x, translated_y = zip(*translated_points)
plt.scatter(translated_x, translated_y, label='Translated Points', color='green')

scaled_x, scaled_y = zip(*scaled_points)
plt.scatter(scaled_x, scaled_y, label='Scaled Points', color='orange')

rotated_x, rotated_y = zip(*rotated_points)
plt.scatter(rotated_x, rotated_y, label='Rotated Points', color='red')

reflected_x, reflected_y = zip(*reflected_points)
plt.scatter(reflected_x, reflected_y, label='Reflected Points', color='purple')

# Thiết lập đồ thị
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Transformations')
plt.legend()
plt.grid(True)

# Hiển thị đồ thị
plt.show()
