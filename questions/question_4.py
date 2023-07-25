"""
Write a program that creates a two-dimensional array with 500
elements, and fills the array with an alternating pattern of 0’s and 1’s.
"""


def binary_array_2D():

    list_2D = []

    for y in range(0, 10):
        list = []
        for x in range(0, 10):
            if x % 2 == y % 2:
                list.append(1)
            else:
                list.append(0)


        list_2D.append(list)

    return list_2D



if __name__ == "__main__":

    list = binary_array_2D()

    for i in list:
        print(i)
