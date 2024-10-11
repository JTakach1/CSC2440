def input_data():
    arr = []
    print("Enter elements for list, enter 'done' when finished:")
    while True:
        num = input("Enter element one at a time: ")
        if num.lower() == 'done':
            break
        arr.append(num)
    return arr

def reverse_array(arr):
    temp = []
    for item in arr:
        temp.append(item)
    reversed = []
    while temp:
        reversed.append(temp.pop())
    return reversed

if __name__ == "__main__":
    arr = input_data()
    print(arr)
    inputList = reverse_array(arr)
    print(inputList)
