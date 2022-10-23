class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return False
        return n == 0 or (n % 2 == 0 and self.isPowerOfTwo(n // 2))
t=Solution()
n=16
print(t.isPowerOfTwo(n))
