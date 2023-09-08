class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        # dummy head node
        self.left = ListNode(0)
        # dummy tail node
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val):
        # create a new node with the given value
        node = ListNode(val)

        # prev is the dummy head node
        prev = self.left

        # next is the node currently just after the dummy head
        next = self.left.next

        # link the new node to prev and next
        node.next = next
        node.prev = prev

        # update prev and next nodes to point to the new node
        next.prev = node
        prev.next = node

        # end result (if addAtHead(5) is called)
        # self.left (dummy head) <-> new_node (value: 5) <-> next <-> ...

    def addAtTail(self, val):
        # create a new node with the given value
        node = ListNode(val)

        # prev is the node currently just before the dummy tail
        prev = self.right.prev

        # next is the dummy tail node
        next = self.right

        # link the new node to prev and next
        node.next = next
        node.prev = prev

        # update prev and next nodes to point to the new node
        next.prev = node
        prev.next = node

        # end result (if addAtTail(10) is called)
        # ... <-> prev <-> new_node (value: 10) <-> self.right (dummy tail)

    def addAtIndex(self, index, val):
        # Start at the first actual node, ignoring the dummy head
        next = self.left.next

        # Traverse the list to find the node that should come after the new node
        while next and index > 0:
            next = next.next
            index -= 1

        # If a node exists at the index, proceed to insert the new node before it
        if next and index == 0:
            # Create a new node with the given value
            node = ListNode(val)

            # Identify the node that will come before the new node
            prev = next.prev

            # Link the new node to prev and next
            node.next = next
            node.prev = prev

            # Update prev and next nodes to point to the new node
            next.prev = node
            prev.next = node

        # end result (if addAtIndex(2, 4) is called on a list [1, 3, 5])
        # becomes [1, 3, 4, 5], inserting the node with value 4 at index 2

    def deleteAtIndex(self, index):
        # Start at the first actual node, ignoring the dummy head
        node = self.left.next

        # Traverse the list to find the node at the given index
        while node and index > 0:
            node = node.next
            index -= 1

        # If a node exists at the index and it's not the dummy tail,
        # proceed to delete it
        if node and node != self.right and index == 0:
            # Update the pointers of the surrounding nodes to "skip" the target node,
            # effectively removing it from the list
            node.prev.next = node.next
            node.next.prev = node.prev

        # end result (if deleteAtIndex(2) is called on a list [1, 3, 5, 7])
        # becomes [1, 3, 7], removing the node with value 5 at index 2


def main():
    methods = [
        "MyLinkedList",
        "addAtHead",
        "addAtTail",
        "addAtIndex",
        "get",
        "deleteAtIndex",
        "get",
    ]
    values = [[], [1], [3], [1, 2], [1], [1], [1]]

    obj = None
    outputs = []

    for i, method in enumerate(methods):
        if method == "MyLinkedList":
            obj = MyLinkedList()
            outputs.append(None)
        elif method == "addAtHead":
            obj.addAtHead(values[i][0])
            outputs.append(None)
        elif method == "addAtTail":
            obj.addAtTail(values[i][0])
            outputs.append(None)
        elif method == "addAtIndex":
            obj.addAtIndex(values[i][0], values[i][1])
            outputs.append(None)
        elif method == "get":
            res = obj.get(values[i][0])
            outputs.append(res)
        elif method == "deleteAtIndex":
            obj.deleteAtIndex(values[i][0])
            outputs.append(None)

    print("Outputs:", outputs)


if __name__ == "__main__":
    main()
