# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = head
        i = 1
        
        # Time Complexity - O(n)
        # Space Complexity - O(1)
        
        # 1. Identify Node to be removed - have a pointer pointing to the prev of node to be deleted
        # Move the current pointer to the end 
        # Release the prev pointer after n 
        # When curr pointer reached end, prev pointer points to the node to prev of the node to be deleted
        # At all times curr pointer and prev pointer are n nodes apart
        while(curr.next != None):
            i += 1
            # Why n+2: 
            # i starts from 1(Error if you choose i=0 and n+1 as it messes deletion of first node) 
            # and you want prev to point to n-1th node
            if i >= (n+2):
                prev = prev.next
            curr = curr.next
        
        # 2. Deletion Step to remove the node as identified in Step 1
        if head.next == None: 
            # Only one node in list - Remove first node
            return None
        elif prev == head and i == n: 
            # Remove first node 
            return prev.next
        elif prev.next == curr:
            # Remove last nide
            prev.next = None
        else: 
            # Remove node in between
            prev.next = prev.next.next
            
        return head