import time


def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            result = n1
        elif counter == 1:
            result = n2
        else:
            n1, n2 = n2, n1 + n2
            result = n2
        counter += 1
        if not max or result <= max:
            yield result
        else:
            break


if __name__ == '__main__':
    fibonacci = fibo_gen(10)
    for element in fibonacci:
        print(element)
        time.sleep(1)
