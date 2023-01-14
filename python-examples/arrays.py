def delete_array_element():
    print('deleting an element from an array')
    array = ['cat', 'dog', 'pig']
    print(array)
    del array[0]
    print('delete item at index 0')
    print(array)

def sort_array_with_lambda():
    array = [[0,30],[30,5],[15,20]]
    print(array)
    # lambda arguments : expression
    # key - function that serves as a key for the sort comparison
    array.sort(key= lambda x: x[0])
    print(array)

def insert_array():
    array = [[0,30],[30,5],[15,20]]
    print('before insertion ' + str(array))
    array.insert(2,'a')
    print('after insertion ' + str(array))

import array as arr

def array_import():
    c = arr.array('i',[1,2,3,4,5,6,7,8,9])
    print('Element you have accessed', c[2])
    print('Element you have accesssed:', c[1])

def reverse_array():
    s = 'hello world'
    s = s[::-1]
    print(s)

def remove_last_element_array():
    s = 'hello world'
    s = s[:-1]
    print(s)

# Note that we can index a range using the colon (:) operator. A colon by itself means fetch everything.
# A colon on the right side of an index means everything after the specified index.

def index_then_colon():
    arr = [1,2,3,4,5,6,7,8,9]
    print('\neverthing after the index 2')
    print('arr[2:]', arr[2:])
    print('everything after the index -2')
    print('arr[-2:]', arr[-2:])

def colon_then_index():
    arr = [1,2,3,4,5,6,7,8,9]
    print('\neverything before the index 2')
    print('arr[:2]', arr[:2])
    print('everything before the index -2')
    print('arr[:-2]', arr[:-2])
  

if __name__ == "__main__":
    #delete_array_element()
    #sort_array_with_lambda()
    #insert_array()
    #array_import()
    #reverse_array()
    #remove_last_element_array()
    index_then_colon()
    colon_then_index()

