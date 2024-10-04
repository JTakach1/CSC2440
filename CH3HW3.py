class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class SortLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        if (self.head == None):
            self.head = Node(data)
            return
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        newNode = Node(data)
        curr.next = newNode

    def merge(self, front, back):
        if not front:
            return back
        if not back:
            return front

        if front.data <= back.data:
            merged = front
            merged.next = self.merge(front.next, back)
        else:
            merged = back
            merged.next = self.merge(front, back.next)

        return merged

    def split(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # Split the list into two halves
        return head, mid

    def mergeSort(self, head):
        if not head or not head.next:
            return head

        left, right = self.split(head)  # Split the list into halves

        leftSort = self.mergeSort(left)  # Sort the left half
        rightSort = self.mergeSort(right)  # Sort the right half

        return self.merge(leftSort, rightSort)  # Merge the sorted halves

    def sort(self):
        self.head = self.mergeSort(self.head)

    def printList(self,n):
        while (n != None):
            print(n.data, end = " ")
            n = n.next

    def AverageOfEven(self, head):
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
    list = SortLinkedList()
    list.addNode(4)
    list.addNode(2)
    list.addNode(7)
    list.addNode(1)
    list.addNode(6)
    list.addNode(3)
    list.addNode(5)
    list.printList(list.head)


    list.sort()
    print("\n \nSorted List")
    list.printList(list.head)

    evens = list.AverageOfEven(list.head)
    print("\nAverage Evens")
    print(evens)
