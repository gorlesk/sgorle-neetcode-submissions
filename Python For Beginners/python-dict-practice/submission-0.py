from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    l = len(word)
    my_dict = {}
    index = 0
    while index < l:
        if word[index] in my_dict:
            count = my_dict[word[index]]
            count += 1
            my_dict[word[index]] = count
        else:
            my_dict[word[index]] = 1

        index += 1

    return my_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
