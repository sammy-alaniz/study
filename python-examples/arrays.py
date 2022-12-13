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

if __name__ == "__main__":
    #delete_array_element()
    #sort_array_with_lambda()
    insert_array()
    array_import()

