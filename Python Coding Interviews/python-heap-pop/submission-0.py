import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    l1 = []
    for i in range(len(heap)):
        l1.append(heapq.heappop(heap))
    return l1

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
