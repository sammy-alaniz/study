# This shows how python passes objects by reference

class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


print("Hello World")

temp = ListNode(1)
print("temp before reassign : " + str(temp.val))
tempTwo = temp
tempTwo.val = 2

print("temp : " + str(temp.val))
print("tempTwo : " + str(tempTwo.val))

one = "sammy"
two = one
two = "alaniz"

print("one : " + one)
print("two : " + two)

