# (b)
#   (i)
from array import array


def linearSearch(val):
    for i in range(len(arrayData)):
        if arrayData[i] == val:
            return True
    
    return False

# (c)
def bubbleSort(arrayData):
    for i in range(len(arrayData)):
        for j in range(len(arrayData) - 1):
            if arrayData[j] > arrayData[j + 1]:
                temp = arrayData[j + 1]
                arrayData[j + 1] = arrayData[j]
                arrayData[j] = temp
    
    return arrayData
if __name__ == "__main__":
    # (a)
    arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

    # (b)
    #   (ii)
    value = None
    while not isinstance(value, int):
        value = int(input("Enter an integer value to be searched in arrayData: "))

    result = linearSearch(value)
    if result: 
        print(f"found {value} in arrayData")
    else: 
        print(f"Did not find {value} in arrayData")
    

    # (c)
    arrayData = bubbleSort(arrayData)
    print(arrayData)