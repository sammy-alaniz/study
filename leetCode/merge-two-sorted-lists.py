'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []


'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def create_new_linked_list(self, sorted :list, head :ListNode):
        for i in range(len(sorted)):
            if i == 0:
                head.val = sorted[i]
            else:
                head.next = ListNode(sorted[i])
                head = head.next

    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return ListNode('')

        list_one = []
        list_two = []

        while list1 != None:
            list_one.append(list1.val)
            list1 = list1.next

        while list2 != None:
            list_two.append(list2.val)
            list2 = list2.next

        total_list = []

        total_list += list_one
        total_list += list_two

        total_list.sort()

        print(total_list)

        current_node = ListNode(0)

        self.create_new_linked_list(total_list, current_node)

        #for i in range(len(total_list)):
        #    if i == 0:
        #        current_node.val = total_list[i]
        #    current_node.next = ListNode(total_list[i])
        #    current_node = current_node.next
    
        return current_node


if __name__ == "__main__":
    sol = Solution()
    one = ListNode(1)
    one.next = ListNode(2)

    two = ListNode(4)
    two.next = ListNode(5)

    ret = sol.mergeTwoLists(one,two)
    
    while ret != None:
        print(ret.val)
        ret = ret.next