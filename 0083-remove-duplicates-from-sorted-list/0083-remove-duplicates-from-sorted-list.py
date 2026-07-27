class Solution:
    def deleteDuplicates(self, head):

        if not head or not head.next:
            return head

        head.next = self.deleteDuplicates(head.next)

        if head.val == head.next.val:
            return head.next

        return head