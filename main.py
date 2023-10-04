from PIL import Image, ImageOps
import matplotlib.pyplot as plt


def Fs(y):
    return 4 * y + 6


def Fd(x, y):
    return 4 * x + 4 * y + 10


def Bresenham_circle(rad):
    x0, y0 = -rad, 0
    F = 1 - 2 * rad

    while True:
        if (x0 == 0): break

        image.putpixel((x0 + rad, y0 + rad), (255, 255, 255))
        image.putpixel((x0 + rad, -y0 + rad), (255, 255, 255))
        image.putpixel((-x0 + rad, y0 + rad), (255, 255, 255))
        image.putpixel((-x0 + rad, -y0 + rad), (255, 255, 255))


        image.putpixel((y0 + rad, x0 + rad), (255, 255, 255))
        image.putpixel((-y0 + rad, x0 + rad), (255, 255, 255))
        image.putpixel((y0 + rad, -x0 + rad), (255, 255, 255))
        image.putpixel((-y0 + rad, -x0 + rad), (255, 255, 255))


        if (abs(x0) <= abs(y0)): break


        if (F < 0):
            F += Fs(y0)

        else:
            x0 += 1
            F += Fd(x0, y0)
        y0 += 1

    return


rad = int(input("r: "))

image = Image.new('RGB', (2 * rad+1, 2 * rad+1))


Bresenham_circle(rad)

image = ImageOps.flip(image)
plt.imshow(image)
plt.show()