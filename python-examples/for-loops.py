
print('simple for loop')
for i in range(10):
    print(i)

print('matrix for loop - code golf')
num_cols = 3
num_rows = 2
matrix = [[' '] * num_cols for _ in range(num_rows)]
print(matrix)

print('matrix for loop - easy')
cols = []
for _ in range(num_cols):
    cols = cols + [' '] # this is how you concatenate an array

rows = []
for _ in range(num_rows):
    rows.append(cols)

print(rows)

print('\nbreak example at 5')
for i in range(10):
    if i == 5 :
        break
    print(i)
print('end of break example\n')

print('continue example at 5')
for i in range(10):
    if i == 5 :
        continue
    print(i)
print('end of continue example\n')

print('pass example at 5')
for i in range(10):
    if i == 5 :
        pass
    print(i)
print('end of pass example\n')




print('looped assignment')
n = 5
dp = [[False, False] for _ in range(n)]
print(dp)
dp[n - 1] = [True, True]
print(dp)

# range(start, stop, step)
print('\nsimple for loop NEGATIVE - range(5, -1, -1)')
for i in range(5, -1, -1):
    print(i)

print('\nsimple for loop NEGATIVE - range(5, -2, -1)')
for i in range(5, -2, -1):
    print(i)

print('\n\nTrying reverse range num list')
for i in range(1,0,-1):
    print(i)

print('\n\nTrying reverse range num list : for i in range(5,-1,-1)')
for i in range(5,-1,-1):
    print(i)