# check amstrong number 
class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = str(n)
        k = len(s)
        total_sum = sum(int(digit) ** k for digit in s)
        return total_sum == n