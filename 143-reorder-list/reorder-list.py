# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        hold = None
        ans = None
        
        while fast and fast.next:
            fast = fast.next.next
            
            hold, hold.next, slow = slow, hold, slow.next
        
        if fast:
            hold, hold.next, slow = slow, hold, slow.next
            
            while slow:
                ans, ans.next, ans.next.next, slow, hold = slow, hold, ans, slow.next, hold.next
            
            ans, ans.next = hold, ans
        else:
            while slow:
                ans, ans.next, ans.next.next, slow, hold = hold, slow, ans, slow.next, hold.next

                    
        
        