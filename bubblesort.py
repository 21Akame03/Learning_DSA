import matplotlib.pyplot as plt
import numpy as np

amount = 20

array = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

plt.title('Bubblesort')
n = len(array)
for i in range(n):
    for j in range(0, n-i-1):
        plt.bar(x, array)
        plt.pause(0.000000001)
        plt.clf()
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

plt.show()

