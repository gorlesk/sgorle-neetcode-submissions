from typing import List, Dict


def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    s = {}
    # for i in range(len(keys)):
    #     s[keys[i]] = values[i]
    # return s

    # for key, val in zip(keys, values):
    #     s[key] = val
    # return s

    return dict(zip(keys, values))

def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    s = []
    for key in keys:
        s.append(hash_map[key])
    return s    


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
