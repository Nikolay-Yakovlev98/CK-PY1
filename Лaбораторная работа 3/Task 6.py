list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers[0]
max_index = 0
last_number = list_numbers[-1]

for i, current_max in enumerate(list_numbers):
    if current_max > max_number:
        max_number = current_max
        max_index = i
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)





