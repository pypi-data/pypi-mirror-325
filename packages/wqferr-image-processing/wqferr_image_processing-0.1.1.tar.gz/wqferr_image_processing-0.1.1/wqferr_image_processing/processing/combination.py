import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Images must have the same shape."
    gray_img1 = rgb2gray(image1)
    gray_img2 = rgb2gray(image2)
    score, difference_img = structural_similarity(gray_img1, gray_img2, full=True)
    print(f"Image similarity: {score:.3f}")
    img_min, img_max = np.min(difference_img), np.max(difference_img)
    normalized_diff_img = (difference_img - img_min) / (img_max - img_min)
    return normalized_diff_img


def transfer_histogram(base, hist_source):
    return match_histograms(base, hist_source, multichannel=True)
