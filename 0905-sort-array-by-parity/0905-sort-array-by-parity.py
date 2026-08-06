class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = [] #
        for num in nums :
            if num % 2 == 0:
                a.append(num)
        for num in nums :
            if num % 2 == 1:
                a.append(num)
        return a
