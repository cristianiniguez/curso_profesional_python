from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        time = end - start
        print(f'Execution time: {time.total_seconds()} seconds')
        return result
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10**8):
        pass


# random_func()

@execution_time
def suma(a: int, b: int) -> int:
    return a + b


suma(5, 5)
