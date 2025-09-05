from collections import Counter
import heapq


def sort_character_by_frequency(s: str) -> str:
    counter = {}

    for char in s:
        counter[char] = counter.get(char, 0) + 1
    
    max_heap = []
    for char, count in counter.items():
        heapq.heappush(max_heap, (-1 * count, char))
    
    result = ""
    while len(max_heap) > 0:
        count, char = heapq.heappop(max_heap)
        result += char * (count * -1)
    
    return result


s = "buubble"
print(sort_character_by_frequency(s))

