# Author: Justin Huang
# GitHub username: huangjus
# Date: 4/25/23
# Description: This code contains a Box class representing a 3D box with methods for calculating its volume and
# accessing its dimensions. It also includes a box_sort function that sorts a list of Box objects in place,
# in descending order based on their volume using the insertion sort algorithm.

class Box:
    """
    A class representing a 3D box with length, width, and height.
    """

    def __init__(self, length, width, height):
        """
        Initializes a Box object with given length, width, and height.
        """
        self.__length = length
        self.__width = width
        self.__height = height

    def volume(self):
        """
        Calculates and returns the volume of the box.
        """
        return self.__length * self.__width * self.__height

    def get_length(self):
        """
        Returns the length of the box.
        """
        return self.__length

    def get_width(self):
        """
        Returns the width of the box.
        """
        return self.__width

    def get_height(self):
        """
        Returns the height of the box.
        """
        return self.__height


def box_sort(box_list):
    """
    Sorts a list of Box objects in place, in descending order based on their
    volume using the insertion sort algorithm.
    """
    for i in range(1, len(box_list)):
        key_box = box_list[i]
        key_volume = key_box.volume()
        k = i - 1
        while k >= 0 and box_list[k].volume() < key_volume:
            box_list[k + 1] = box_list[k]
            k -= 1
        box_list[k + 1] = key_box
