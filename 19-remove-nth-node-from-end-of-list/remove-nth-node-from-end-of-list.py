# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        _dict = dict()
        idx = 1
        node = head
        
        while True:
            _dict[idx] = node
            
            node = node.next
            
            if node is None:
                break
            else:
                idx += 1 

        if idx-n + 2 in _dict:
            n_node =  _dict[idx - n + 2] 
        else:
            n_node = None
            
        if idx-n in _dict:
            f_node =  _dict[idx - n]
            f_node.next = n_node
            return head
        else:
            return n_node
            
            