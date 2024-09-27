def selectionSort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

def averageEvens(list2):
    evenNumbers = []
    for i in range(len(list2) - 1):
        if list2[i] % 2 == 0:
            evenNumbers.append(list2[i])
    average = sum(evenNumbers) / len(evenNumbers)
    return average


mainList = [2,5,3,1,4,7,6]
print("unsorted list \n", mainList)

selectSortList = selectionSort(mainList)

print("sorted list \n", selectSortList)

evens = averageEvens(mainList)

print("sum of evens from list \n", evens)
