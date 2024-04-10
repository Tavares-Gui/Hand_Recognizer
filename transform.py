import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Transformada de Fourier
def fft(img):
    img = np.fft.fft2(img)
    img = np.fft.fftshift(img)
    return img


# Inversa (retorna para imagem original)
def ifft(fimg):
    fimg = np.fft.ifftshift(fimg)
    fimg = np.fft.ifft2(fimg)
    return fimg


# Obtém a magnitude da imagem
def mag(img):
    absvalue = np.abs(img)
    magnitude = 20 * np.log(absvalue)
    return magnitude


# Normaliza a imagem entre 0 e 255
def norm(img):
    img = cv.normalize(img, None, 0, 255, cv.NORM_MINMAX)


# Melhor para ver imagens da transformada e imagens pequenas em geral.
def show(img):
    plt.imshow(img, cmap="gray")
    plt.show()
    return img


ds_path = r"C:/Users/disrct/Desktop/desafio3/datasets/binary/ds"

ds_directory = r"C:/Users/disrct/Desktop/desafio3/datasets/binaryFourier/ds"

os.chdir(ds_directory)


def fourier(ds_path):
    images = []
    for subdir, dirs, files in os.walk(ds_path):
        for file in files:
            if file.endswith(".png"):
                img_path = os.path.join(subdir, file)
                img = cv.imread(img_path, cv.COLOR_GRAY2BGRA)
                images.append(img)
    return images


def binary(ds_path):
    images = []
    for subdir, dirs, files in os.walk(ds_path):
        for file in files:
            if file.endswith(".png"):
                img_path = os.path.join(subdir, file)
                img = cv.imread(img_path)
                img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                threshold, img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
                images.append(img)
    return images

for j in range(6):
    directories = [f"{ds_path}/{j}/"]
    images = []
    for dir in directories:
        images.extend(fourier(dir))

    for i, img in enumerate(images):
        img = fft(img)
        img = mag(img)
        cv.imwrite(os.path.join(f"{ds_directory}/{j}/", f"{i}.png"), img)
