def make_division_by(n):
    """This closure returns a function that returns the division of an x number by n"""
    assert type(n) in [int, float], "n must be a number"
    assert n != 0, "division by zero is not allowed"

    def divider(x):
        assert type(x) in [int, float], "x must be a number"
        return x / n

    return divider


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # 3

    division_by_18 = make_division_by('9')  # AssertionError: n must be a number
    division_by_18 = make_division_by(0)  # AssertionError: division by zero is not allowed
    print(division_by_3(True))  # AssertionError: x must be a number


if __name__ == '__main__':
    run()
