from PIL import Image, ImageOps
import matplotlib.pyplot as plt

image = Image.new('RGB', (50, 50))

def Bresenham(x1, y1, x2, y2):
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    error = 0
    diff = 1


    if (x1 - x2 > 0):
        x1, x2 = x2, x1
        y1, y2 = y2, y1


    if (y1 - y2 > 0):
        diff = -1


    if (delta_x >= delta_y):
        y_i = y1
        for x in range(x1, x2 + 1):
            image.putpixel((x, y_i), (255, 255, 255))
            error = error + 2 * delta_y
            if error >= delta_x:
                y_i += diff
                error -= 2 * delta_x

    elif (delta_x < delta_y):

        if (diff == -1):
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        x_i = x1
        for y in range(y1, y2 + 1):
            image.putpixel((x_i, y), (255, 255, 255))
            error = error + 2 * delta_x
            if error >= delta_y:
                x_i += diff
                error -= 2 * delta_y


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
Bresenham(x1, y1, x2, y2)


image = ImageOps.flip(image)
plt.imshow(image)
plt.show()