class Solution(object):
    def smallestNumber(self, num, t):
        a = b = c = d = 0
        temp_t = t
        while temp_t % 2 == 0:
            a += 1
            temp_t //= 2
        while temp_t % 3 == 0:
            b += 1
            temp_t //= 3
        while temp_t % 5 == 0:
            c += 1
            temp_t //= 5
        while temp_t % 7 == 0:
            d += 1
            temp_t //= 7
        
        # If t has prime factors other than 2, 3, 5, 7
        if temp_t > 1:
            return "-1"

        # Prime factors contributed by each digit 1..9
        digit_factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        # Helper to compute minimum digits needed for factors (req_a, req_b, req_c, req_d)
        def get_min_len(req_a, req_b, req_c, req_d):
            if req_a <= 0 and req_b <= 0 and req_c <= 0 and req_d <= 0:
                return 0
            req_a = max(0, req_a)
            req_b = max(0, req_b)
            req_c = max(0, req_c)
            req_d = max(0, req_d)

            cnt = req_c + req_d
            cnt += req_b // 2
            rem3 = req_b % 2

            cnt += req_a // 3
            rem2 = req_a % 3

            if rem2 == 1 and rem3 == 1:
                cnt += 1
            elif rem2 == 2 and rem3 == 1:
                cnt += 2
            elif rem2 == 1 and rem3 == 0:
                cnt += 1
            elif rem2 == 2 and rem3 == 0:
                cnt += 1
            elif rem2 == 0 and rem3 == 1:
                cnt += 1

            return cnt

        # Helper to get the multiset of minimal digits
        def get_min_digits(req_a, req_b, req_c, req_d):
            if req_a <= 0 and req_b <= 0 and req_c <= 0 and req_d <= 0:
                return []
            req_a = max(0, req_a)
            req_b = max(0, req_b)
            req_c = max(0, req_c)
            req_d = max(0, req_d)

            res = []
            res.extend([5] * req_c)
            res.extend([7] * req_d)

            res.extend([9] * (req_b // 2))
            rem3 = req_b % 2

            res.extend([8] * (req_a // 3))
            rem2 = req_a % 3

            if rem2 == 1 and rem3 == 1:
                res.append(6)
            elif rem2 == 2 and rem3 == 1:
                res.append(2)
                res.append(6)
            elif rem2 == 1 and rem3 == 0:
                res.append(2)
            elif rem2 == 2 and rem3 == 0:
                res.append(4)
            elif rem2 == 0 and rem3 == 1:
                res.append(3)

            res.sort()
            return res

        N = len(num)

        # Precompute prefix factor sums and find the index of the first '0'
        pref_a = [0] * (N + 1)
        pref_b = [0] * (N + 1)
        pref_c = [0] * (N + 1)
        pref_d = [0] * (N + 1)

        first_zero = N
        for i, ch in enumerate(num):
            if ch == '0':
                first_zero = i
                break
            d_val = int(ch)
            fa, fb, fc, fd = digit_factors[d_val]
            pref_a[i + 1] = pref_a[i] + fa
            pref_b[i + 1] = pref_b[i] + fb
            pref_c[i + 1] = pref_c[i] + fc
            pref_d[i + 1] = pref_d[i] + fd

        # Case 1: Try to construct a number of same length N
        start_i = min(N, first_zero)
        for i in range(start_i, -1, -1):
            if i == N:
                # Check if num itself is valid
                if pref_a[N] >= a and pref_b[N] >= b and pref_c[N] >= c and pref_d[N] >= d:
                    return num
                continue

            rem_a = a - pref_a[i]
            rem_b = b - pref_b[i]
            rem_c = c - pref_c[i]
            rem_d = d - pref_d[i]

            min_digit = int(num[i]) + 1
            for d_val in range(min_digit, 10):
                fa, fb, fc, fd = digit_factors[d_val]
                req_a = rem_a - fa
                req_b = rem_b - fb
                req_c = rem_c - fc
                req_d = rem_d - fd

                suf_len = N - 1 - i
                if get_min_len(req_a, req_b, req_c, req_d) <= suf_len:
                    # Construct solution for length N
                    min_d = get_min_digits(req_a, req_b, req_c, req_d)
                    ones_count = suf_len - len(min_d)
                    suffix = ['1'] * ones_count + [str(x) for x in min_d]
                    suffix.sort()
                    return num[:i] + str(d_val) + "".join(suffix)

        # Case 2: Construct the smallest number of length > N
        min_d = get_min_digits(a, b, c, d)
        target_len = max(N + 1, len(min_d))
        ones_count = target_len - len(min_d)
        res_digits = ['1'] * ones_count + [str(x) for x in min_d]
        res_digits.sort()
        return "".join(res_digits)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna