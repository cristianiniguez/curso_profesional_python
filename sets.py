def remove_duplicates(my_list):
    return list(set(my_list))


def run():
    random_list = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()
