import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    rev_heap = []
    for num in nums:
        heapq.heappush(rev_heap, -num)

    l1 = []
    while rev_heap:
        l1.append(-heapq.heappop(rev_heap))
    return l1    

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
