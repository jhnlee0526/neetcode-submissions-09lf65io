class LRUCache:
    '''
    [Brute Force] Using List []
    The implementation uses a list-based approach for the LRU cache.
        - get(key):
            Search for key in the list: O(n)
            Remove and reinsert at end: O(n) (because pop(i) shifts elements)
            Overall: O(n)

        - put(key, value):
            Search for existing key: O(n)
            Remove and reinsert at end: O(n)
            Removing least recently used element (pop(0)) shifts all elements: O(n)
            Overall: O(n)

        - Since both get() and put() involve searching and shifting elements in a list, the worst-case time complexity is O(n) per operation.
    '''

    def __init__(self, capacity: int):
        self.cache = []  # Stores key-value pairs
        self.capacity = capacity  # Defines max size of cache


    def get(self, key: int) -> int:
        for i in range(len(self.cache)):  # Loop through cache
            if self.cache[i][0] == key:  # Found matching key
                tmp = self.cache.pop(i)  # Remove from list (LRU behavior)
                self.cache.append(tmp)  # * Reinsert at end (recently used)
                return tmp[1]  # Return value

        return -1  # Key not found
        

    def put(self, key: int, value: int) -> None:
        ## Search for existing key
        for i in range(len(self.cache)):  
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)  # Remove existing item
                tmp[1] = value  # * Update value
                self.cache.append(tmp)  # * Reinsert at end
                return

        ## When there is no existing key
        if self.capacity == len(self.cache):  # If cache is full, remove LRU
            self.cache.pop(0)  # Remove first item (Least Recently Used)

        self.cache.append([key, value])  # Insert new item
                
