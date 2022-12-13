
# start starts at start if 5, first loop will be 5
# end does not inlcude that number, it's     -1
for i in range(5,10):
    print(i)

# 5
# 6
# 7
# 8
# 9

chars = set()
chars.add('c')
chars.add('d')
print(chars)

string = "12345"
print('Len of 12345 : ' + str(len(string)))

#when just giving a length, range will start at zero and n-1 
for i in range(len(string)):
    print(i)