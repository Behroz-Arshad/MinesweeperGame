from settings import *


def height_percent(percent):
    return (percent * HEIGHT) / 100


def width_percent(percent):
    return (percent * WIDTH) / 100

print(height_percent(25))
print(width_percent(25))
