"""
In a right-angled triangle the length of the
hypotenuse c and the length of the two remaining
sides a and b define the angles of the triangle.


Write a function (method) which takes the three side
lengths of a right-angles triangle (a,b,c) as
parameters and calculates the angles of the triangles.
"""

import math

def calc_angles(a: float, b: float, c: float) -> (float, float, float):
    A = math.degrees(math.atan(a / b))
    B = math.degrees(math.atan(b / a))

    return A, B, 90.0



if __name__ == "__main__":
    print(
        calc_angles(
            2.7, 1.3, 3.0
        )
    )