import heapq
def input_tree_values():
    arr = []
    while True:
        value = input("Enter tree values one at a time. Type 'done' when you're finished: ")
        if value.lower() == 'done':
            break
        arr.append(int(value))
        return arr


def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        smallest = heapq.heappop(arr)
        sorted_arr.insert(0, smallest)

    return sorted_arr

def print_sorted_values(arr):
    print("Sorted values:")
    print(arr)


arr = input_tree_values()
sorted_arr = heap_sort(arr)
print_sorted_values(sorted_arr)
