import random
len_list = 15
def get_unique_list_numbers() -> list[int]:
    random_list = [random.randint(-10, 10) for _ in range(len_list+1)]
    while len(random_list) != len(set(random_list)):
        random_list = [random.randint(-10, 10) for _ in range(len_list + 1)]
    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
