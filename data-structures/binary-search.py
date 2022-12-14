# binary search
# YT link - https://www.youtube.com/watch?v=G1uv8YCQmC0

def search( numbers: list[int], target: int) -> int:
    N = len(numbers)
    l,r = 0,N-1 # loop start's at zero

    while l <= r:

        mid = (l+r)//2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

# MSUT BE SORTED
array = [1,2,3,4,5,6,7,9]
tar = 1
print(str(search(array,tar)))
