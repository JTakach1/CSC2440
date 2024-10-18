from collections import deque

def input_array():
    inputArr = input("Enter the elements separated by spaces: ")

    arr = []
    for item in inputArr.split():
        arr.append(int(item))
    return arr

def reverseArrayUsingQueue(arr):
    queue = deque(arr)
    reversedArr = []
    while queue:
        reversedArr.append(queue.pop())
    return reversedArr

if __name__ == "__main__":
    arr = input_array()
    reversed_arr = reverseArrayUsingQueue(arr)

    output = []
    for x in reversed_arr:
        output.append(str(x))

    print("Reversed array: ", output)
