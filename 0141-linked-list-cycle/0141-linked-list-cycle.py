# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        tail = head
        while tail:
            if tail in visited:
                return True
            visited.add(tail)
            tail = tail.next    
        return False
        