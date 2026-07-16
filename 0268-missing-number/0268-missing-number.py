class Solution:
    def missingNumber(self, nums):
        nums.sort()
        print("Sorted:", nums)

        for i in range(len(nums)):
            print(f"i = {i}, nums[i] = {nums[i]}")
            if nums[i] != i:
                return i

        return len(nums)


