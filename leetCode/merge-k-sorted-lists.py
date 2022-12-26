'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2

Input: lists = []
Output: []

Example 3

Input: lists = [[]]
Output: []

'''


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # mine works!
    def sammy_mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # edge cases
        if len(lists) == 0:
            return ListNode("")

        for i in range(lists.count(None)):
            lists.remove(None)

        prehead = ListNode(-1)

        prev = prehead

        while len(lists) > 0:
            
            # find smallest node
            smallest_node = ListNode(-1) # here so python doesn't complain
            i = 0
            for list_node in lists:
                if i == 0:
                    smallest_node = list_node
                    i = 1
                elif list_node.val < smallest_node.val:
                    smallest_node = list_node
            
            # add smallest node to return 
            prev.next = smallest_node
            prev = prev.next

            # iterate to the next node, from the chosen node
            #smallest_node = smallest_node.next <- didn't work

            if smallest_node in lists and smallest_node != ListNode(""):
                lists.remove(smallest_node)
                smallest_node = smallest_node.next
                lists.append(smallest_node)


            #for list_node in lists:
            #    if smallest_node == list_node:
            #        list_node = list_node.next
            #        break

            if None in lists:
                lists.remove(None)

            # remove a node with the same value
            #element_index = lists.index(smallest_node)
            #node_taken = list[element_index]
            #if node_taken.next == None:
            #    lists.remove(None)
            #else:
            #    node_taken = node_taken.next

        return prehead.next if prehead.next != None else ListNode("")

if __name__ == "__main__":
