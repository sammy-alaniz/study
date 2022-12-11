from collections import deque

array = ['cat', 'mouse', 'pig']
print('print array before deque' + str(array))

dq = deque(array)

print('print array after deque' +  str(array))
print('printing deque' + str(dq))

dq.append('horse')

print('added horse ' + str(dq))

dq.appendleft('shark')

print('addedleft shark ' + str(dq))