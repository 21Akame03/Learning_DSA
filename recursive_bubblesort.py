#  Recursive bubble sort

def bubbleSort(array: list) -> list:
    length =  len(array) - 1
    swapped = False

    for i in range(length):
        if array[i] > array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
            swapped = True

    if swapped: return bubbleSort(array)
    return array


array = [4, 5, 8, 9 ,45, 2, 1, 7, 32, 98, 3, 7899, 755, 144, 2121, 4]
assert bubbleSort(array), [1, 2, 3, 4, 4, 5, 7, 8, 9, 32, 45, 98, 144, 755, 2121, 7899]
print(bubbleSort(array))
