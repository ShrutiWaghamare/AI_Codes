def selectionSort(array):
    for step in range(len(array)):
        min_idx = step
        for i in range(step + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i
        array[step], array[min_idx] = array[min_idx], array[step]

data = [-2, 45, 0, 11, -9]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
