class Solution(object):

  def isPalindrome(self, x):
    """:type x: int

    :rtype: bool
    """
    # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
      return False

    result = 0
    num = x  # Store original value of x

    while num > 0:
      ld = num % 10
      result = (result * 10) + ld
      num = num // 10

    return result == x