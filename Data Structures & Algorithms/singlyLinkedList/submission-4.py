class Node:
    def __init__(self, val: int):
        self.val=val
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=-1
    
    def get(self, index: int) -> int:
        if (index < 0) or (index > self.length):
            return(-1) 
        currNode=self.head
        count=0
        while count!=index:
            count+=1
            currNode=currNode.next
        return(currNode.val)

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
            self.tail=self.head
        else:
            newHead=Node(val)
            newHead.next=self.head
            self.head=newHead
        self.length+=1

    def insertTail(self, val: int) -> None:
        if not self.tail:
            self.tail=Node(val) 
            self.head=self.tail
        else:
            newTail=Node(val)
            self.tail.next=newTail
            self.tail=newTail
        self.length+=1

    def remove(self, index: int) -> bool:
        if (index < 0) or (index > self.length):
            return(False)
        prevNode=None
        currNode=self.head
        count=0
        while count!=index:
            count+=1
            prevNode=currNode
            currNode=currNode.next
        if not prevNode:
            self.head=self.head.next
            self.length-=1
            return(True)
        if currNode==self.tail:
            self.tail=prevNode
            self.length-=1
            return(True)           
        prevNode.next=currNode.next
        self.length-=1
        return(True)

    def getValues(self) -> List[int]:
        if not self.head:
            return([])
        arr=list()
        headNode=self.head
        while headNode!=self.tail:
            arr.append(headNode.val)
            headNode=headNode.next
        arr.append(headNode.val)
        return(arr)
        
