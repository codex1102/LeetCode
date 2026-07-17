class Solution:
    def moveZeroes(self, nums):
        result = []

        # Add all non-zero elements
        for num in nums:
            if num != 0:
                result.append(num)

        # Add zeros
        while len(result) < len(nums):
            result.append(0)

        # Copy back to original array
        nums[:] = result