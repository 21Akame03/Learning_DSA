import matplotlib.pyplot as plt
import numpy as np

def insertionsort(array: list, x, keyindex: int = 1) -> list:
    if keyindex >= len(array):
        return array 
    

    plt.bar(x,  array)
    plt.pause(0.0000001)
    plt.clf()

    key = array[keyindex]
    index = keyindex -  1
    while index >= 0 and key < array[index]:
        array[index + 1] = array[index]
        index = index - 1

    array[index + 1] = key
    return insertionsort(array, x, keyindex + 1)

#  array = [789, 4, 2, 5, 7, 89, 2, 554, 6664, 1, 22225, 14, 75, 32, 12]

amount = 100
array = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)
print(insertionsort(array, x))
plt.show()
