import cv2
import numpy


def tilt_shift(source):
    gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

    mask = numpy.zeros_like(gray)
    mask[gray.shape[0] // 3: 2 * gray.shape[0] // 3, :] = 255

    blurred = cv2.GaussianBlur(source, (7, 7), 5)

    output = numpy.where(mask[:, :, None] == 255, source, blurred)

    return output
