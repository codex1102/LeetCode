class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []

        nextGreater = {}

        for num in reversed(nums2):

            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                nextGreater[num] = stack[-1]
            else:
                nextGreater[num] = -1

            stack.append(num)

        answer = []

        for num in nums1:
            answer.append(nextGreater[num])

        return answer