
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        node = head
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

            

        