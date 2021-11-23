from skimage import io
from skimage import util
from skimage import transform
# from scipy.spatial.transform import Rotation as R
from skimage.transform import rotate
import os
import cv2
import random
from scipy import ndarray

# image processing library
import skimage as sk
from skimage.io import imread
# from scipy.misc import imread
# im = imread("farm.jpg")


def random_rotation(image_array: ndarray):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    angales_list = [90, 180, 270]
    random_degree = random.choice(angales_list)
    # if random_degree == 0:
    #     return rotate(image_array, random_degree)
    if random_degree == 90:
        return cv2.rotate(image_array, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif random_degree == 180:
        return cv2.rotate(image_array, cv2.ROTATE_180)
    elif random_degree == 270:
        return cv2.rotate(image_array, cv2.ROTATE_90_CLOCKWISE)


def random_noise(image_array: ndarray):
    # add random noise to the image
    return sk.util.random_noise(image_array)


def horizontal_flip(image_array: ndarray):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[:, ::-1]


# dictionary of the transformations we defined earlier
available_transformations = {
    'rotate': random_rotation,
    'noise': random_noise,
    # 'horizontal_flip': horizontal_flip
}

folder_path = '/home/rits/Documents/Assets/UAE_identity/Samples/'
num_files_desired = 200

# find all files paths from the folder
images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

num_generated_files = 0
while num_generated_files <= num_files_desired:
    print("-------num_generated_files----------")
    print(num_generated_files)
    print("-------num_generated_files----------")

    print("-------num_files_desired----------")
    print(num_files_desired)
    print("-------num_files_desired----------")

    # random image from the folder
    image_path = random.choice(images)
    print("--------image_path------------")
    print(image_path)
    print("--------image_path------------")
    # read image as an two dimensional array of pixels
    # image_to_transform = cv2.imread(image_path)
    # print(image_path)
    image_to_transform = imread(image_path)
    # random num of transformation to apply
    num_transformations_to_apply = random.randint(1, len(available_transformations))

    num_transformations = 0
    transformed_image = None
    while num_transformations <= num_transformations_to_apply:
        # random transformation to apply for a single image
        key = random.choice(list(available_transformations))
        transformed_image = available_transformations[key](image_to_transform)
        num_transformations += 1

    new_file_path = '%s/augmented_image_%s.png' % (folder_path, num_generated_files)

    # write image to the disk
    io.imsave(new_file_path, transformed_image)
    num_generated_files += 1
