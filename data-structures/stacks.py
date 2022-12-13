# Data Structure - Stack

# Stack = linear data structure that stores items in a last in first out
# or first in last out manner. A new element is added to one end (A) and
# an element is removed from that end only (end A).

# [1,2,3] add [5]
# [1,2,3,5]
# remove [5]
# [1,2,3] removed [5]

# Option 1 - array 

print('\nOption 1 - array ')

array_stack = []

array_stack.append('a')
array_stack.append('b')
array_stack.append('c')

print('Initial stack')
print(array_stack)

print('\nElements popped from stack:')
print(array_stack.pop())
print(array_stack.pop())
print(array_stack.pop())

print('\nStack after elements are popped:')
print(array_stack)

# Option 2 - deque
print('\nOption 2 - deque')

from collections import deque

deque_stack = deque()

deque_stack.append('a')
deque_stack.append('b')
deque_stack.append('c')

print('Initial stack:')
print(deque_stack)

print('\nElements popped from stack')
print(deque_stack.pop())
print(deque_stack.pop())
print(deque_stack.pop())

print('\nStack after elements are popped:')
print(deque_stack
)

#Option 3 - lifo queue

print('\nOption 3 - lifo queue')

from queue import LifoQueue

lifoQueue_stack = LifoQueue(maxsize=3)

print('stack size ' + str(lifoQueue_stack.qsize()))

lifoQueue_stack.put('a')
lifoQueue_stack.put('b')
lifoQueue_stack.put('c')

print('Full: ' ,  lifoQueue_stack.full())
print('Size: ', lifoQueue_stack.qsize() )


print('\nElements popped from stack')
print(lifoQueue_stack.get())
print(lifoQueue_stack.get())
print(lifoQueue_stack.get())

print('\nEmpty: ', lifoQueue_stack.empty())
