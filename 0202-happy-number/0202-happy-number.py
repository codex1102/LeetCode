class Solution:

    def squareSum(self, n):

        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total

    def isHappy(self, n):

        slow = n
        fast = self.squareSum(n)

        while fast != 1 and slow != fast:

            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))

        return fast == 1