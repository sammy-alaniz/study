
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