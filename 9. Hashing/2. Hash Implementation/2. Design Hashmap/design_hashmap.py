class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        # Assign the key argument to the key attribute
        self.key = key
        # Assign the val argument to the val attribute
        self.val = val
        # Assign the next argument to the next attribute
        self.next = next


class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hashcode(self, key):
        # Return the remainder of key divided by the length of self.map
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        # Get the bucket where the key-value pair should be stored
        cur = self.map[self.hashcode(key)]
        # Traverse the linked list in the bucket
        while cur.next:
            # If the key already exists, update its value
            if cur.next.key == key:
                cur.next.val = value
                return
            # Move to the next node in the linked list
            cur = cur.next
        # If the key doesn't exist, create a new ListNode with the key-value pair and insert it into the list
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # Get the first node in the bucket's linked list
        cur = self.map[self.hashcode(key)].next
        # Traverse the linked list to find the key
        while cur and cur.key != key:
            # Move to the next node in the linked list
            cur = cur.next
        # If the key is found, return its value
        if cur:
            return cur.val
        return -1

    def remove(self, key: int) -> None:
        # Get the bucket where the key-value pair should be stored
        cur = self.map[self.hashcode(key)]
        # Traverse the linked list to find the key
        while cur.next and cur.next.key != key:
            # Move to the next node in the linked list
            cur = cur.next
        # If the key is found, remove it from the linked list
        if cur and cur.next:
            cur.next = cur.next.next


def main():
    commands = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    args = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

    output = []

    for i, command in enumerate(commands):
        if command == "MyHashMap":
            hashMap = MyHashMap()
            output.append(None)
        elif command == "put":
            hashMap.put(args[i][0], args[i][1])
            output.append(None)
        elif command == "get":
            result = hashMap.get(args[i][0])
            output.append(result)
        elif command == "remove":
            hashMap.remove(args[i][0])
            output.append(None)

    print(output)


if __name__ == "__main__":
    main()
