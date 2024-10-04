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
    def partitionLast(self,start,end):
        if (start == end or start == None or end == None):
            return start
        pivotPrev = start
        curr = start
        pivot = end.data
        while (start != end):
            if (start.data < pivot):
                pivotPrev = curr
                temp = curr.data
                curr.data = start.data
                start.data = temp
                curr = curr.next
            start = start.next
        temp = curr.data
        curr.data = pivot
        end.data = temp
        return pivotPrev
    def sort(self,start,end):
        if (start == end or start == None or end == None):
            return start
        pivotPrev = self.partitionLast(start,end)
        self.sort(start, pivotPrev)
        if (pivotPrev != None and pivotPrev == start):
            self.sort(pivotPrev.next, end)
        elif(pivotPrev != None and pivotPrev.next != None):
            self.sort(pivotPrev.next.next,end)
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

    back = list.head
    while (back.next != None):
        back = back.next
    list.sort(list.head, back)
    print("\n \nSorted List")
    list.printList(list.head)

    evens = list.AverageOfEven(list.head)
    print("\nAverage Evens")
    print(evens)
