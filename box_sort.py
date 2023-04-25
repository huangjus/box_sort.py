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

        Args:
            length (float): Length of the box.
            width (float): Width of the box.
            height (float): Height of the box.
        """
        self.__length = length
        self.__width = width
        self.__height = height

    def volume(self):
        """
        Calculates and returns the volume of the box.

        Returns:
            float: Volume of the box.
        """
        return self.__length * self.__width * self.__height

    def get_length(self):
        """
        Returns the length of the box.

        Returns:
            float: Length of the box.
        """
        return self.__length

    def get_width(self):
        """
        Returns the width of the box.

        Returns:
            float: Width of the box.
        """
        return self.__width

    def get_height(self):
        """
        Returns the height of the box.

        Returns:
            float: Height of the box.
        """
        return self.__height


def box_sort(box_list):
    """
    Sorts a list of Box objects in place, in descending order based on their
    volume using the insertion sort algorithm.

    Args:
        box_list (list): List of Box objects to be sorted.
    """
    for i in range(1, len(box_list)):
        key_box = box_list[i]
        key_volume = key_box.volume()
        j = i - 1
        while j >= 0 and box_list[j].volume() < key_volume:
            box_list[j + 1] = box_list[j]
            j -= 1
        box_list[j + 1] = key_box
