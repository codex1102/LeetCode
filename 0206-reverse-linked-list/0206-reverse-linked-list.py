class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):

        prev = None
        current = head

        while current:

            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        return prev


# Create Linked List: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()

new_head = sol.reverseList(head)

print("Reversed List:", end=" ")
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next