"""Write a procedure/method that takes a positive integer parameter
and prints the number that results from adding up the digits of
the parameter. For example, if the parameter has the value 367,
your procedure should print 16. Your procedure must not contain any
input statements
"""

def add_digits(number_to_dissect: int) -> int:

    add_digits = 0


    while number_to_dissect > 0:
        value_in_units_place = number_to_dissect  % 10  # - ((number_to_dissect // 10) * 10)
        add_digits += value_in_units_place
        number_to_dissect //= 10


    return add_digits


if __name__ == "__main__":
    val = add_digits(367)
    print(val)