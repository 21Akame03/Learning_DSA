import matplotlib.pyplot as plt
import numpy as np

#  Best case scenario: Ω (n^2)
#  Worst case scenario: O(n^2)



def selectionsort(array):
    for i in range(len(array)):
        smallest_index = i
        for j in range(i, len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
                        
        temp = array[smallest_index]
        array[smallest_index] = array[i]
        array[i] = temp

        plt.bar(x, array)
        plt.pause(0.000000001)
        plt.clf()

        
    return array

if __name__ == '__main__':
    n = 100
    array = np.random.randint(0, 100, n)
    x = np.arange(0, n, 1)

    print(f"Before sorting  {array}")
    array = selectionsort(array.tolist())
    print(f"After sorting {array}")
    

