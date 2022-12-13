# Data Structure - queues

# Queue - the least recently added item is removed first.
# linear data structure, first in first out (FIFO)
# customer that came first is served first

print('\nOption 1 - queue from list')

list_queue = []

list_queue.append('a')
list_queue.append('b')
list_queue.append('c')

print('Initial queue')
print(list_queue)

print('\nElements dequeued from queue')
print(list_queue.pop(0))
print(list_queue.pop(0))
print(list_queue.pop(0))

print('\nQueue after removing elements')
print(list_queue)

print('\nOption 2 - deque')

from collections import deque

deque_queue = deque()

deque_queue.append('a')
print(deque_queue)
deque_queue.append('b')
print(deque_queue)
deque_queue.append('c')
print(deque_queue)

print('Initial queue')
print(deque_queue)

print('\nElements dequeued from the queue')
print(deque_queue.popleft(), deque_queue)
print(deque_queue.popleft(), deque_queue)
print(deque_queue.popleft(), deque_queue)

print('\nQueue after removing elements')
print(deque_queue)

print('\nOption 3 - queue')

from queue import Queue

q = Queue(maxsize = 3)

print('size of q: ', q.qsize())

q.put('a')
q.put('b')
q.put('c')

print('\nFull: ', q.full())

print('\nElements dequeued from the queue')
print(q.get())
print(q.get())
print(q.get())

print('\nEmpty: ', q.empty())

q.put(1)
print('\nEmpty: ', q.empty(), q)

print('\nFull: ', q.full(), q)