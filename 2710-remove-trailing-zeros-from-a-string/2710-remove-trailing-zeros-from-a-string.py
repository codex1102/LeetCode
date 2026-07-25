class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        result = num.rstrip('0')
        return result