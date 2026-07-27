class Solution:
    def sortPeople(self, names, heights):

        d = {}

        for i in range(len(names)):
            d[heights[i]] = names[i]

        heights.sort(reverse=True)

        result = []

        for h in heights:
            result.append(d[h])

        return result