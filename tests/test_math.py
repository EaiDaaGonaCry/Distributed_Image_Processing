import os
from server.image_math import save_filter_result, laplace_filter,gaussian_blur,sobbel_detection


def test_laplace_creates_file():
    input_file = "tests/res/test.jpg"
    output_file = "tests/res/laplace_out.jpg"

    if os.path.exists(output_file):
        os.remove(output_file)

    save_filter_result(input_file, laplace_filter, output_file)

    assert os.path.exists(output_file) == True


def test_gaussian_creates_file():
    input_file = "tests/res/test.jpg"
    output_file = "tests/res/gaussian_out.jpg"

    if os.path.exists(output_file):
        os.remove(output_file)

    save_filter_result(input_file, gaussian_blur, output_file)

    assert os.path.exists(output_file) == True


def test_sobel_creates_file():
    input_file = "tests/res/test.jpg"
    output_file = "tests/res/sobel_out.jpg"

    if os.path.exists(output_file):
        os.remove(output_file)

    save_filter_result(input_file, sobbel_detection, output_file)

    assert os.path.exists(output_file) == True