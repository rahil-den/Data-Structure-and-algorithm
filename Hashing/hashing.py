# import List
from typing import List
def hashMostFrequent(nums: List[int]) -> int:
    hashmap ={}
    for i,v in enumerate(nums):
        if v not in hashmap:
            hashmap[v] = 1
        else:
            hashmap[v] += 1
    most_frequent = max(hashmap, key=hashmap.get)
    return most_frequent

if __name__ == '__main__':
    arr = [1, 2, 3, 2, 4, 5, 2]
    print(hashMostFrequent(arr))  # Output: 2