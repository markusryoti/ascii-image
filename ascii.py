import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

from html_renderer import HtmlRenderer

IMG_HEIGHT = 128
IMG_WIDTH = 128


def pixel_to_ascii(num):
    '''
    Converts pixel value (0-255) to ascii character value (33-126).
    '''
    return chr(get_scaled_value(num))


def get_scaled_value(num):
    '''
    Converts pixel value (0-255) to valid ascii value (33-126).
    '''
    return int((num / 255) * (126 - 33) + 33)


def img_to_ascii(mat):
    '''
    Convert numpy array of pixel values to character array with character values
    '''
    n_rows, n_cols = mat.shape
    new_img = np.chararray((n_rows, n_cols))
    for i in range(n_rows):
        for j in range(n_cols):
            new_img[i][j] = pixel_to_ascii(mat[i][j])

    return new_img


def blur_img(img):
    '''
    The input image will most likely have to much details resulting the ascii image to 
    have more varying characters than needed. Blurring will remove some of those details.
    '''
    kernel_size = (3, 3)
    return cv2.blur(img, kernel_size)


def resize_img(img):
    return cv2.resize(img, [IMG_HEIGHT, IMG_WIDTH])


def preprocess_image(img):
    '''
    The image is preprocessed before converting it to ascii character representation.
    '''
    img = resize_img(img)
    img = blur_img(img)

    return img


def show_img(img):
    plt.imshow(img)
    plt.show()


def show_compare(orig, edited):
    '''
    Prints both the original and pre-processed image.
    '''
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

    preprocessed_image = preprocess_image(orig_img)

    ascii_img = img_to_ascii(preprocessed_image)
    html_renderer = HtmlRenderer()
    html_renderer.render(ascii_img)

    show_compare(orig_img, preprocessed_image)
