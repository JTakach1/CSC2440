class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

def split(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    temp = slow.next
    slow.next = None
    if temp is not None:
        temp.prev = None
    return temp

def merge(first,second):
    if first is None:
        return second
    if second is None:
        return first
    if first.data < second.data:
        first.next = merge(first.next, second)

        first.prev = None
        return first
    else:
        second.next = merge(first, second.next)
        second.prev = None
        return second
def MergeSort(head):
    if head is None or head.next is None:
        return head
    second = split(head)
    head = MergeSort(head)
    second = MergeSort(second)
    return merge(head,second)
def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end = " ")
        curr = curr.next
    print()
def AverageOfEven(head):
    evenSum = 0
    evenCount = 0

    while head:
        if head.data % 2 == 0:
            evenSum += head.data
            evenCount += 1
        head = head.next
    if evenCount == 0:
        return 0
    return evenSum / evenCount

if __name__ == "__main__":
    list = Node(4)
    list.next = Node(2)
    list.next.next = Node(7)
    list.next.next.next = Node(1)
    list.next.next.next.next = Node(6)
    list.next.next.next.next.next = Node(3)
    list.next.next.next.next.next.next = Node(5)

    printList(list)

    print("\nSorted List:")
    sortedList = MergeSort(list)
    printList(sortedList)
    print("\nAverage of Evens:")
    print(AverageOfEven(sortedList))
