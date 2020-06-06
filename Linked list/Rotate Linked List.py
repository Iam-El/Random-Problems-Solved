class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        elif head.next is None:
            return head
        else:
            while k>0:
                cur=head
                prev=None
                while cur.next is not None:
                    prev=cur
                    cur=cur.next
                prev.next=None
                cur.next=head
                head=cur
                k=k-1
            return head