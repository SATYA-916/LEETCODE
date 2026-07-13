class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        x = "123456789"
        i = 0
        j = len(str(low))
        ans = []
        var = j

        while True:
            num = int(x[i:j])

            if low <= num <= high:
                ans.append(num)

            i += 1
            j += 1

            if j >= 10 or int(x[i:j]) > high:
                var += 1
                if var > 9:   # No sequential numbers longer than 9 digits
                    break
                i = 0
                j = var

        return ans