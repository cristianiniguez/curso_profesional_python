import time


class FiboIter():
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            result = self.n1
        elif self.counter == 1:
            result = self.n2
        else:
            self.n1, self.n2 = self.n2, self.n1 + self.n2
            result = self.n2

        if not self.max or result <= self.max:
            self.counter += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    fibonacci = FiboIter(10)
    for element in fibonacci:
        print(element)
        time.sleep(1)
