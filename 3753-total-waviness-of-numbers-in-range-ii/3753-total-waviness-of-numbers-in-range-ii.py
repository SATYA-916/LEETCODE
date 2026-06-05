from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def get_waves(num_str: str) -> int:
            # A number needs at least 3 digits to form a peak or valley
            if len(num_str) < 3:
                return 0
                
            @cache
            def dp(index: int, is_bound: bool, two_before: int, one_before: int, leading_zeros: bool):
                # Base case: We've reached the end of the number
                if index == len(num_str):
                    if leading_zeros:
                        return 0, 0  # (valid_count, waves_count)
                    return 1, 0      # 1 valid number, 0 additional waves at the end
                
                # Determine the maximum digit we can place at the current index
                limit = int(num_str[index]) if is_bound else 9
                total_count = 0
                total_waves = 0
                
                for digit in range(limit + 1):
                    next_leading_zeros = leading_zeros and (digit == 0)
                    next_bound = is_bound and (digit == limit)
                    
                    next_two_before = -1
                    next_one_before = -1
                    current_wave = 0
                    
                    if next_leading_zeros:
                        next_one_before = -1
                        next_two_before = -1
                    else:
                        if leading_zeros:
                            # First non-zero digit of the number
                            next_one_before = digit
                            next_two_before = -1
                        else:
                            # Ongoing number
                            next_one_before = digit
                            next_two_before = one_before
                            
                            # Check if the middle digit (`one_before`) forms a peak or valley
                            if two_before >= 0 and one_before >= 0:
                                is_peak = (one_before > two_before) and (one_before > digit)
                                is_valley = (one_before < two_before) and (one_before < digit)
                                if is_peak or is_valley:
                                    current_wave = 1
                    
                    # Recurse for the next index
                    next_c, next_w = dp(index + 1, next_bound, next_two_before, next_one_before, next_leading_zeros)
                    
                    # Accumulate valid suffixes and waviness 
                    total_count += next_c
                    # The current wave is applied to all valid combinations formed subsequently
                    total_waves += next_w + (current_wave * next_c)
                    
                return total_count, total_waves

            # Start the DP sequence
            _, ans_waves = dp(0, True, -1, -1, True)
            return ans_waves
            
        # Calculate waviness from 0 to num2, minus 0 to num1 - 1
        return get_waves(str(num2)) - get_waves(str(num1 - 1))