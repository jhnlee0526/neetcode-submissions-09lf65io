class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.head = None
        self.tail = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key: ListNode, }

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            selectedNode = self.cache[key]
            self._remove(selectedNode)
            self._insert(selectedNode)
            return selectedNode.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            selectedNode = self.cache[key]
            self._remove(selectedNode)
        
        elif len(self.cache) >= self.capacity:
            oldestNode = self.head.next
            self._remove(oldestNode)
            del self.cache[oldestNode.key]
        
        newNode = ListNode(key, value)
        self.cache[key] = newNode
        self._insert(newNode)


    def _remove(self, node: ListNode):
        node.next.prev = node.prev
        node.prev.next = node.next


    def _insert(self, node: ListNode):
        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node




