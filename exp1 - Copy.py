"""
this function returns the largest number in the list

original code without intention to import as module

numbers = [10, 3, 6, 2]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
"""


def find_max(list_of_numbers):
    max = list_of_numbers[0]
    for number in list_of_numbers:
        if number > max:
            max = number
    return max
