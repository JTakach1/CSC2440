import heapq

def treeValuesInputs():
    inputValuesStorage = []
    while True:
        valForTree = input("Enter heap values one at a time. Type 'done' to stop inputting: ")
        if valForTree.lower() == 'done':
            break
        else:
            inputValuesStorage.append(valForTree)

    return inputValuesStorage

def minHeapSort(arr):
    heapq.heapify(arr)
    valueStorage = []
    while arr:
        valueStorage.append(heapq.heappop(arr))

    left = 0
    right = len(valueStorage) - 1

    while left < right:
        valueStorage[left], valueStorage[right] = valueStorage[right], valueStorage[left]
        left += 1
        right -= 1

    return valueStorage

if __name__ == "__main__":
    arr = treeValuesInputs()

    sortedArray = minHeapSort(arr)
    print("Sorted values in decreasing order:")
    print(sortedArray)
