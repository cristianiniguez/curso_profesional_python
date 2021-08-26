def is_prime(number: int) -> bool:
    if number < 2:
        return False

    limit: float = number**.5

    for i in range(2, int(limit)+1):
        if number % i == 0:
            return False

    return True


def run():
    print(is_prime(7))
    print(is_prime(10))
    print(is_prime(97))


if __name__ == "__main__":
    run()
