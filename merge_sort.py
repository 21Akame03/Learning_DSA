import matplotlib.pyplot as plt
import numpy as np
# MergeSort in Python


def mergeSort(array):
    if len(array) > 1:
        update_visualization(array)
        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
                update_visualization(array)
            else:
                array[k] = M[j]
                j += 1
                update_visualization(array)
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            update_visualization(array)

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            update_visualization(array)

def update_visualization(array):
    x = np.arange(0, len(array), 1)
    plt.bar(x, array)
    plt.pause(0.01)
    plt.clf()



# Driver program
if __name__ == '__main__':
    array = np.random.randint(0, 100, 50).tolist()
    x = np.arange(0, 50, 1)
    print(f"Before sorting {array}")
    mergeSort(array)

    print(f"Sorted array is: {array}")
    plt.show()
