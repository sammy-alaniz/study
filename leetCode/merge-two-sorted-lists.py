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

    
    # this was my attempt
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

   # leet code solutions
    def leet_one_mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # handle edge case
        if list1 is None:
            return list2
        # handle edge case
        elif list2 is None:
            return list1
        # if list one value is less than list two value iterate to the next list one node
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        # if list two value is less than list one value iterate to the next list two ndoe
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def leet_two_mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)

        prev = prehead

        # while list one and list two are not None, opposite of if lol
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        # attach the rest of the non empty sorted list
        prev.next = list1 if list1 is not None else list2

        return prehead.next


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