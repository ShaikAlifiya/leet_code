class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Check each bit from 31 down to 0
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                quotient += (1 << i)

        return -quotient if negative else quotient
        