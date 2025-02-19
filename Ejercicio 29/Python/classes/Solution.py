class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        
        while dividend >= divisor:
            temp, multiple = divisor, 1
           
            while dividend >= (temp << 1): 
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple
        
        if negative:
            result = -result
        
        return min(max(-2**31, result), 2**31 - 1)
