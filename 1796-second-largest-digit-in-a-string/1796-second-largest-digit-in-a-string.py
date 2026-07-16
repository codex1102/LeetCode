class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second = -1

        for ch in s:
            if ch.isdigit():
                digit = int(ch)

                if digit > largest:
                    second = largest
                    largest = digit

                elif largest > digit > second:
                    second = digit

        return second