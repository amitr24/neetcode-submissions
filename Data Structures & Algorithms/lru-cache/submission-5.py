class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # DS to store keys and corresponding Nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = node.next
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        self.right.prev = node
        prev.next = node

    def get(self, key: int) -> int: 
        # When we get, we want to retrieve the value
        # But also add the value to the end of the cache
        # We will abstract using methods remove() and insert()
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].val = value
            self.insert(self.cache[key])
            return
        if len(self.cache) == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node        

