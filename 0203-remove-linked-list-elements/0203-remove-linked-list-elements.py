class Solution:
    def removeElements(self, head, val):

        if not head:
            return None

        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next

        return head