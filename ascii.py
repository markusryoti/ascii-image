import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt


def pixel_to_ascii(num):
    '''
    This is probably the most important piece of the puzzle. The image should probably be filtered somehow to reduce the number of varying pixels
    '''
    if num < 33:
        return chr(33)
    if num > 126:
        return chr(126)
    return chr(num)


def print_ascii_image(mat):
    '''
    Print image matrix to terminal, converting each pixel to ascii value
    '''
    n_rows, n_cols = mat.shape
    for i in range(n_rows):
        for j in range(n_cols):
            pixel_value = mat[i][j]
            print(pixel_to_ascii(pixel_value), end='')
        print()


def show_original_img(img):
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python ascii.py <filename>')
        quit()

    filename = sys.argv[1]

    orig_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    resized_img = cv2.resize(orig_img, [64, 64])

    print_ascii_image(resized_img)
    show_original_img(orig_img)
