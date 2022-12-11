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

# dq evaluates to false once it's empty
while dq:
    print('dq before pop' + str(dq))
    dq.pop()
    print('dq after pop' + str(dq) + '\n')
print('end of while loop!\n')
