def add_two_numbers() -> int:
    list_str = input()
    list_str = list_str.split(",")
    sum = 0
    for i in (list_str):
        sum += int(i)

    return sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
