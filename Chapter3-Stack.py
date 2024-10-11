def input_data():
    List = []
    print("Enter elements for list, enter 'done' when finished:")
    while True:
        num = input("Enter element one at a time: ")
        if num.lower() == 'done':
            break
        List.append(num)
    return List

def reverse_array(List):
    temp = []
    for item in List:
        temp.append(item)
    reversed = []
    while temp:
        reversed.append(temp.pop())
    return reversed

if __name__ == "__main__":
    inputList = input_data()
    print(inputList)
    inputList = reverse_array(inputList)
    print(inputList)
