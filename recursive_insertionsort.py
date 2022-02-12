import matplotlib.pyplot as plt
import numpy as np

#  Best case scenario: Ω (n^2)
#  Worst case scenario: O(n^2)


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
        
    # In order to negate the above index -= 1 at the end of the , we have to + 1 
    array[index + 1] = key
    return insertionsort(array, x, keyindex + 1)

#  array = [789, 4, 2, 5, 7, 89, 2, 554, 6664, 1, 22225, 14, 75, 32, 12]

amount = 100
array = np.random.randint(0, 500, amount)
x = np.arange(0, amount, 1)
print(f"Before sorting {array}")
print(insertionsort(array, x))
plt.show()
