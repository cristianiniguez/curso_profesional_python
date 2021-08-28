def remove_duplicates(list):
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)
    return new_list


def run():
    random_list = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()
