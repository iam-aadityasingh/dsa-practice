import math
from collections import Counter

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count_map = Counter(answers)
        total = 0

        for x, freq in count_map.items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            total += groups * group_size

        return total
