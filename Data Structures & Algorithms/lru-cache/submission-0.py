class Node:
    def __init__(self,key, val):
        self.key =key
        self.val =val
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key to node
        self.left,self.right =Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        #insert from right
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev= node
        node.next, node.prev = nxt, prv

         
    def remove(self,node):
        #remove from the list
        before, after = node.prev, node.next
        before.next = after
        after.prev = before


    def get(self, key: int) -> int:
        if key in self.cache:
            #update to most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1



    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            #remove from the list and delete LRU from the hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]


