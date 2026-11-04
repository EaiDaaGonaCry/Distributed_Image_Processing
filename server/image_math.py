from PIL import Image
from scipy.signal import convolve2d
import numpy as np

def save_filter_result(image_path: str, filter_f, output_path: str):
    img = Image.open(image_path).convert('L')
    img_matrix = np.array(img)

    res_matrix = filter_f(img_matrix)

    res_img = Image.fromarray(res_matrix)
    res_img.save(output_path)

def laplace_filter(img_matrix: np.ndarray) -> np.ndarray:
    laplace_kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])

    proc_matrix = convolve2d(img_matrix, laplace_kernel, mode='same', boundary='symm')
    proc_matrix = np.clip(proc_matrix, 0, 255)

    return proc_matrix.astype('uint8')

def sobbel_detection(img_matrix: np.ndarray) -> np.ndarray:
    sobel_x = np.array([
        [-1,0,1],
        [-2,0,2],
        [-1,0,1]
    ])

    sobel_y = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])

    grad_x = convolve2d(img_matrix, sobel_x,mode='same',boundary='symm')
    grad_y = convolve2d(img_matrix, sobel_y, mode='same', boundary='symm')

    proc_matrix = np.sqrt(grad_x**2 + grad_y**2)
    proc_matrix = np.clip(proc_matrix,0,255)

    return proc_matrix.astype('uint8')

def gaussian_blur(img_matrix: np.ndarray) -> np.ndarray:
    gaussian_kernel = np.array([
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ])

    gaussian_kernel = gaussian_kernel / 256.0

    proc_matrix = convolve2d(img_matrix,gaussian_kernel,mode='same',boundary='symm')
    proc_matrix = np.clip(proc_matrix,0,255)

    return  proc_matrix.astype('uint8')


