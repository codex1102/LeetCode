class Solution:
    def maximumSubarraySum(self, nums, k):
        freq = {}
        window_sum = 0
        maximum = 0

        for i in range(len(nums)):
            window_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            if i >= k:
                left = nums[i - k]
                window_sum -= left
                freq[left] -= 1

                if freq[left] == 0:
                    del freq[left]

            if i >= k - 1:
                if len(freq) == k:
                    maximum = max(maximum, window_sum)

        return maximum