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


    

if __name__ == "__main__":
    #delete_array_element()
    sort_array_with_lambda()

