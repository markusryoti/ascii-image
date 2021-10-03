import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

from html_renderer import HtmlRenderer

IMG_HEIGHT = 128
IMG_WIDTH = 128


def pixel_to_ascii(num):
    '''
    This is probably the most important piece of the puzzle. The image should probably be filtered somehow to reduce the number of varying pixels.
    '''
    return chr(get_scaled_value(num))


def get_scaled_value(num):
    '''
    Converts pixel value (0-255) to valid ascii value (33-126).
    '''
    return int((num / 255) * (126 - 33) + 33)


def print_ascii_image(mat):
    '''
    Print image matrix to terminal, converting each pixel to ascii value.
    '''
    n_rows, n_cols = mat.shape
    for i in range(n_rows):
        for j in range(n_cols):
            pixel_value = mat[i][j]
            print(pixel_to_ascii(pixel_value), end='')
        print()


def img_to_ascii(mat):
    n_rows, n_cols = mat.shape
    new_img = np.chararray((n_rows, n_cols))
    for i in range(n_rows):
        for j in range(n_cols):
            new_img[i][j] = pixel_to_ascii(mat[i][j])

    return new_img


def blur_img(img):
    kernel_size = (5, 5)
    return cv2.blur(img, kernel_size)


def resize_img(img):
    return cv2.resize(img, [IMG_HEIGHT, IMG_WIDTH])


def show_img(img):
    plt.imshow(img)
    plt.show()


def show_compare(orig, edited):
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(orig)
    ax[1].imshow(edited)
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python ascii.py <filename>')
        quit()

    filename = sys.argv[1]

    orig_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    blurred_img = blur_img(orig_img)

    resized = resize_img(blurred_img)
    ascii_img = img_to_ascii(resized)

    show_compare(orig_img, resized)

    html_renderer = HtmlRenderer()
    html_renderer.render(ascii_img)
