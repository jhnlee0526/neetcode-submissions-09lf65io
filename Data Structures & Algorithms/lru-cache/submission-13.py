class ListNode:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

        self.head = None
        self.tail = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}     # {key : node, }
        self.capacity = capacity
        
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.cache:
            foundNode = self.cache[key]
            self._remove(foundNode)
            self._insert(foundNode)
            return foundNode.value
        return -1        


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            foundNode = self.cache[key]
            self._remove(foundNode)

        elif len(self.cache) >= self.capacity:
            oldestNode = self.head.next
            self._remove(oldestNode)
            del self.cache[oldestNode.key]

        newNode = ListNode(key, value)
        self.cache[key] = newNode
        self._insert(newNode)


    def _insert(self, node: ListNode):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node ##
        self.tail.prev = node ##
    

    def _remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
