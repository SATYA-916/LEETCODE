from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = {}

        # Count frequencies of each number
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        t = 1

        # Special case for handling 1s (since 1 * 1 = 1)
        if 1 in d:
            t = max(t, d[1] if d[1] % 2 else d[1] - 1)

        # Process all other numbers
        for i in d:
            if i == 1:
                continue

            j = i
            ans = 1

            # While the current element can form the sides (freq >= 2) 
            # and its square exists to continue the chain
            while j in d and d[j] >= 2 and (j * j) in d:
                ans += 2
                j = j * j

            t = max(t, ans)

        return t