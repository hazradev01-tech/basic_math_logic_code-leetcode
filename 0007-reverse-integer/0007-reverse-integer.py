class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Convert to string to index individual characters
        s = str(x)
        
        # Track sign and isolate the digit characters
        if s[0] == '-':
            sign = -1
            chars = list(s[1:])
        else:
            sign = 1
            chars = list(s)
            
        # Two pointers starting at opposite ends
        left, right = 0, len(chars) - 1
        
        # Swap characters until pointers meet in the middle
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            
        # Reconstruct the reversed integer
        rev = sign * int("".join(chars))
        
        # Enforce 32-bit signed integer boundary constraints
        if rev < INT_MIN or rev > INT_MAX:
            return 0
            
        return rev
        