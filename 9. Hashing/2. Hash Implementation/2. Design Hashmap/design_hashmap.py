class ListNode:
    def __init__(self, key=None, val=None, next=None):
        # Assign the key argument to the key attribute
        self.key = key
        # Assign the val argument to the val attribute
        self.val = val
        # Assign the next argument to the next attribute
        self.next = next


class MyHashMap:
    def __init__(self):
        self.listNodeArr = [ListNode() for i in range(1000)]

    def getIndex(self, key):
        # Return the remainder of key divided by the length of self.map
        # For example, if key = 1 then 1 % 1000 = 1 since 1 cannot be divided by 1000 giving a remainder of 1
        return key % len(self.listNodeArr)

    def put(self, key: int, value: int) -> None:
        # Get the index of the bucket
        index = self.getIndex(key)
        # Get the bucket's head node where the key-value pair should be stored
        cur = self.listNodeArr[index]
        # Traverse the linked list in the bucket
        # Start at cur.next since cur is a dummy node with key = None and val = None
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
        # Get the index of the bucket
        index = self.getIndex(key)
        # Get the first node in the bucket's linked list
        # Start at cur.next since cur is a dummy node
        cur = self.listNodeArr[index].next
        # Traverse the linked list to find the key
        while cur and cur.key != key:
            # Move to the next node in the linked list
            cur = cur.next
        # If the key is found, return its value
        if cur:
            return cur.val
        return -1

    def remove(self, key: int) -> None:
        # Get the index of the bucket
        index = self.getIndex(key)
        # Get the bucket where the key-value pair should be stored
        # Start at cur which is the dummy node since we need to know the node before the one we want to remove
        cur = self.listNodeArr[index]
        # Traverse the linked list to find the key
        while cur.next:
            # If the key of the next node matches the key to be removed
            if cur.next.key == key:
                # Remove the node by updating the next pointer of the current node
                # We do not need to do a `if cur.next.next` since it being None is fine because we want to remove the last node as well
                cur.next = cur.next.next
                return  # Exit the method as the node has been removed
            # Move to the next node in the linked list
            cur = cur.next


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
