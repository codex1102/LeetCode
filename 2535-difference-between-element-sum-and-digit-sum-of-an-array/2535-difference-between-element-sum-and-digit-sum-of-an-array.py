class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for sums in nums:
            element_sum = element_sum + sums
        for num in nums:
            for digit in str(abs(num)):
                digit_sum += int(digit)
        return abs(element_sum - digit_sum)