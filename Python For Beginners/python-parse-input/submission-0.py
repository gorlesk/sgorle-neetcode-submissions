from typing import List

def read_integers() -> List[int]:
    input_str = (input())
    list_str = input_str.split(",")
    list_int = list()
    for i in list_str:
        list_int.append(int(i))
    return list_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
