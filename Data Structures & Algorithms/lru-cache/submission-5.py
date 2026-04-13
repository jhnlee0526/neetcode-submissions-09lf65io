class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Node(key, val)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # move node to the most recently used position
            self._remove(node)
            self._insert(node)
            return node.value
        
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key]) # remove old node
        elif len(self.cache) >= self.capacity:
            leastRecent = self.head.next
            self._remove(leastRecent)
            del self.cache[leastRecent.key]
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self._insert(newNode)

    
    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def _insert(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
