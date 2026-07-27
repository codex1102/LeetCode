class Solution:
    def middleNode(self, head):

        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        middle = count // 2

        current = head

        for _ in range(middle):
            current = current.next

        return current