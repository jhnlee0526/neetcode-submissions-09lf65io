class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key: Node,}
        
        # set up the doubly linked list
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
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
        if key in self.cache:
            existingNode = self.cache[key]
            self._remove(existingNode)

        elif len(self.cache) >= self.capacity:
            oldestNode = self.head.next
            self._remove(oldestNode)
            del self.cache[oldestNode.key]
        
        newNode = ListNode(key, value)
        self._insert(newNode)
        self.cache[key] = newNode
            

    def _remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev


    def _insert(self, node: ListNode):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node