from pathlib import Path
from matplotlib.image import imread, imsave
import random


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:

    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = rgb2gray(imread(path)).tolist()

    def save_img(self):
        """
        Do not change the below implementation
        """
        new_path = self.path.with_name(self.path.stem + '_filtered' + self.path.suffix)
        imsave(new_path, self.data, cmap='gray')
        return new_path

    def blur(self, blur_level=16):

        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2

        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)

        self.data = result

    def contour(self):
        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j-1] - row[j]))

            self.data[i] = res

# concat function
    def concat(self, other_img, direction='horizontal'):
        # if direction == 'horizontal':
        #     self.concat_horizontal(other_img)
        # elif direction == 'vertical':
        #     self.concat_vertical(other_img)
        # else:
        #     raise RuntimeError("Invalid direction for concatenation. Must be 'horizontal' or 'vertical'.")
        if direction == 'horizontal':
            if len(self.data) != len(other_img.data):
                raise RuntimeError("Images must have the same height for horizontal concatenation")
            self.data = [row1 + row2 for row1, row2 in zip(self.data, other_img.data)]
        elif direction == 'vertical':
            if len(self.data[0]) != len(other_img.data[0]):
                raise RuntimeError("Images must have the same width for vertical concatenation")
            self.data += other_img.data
        else:
            raise RuntimeError("Invalid direction for concatenation. Must be 'horizontal' or 'vertical'.")

# # Helper function for concat function. Concatenate the other_img to the right of the current image
#     def concat_horizontal(self, other_img):
#         if len(self.data) != len(other_img.data):
#             raise RuntimeError("Images must have the same height for horizontal concatenation")
#         #use zip to concatenate the rows of the two images
#         self.data = [row1 + row2 for row1, row2 in zip(self.data, other_img.data)]
#
#     # Helper function for concat function. Concatenate the other_img to the bottom of the current image
#     def concat_vertical(self, other_img):
#        if len(self.data[0]) != len(other_img.data[0]):
#               raise RuntimeError("Images must have the same width for vertical concatenation")
#          #use the + operator to concatenate the two images
#          self.data += other_img.data

    def rotate(self):
        if not self.data:
            raise RuntimeError("Image data is empty")
        self.data = [list(row) for row in zip(*self.data[::-1])]

    def salt_n_pepper(self, salt_prob=0.05, pepper_prob=0.05):
        height = len(self.data)
        width = len(self.data[0])
        for i in range(height):
            for j in range(width):
                rand = random.random()
                if rand < salt_prob:
                    self.data[i][j] = 255
                elif rand < salt_prob + pepper_prob:
                    self.data[i][j] = 0

    def segment(self):
        if not self.data:
            raise RuntimeError("Image data is empty")
        total_pixels = sum(sum(row) for row in self.data)
        average = total_pixels // (len(self.data) * len(self.data[0]))
        for i, row in enumerate(self.data):
            self.data[i] = [0 if pixel < average else 255 for pixel in row]

