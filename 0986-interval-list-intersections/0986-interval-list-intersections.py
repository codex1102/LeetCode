class Solution:

    def intervalIntersection(self, firstList, secondList):

        i = 0
        j = 0

        answer = []

        while i < len(firstList) and j < len(secondList):

            # Find intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # If intersection exists
            if start <= end:
                answer.append([start, end])

            # Move the pointer whose interval ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return answer