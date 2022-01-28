#! This example has an exception due to recusive depth


def binarysearch(array: list, start: int, end:int, searchitem: int) -> int:
    # get an integer mid point
    midpoint = (start + end) // 2
    
    if array[midpoint] == searchitem:
        return midpoint

    if searchitem >  midpoint:
        return binarysearch(array, midpoint, end, searchitem)
    else:
        return binarysearch(array, start, midpoint, searchitem)
    
    return -1

def insertionsort(array: list, keyindex: int = 1) -> list:
    if keyindex >= len(array):
        return array 

    key = array[keyindex]
    index = keyindex -  1
    while index >= 0 and key < array[index]:
        array[index + 1] = array[index]
        index = index - 1

    array[index + 1] = key
    return insertionsort(array, keyindex + 1)


array = [789, 4, 2, 5, 7, 89, 2, 554, 6664, 1, 22225, 14, 75, 32, 12]
array = insertionsort(array)
end = len(array) - 1
print(f"Sorted array is {array}")
print(f"89 is found at index {binarysearch(array, 0, end, 89)}")
print(f"75 is found at index {binarysearch(array, 0, end, 14)}")
print(f"554 is found at index {binarysearch(array, 0, end, 32)}")
