import cv2
import numpy
import random


def tilt_shift(source):
    gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

    mask = numpy.zeros_like(gray)
    mask[gray.shape[0] // 3: 2 * gray.shape[0] // 3, :] = 255

    blurred = cv2.GaussianBlur(source, (7, 7), 5)

    output = numpy.where(mask[:, :, None] == 255, source, blurred)

    return output


def pixelation(source, noisy_width, noisy_height, square_size=1):
    output = numpy.copy(source)

    h, w, _ = source.shape

    x_start = int(w / 2 - noisy_width / 2)
    x_end = int(w / 2 + noisy_width / 2)
    y_start = int(h / 2 - noisy_height / 2)
    y_end = int(h / 2 + noisy_height / 2)

    for y in range(y_start, y_end, square_size):
        for x in range(x_start, x_end, square_size):
            intensity = random.randint(100, 255)
            output[y:(y + square_size), x:(x + square_size)] = intensity

    return output
