class Node:
    def __init__(self, key, val):
        # Store the key/value pair in the node
        self.key, self.val = key, val
        # Initialize previous and next pointers to None
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # Store the capacity of the cache
        self.cap = capacity
        # Initialize an empty dictionary to store key-node pairs
        self.cache = {}

        # Create dummy nodes for the left and right ends of the doubly linked list
        self.left, self.right = Node(0, 0), Node(0, 0)
        # Connect the dummy nodes to each other
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # Get the previous and next nodes
        prev, nxt = node.prev, node.next
        # Update their pointers to bypass the current node
        prev.next, nxt.prev = (
            nxt,
            prev,
        )

    # Method to insert a node at the right end of the doubly linked list
    def insert(self, node):
        # Get the node before the right dummy node
        prev, nxt = (
            self.right.prev,
            self.right,
        )
        # Update their pointers to include the new node
        prev.next = nxt.prev = node
        # Update the new node's pointers
        node.next, node.prev = nxt, prev

    # Method to get the value associated with a key
    def get(self, key: int) -> int:
        # Check if the key is in the cache
        if key in self.cache:
            # If yes, remove the node from its current position
            self.remove(self.cache[key])
            # Reinsert the node at the right end using custom class insert method
            self.insert(self.cache[key])
            # Return the value of the node
            return self.cache[key].val
        # If the key is not in the cache, return -1
        return -1

    # Method to add a key-value pair or update the value of an existing key
    def put(self, key: int, value: int) -> None:
        # Check if the key is already in the cache
        if key in self.cache:
            # If yes, remove the node from its current position
            self.remove(self.cache[key])
        # Create a new node or overwrite the existing node
        self.cache[key] = Node(key, value)
        # Insert the node at the right end
        self.insert(self.cache[key])

        # If the cache has exceeded its capacity,
        if len(self.cache) > self.cap:
            # Get the least recently used node (the node after the left dummy node)
            lru = self.left.next
            # Remove the least recently used node from the list
            self.remove(lru)
            # Remove the least recently used node from the cache
            del self.cache[lru.key]

    """ 
    The left end of the list represents the least recently used items, while the right end represents the most recently used items (put or get).
    """


def process_operations(operations, values):
    output = []
    lru_cache_instance = None
    for operation, value in zip(operations, values):
        if operation == "LRUCache":
            lru_cache_instance = LRUCache(value[0])
            output.append(None)
        elif operation == "put":
            lru_cache_instance.put(value[0], value[1])
            output.append(None)
        elif operation == "get":
            result = lru_cache_instance.get(value[0])
            output.append(result)
    return output


def main():
    operations = [
        "LRUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    output = process_operations(operations, values)
    print(output)


if __name__ == "__main__":
    main()
