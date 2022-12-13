'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

'''

#my attempt

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd_didnt_work(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dq = deque()
        return_head = ListNode()
        
        # place linked list in a deque
        while head != None:
            dq.append(head.val)
            head = head.next
        
        for i in range(1,len(dq)+1):
            
            # create head node on first iteration
            if i == 1:
                head = ListNode(dq.popleft())
                return_head = head
            
            if ((len(dq)+1)-n-1) == i:
                dq.popleft()
                continue

            newNode = ListNode(dq.popleft())
            head.next = newNode
            head = head.next
        return return_head
#couldn't get this to work because of references
#class Solution:
#    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#        length = 0
#        current_node = head
#
#        while current_node != None:
#            length += 1
#            current_node = current_node.next
#        
#        current_node = head
#        new_ret = current_node
#
#        node_to_remove = (length - n + 1)
#        for i in range(1, length):
#            if node_to_remove-1 == i:
#                current_node = current_node.next.next
#                continue
#
#            if current_node != None and current_node.next != None:
#                current_node = current_node.next
#

#        return new_ret

#gave up
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#class Solution:
#    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#        length = 0
#        current_node = head
#
#        while current_node != None:
#            length += 1
#            current_node = current_node.next
#        
#        current_node = head
#        new_ret = current_node
#
#        node_to_remove = (length - n + 1)
#        for i in range(1, length):
#            if node_to_remove-3 == i:
#                current_node = current_node.next
#                print(str(current_node.val))
#                continue
#
#            if current_node != None and current_node.next != None:
#                current_node = current_node.next
#
#        return new_ret