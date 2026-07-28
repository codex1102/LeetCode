class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        keep = arr[0]
        delete = 0
        answer = arr[0]

        for i in range(1, len(arr)):

            delete = max(delete + arr[i], keep)

            keep = max(arr[i], keep + arr[i])

            answer = max(answer, keep, delete)

        return answer