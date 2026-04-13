'''
[Doubly Linked List] Optinaml!
- get(key) → O(1)
    Lookup in the hash map (self.cache[key]) is O(1).
    Removing and reinserting the node (_remove() & _insert()) are both O(1).
    Total: O(1).

- put(key, value) → O(1)
    Checking if key exists in hash map is O(1).
    Removing LRU node (if needed) is O(1).
    Inserting a new node into the linked list is O(1).
    Total: O(1).

- Final Time Complexity: O(1) for both get()
'''

# Define a node class for the doubly linked list
class Node:
    def __init__(self, key, val):
        self.key = key  # Stores the cache key
        self.value = val  # Stores the associated cache value
        self.prev = None  # Pointer to previous node (for efficient removal)
        self.next = None  


class LRUCache:

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.
        - Uses a HashMap (`self.cache`) for O(1) lookup.
        - Uses a doubly linked list (`self.head` <-> `self.tail`) for efficient ordering.
        """
        self.capacity = capacity  # Maximum number of items in the cache
        self.cache = {}  # HashMap to store key-to-node mappings
        
        self.head = Node(0, 0)  # Dummy head node (marks the front)
        self.tail = Node(0, 0)  # Dummy tail node (marks the end)
        self.head.next = self.tail  # Initialize doubly linked list
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        """
        Retrieves the value associated with `key`.
        - If found, moves the node to the end (most recently used).
        - If not found, returns `-1`.
        """
        if key in self.cache:
            node = self.cache[key]  # Get the node from HashMap
            self._remove(node)  # Move it to most recently used position
            self._insert(node)
            return node.value  # Return the stored value
        return -1  # Key not found


    def put(self, key: int, value: int) -> None:
        """
        Inserts a key-value pair into the cache.
        - If key already exists, update the value and move it to the end.
        - If cache is full, evict the least recently used item before adding new data.
        """
        if key in self.cache:
            self._remove(self.cache[key])  # Remove the old node

        elif len(self.cache) >= self.capacity:
            # Remove least recently used (LRU) node, which is right after `head`
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]  # Remove key from HashMap

        # Insert the new key-value pair at the end (most recently used)
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)


    def _remove(self, node: Node):
        """
        Removes a node from the linked list.
        - Adjusts `prev` and `next` pointers to exclude the given node.
        - Used when updating access order or evicting LRU items.
        """
        node.prev.next = node.next
        node.next.prev = node.prev


    def _insert(self, node: Node):
        """
        Inserts a node at the end (most recently used).
        - Places the node right before the tail.
        - Helps maintain LRU order with O(1) operations.
        """
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
