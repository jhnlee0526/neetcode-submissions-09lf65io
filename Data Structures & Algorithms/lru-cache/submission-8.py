class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # {key: Node, }
        self.capacity = capacity
        # set up doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            selectedNode = self.cache[key]
            self._remove(selectedNode)
            self._insert(selectedNode)
            return selectedNode.val
        return -1        


    def put(self, key: int, value: int) -> None:
        if key in self.cache: # remove existing node in cache
            existingNode = self.cache[key]
            self._remove(existingNode)
        elif len(self.cache) >= self.capacity: # remove the oldest node in the cache & list
            oldestNode = self.head.next
            self._remove(oldestNode) # remove from list
            del self.cache[oldestNode.key] # delete from cache
        # insert the new node to cache & list
        newNode = Node(key, value)
        self._insert(newNode) # add to list
        self.cache[key] = newNode # add to cache


    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    

    def _insert(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node


