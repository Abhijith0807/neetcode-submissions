class Node:
    def __init__(self, key:int, val: int):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache=dict()
        self.lruN=Node(0,0)
        self.mruN=Node(0,0)
        self.lruN.next,self.mruN.prev=self.mruN,self.lruN
    
    def insert(self,node: Node):
        prevN=self.mruN.prev
        prevN.next,node.prev=node,prevN
        node.next,self.mruN.prev=self.mruN,node
    
    def update(self,node: Node, value: int ):
        node.val=value
        node.next.prev,node.prev.next=node.prev,node.next
        prevN=self.mruN.prev
        prevN.next,node.prev=node,prevN
        node.next,self.mruN.prev=self.mruN,node
    
    def remove(self):
        currlsu=self.lruN.next
        del self.cache[currlsu.key]
        self.lruN.next=currlsu.next
        currlsu.next.prev=self.lruN
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return(-1)
        node=self.cache[key]
        self.update(node,node.val)
        return(node.val)
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.update(self.cache[key],value)
        else:
            if len(self.cache)==self.cap:
                self.remove()
                self.cache[key]=Node(key,value)
                self.insert(self.cache[key])
            else:
                self.cache[key]=Node(key,value)
                self.insert(self.cache[key])