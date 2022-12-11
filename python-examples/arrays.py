import heapq

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

def heapqify_and_arrays():
    array = [5,4,8,4,3,8]
    print('array before heapify ' + str(array))
    heapq.heapify(array)
    print('printing array after heapify ' + str(array))
    # can't print heapq! not an object with our data
    #print('printing heapq ' + str(heapq))

def heappop_example():
    array = [5,4,3,2,1]
    # heappop doesn't on first iteration if you don't heapify first
    heapq.heapify(array)
    print('len ' + str(len(array)) + ' print array before heappop ' + str(array))
    temp_num = heapq.heappop(array)
    print(temp_num)
    print('len ' + str(len(array)) + ' print array after 1 heappop ' + str(array))
    temp_num = heapq.heappop(array)
    print(temp_num)
    print('len ' + str(len(array)) + ' print array after 2 heappop ' + str(array))
    temp_num = heapq.heappop(array)
    print(temp_num)
    print('len ' + str(len(array)) + ' print array after 3 heappop ' + str(array))
    temp_num = heapq.heappop(array)
    print(temp_num)
    print('len ' + str(len(array)) + ' print array after 4 heappop ' + str(array))

def heappush_example():
    

if __name__ == "__main__":
    #delete_array_element()
    #sort_array_with_lambda()
    #heapqify_and_arrays()
    #heappop_example()
