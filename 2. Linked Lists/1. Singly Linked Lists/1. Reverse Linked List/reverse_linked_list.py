class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        # prev = None
        # curr = 1 -> 2 -> 3 -> None
        while curr:
            # temp = 2 -> 3 -> None
            # temp = 3 -> None
            # temp = None
            temp = curr.next

            # curr.next = None
            # curr.next = 1 -> None
            # curr.next = 2 -> 1 -> None
            curr.next = prev

            # prev = 1 -> None
            # since curr.value = 1 and curr.next = None

            # prev = 2 -> 1 -> None
            # since curr.value = 2 and curr.next = 1 -> None

            # prev = 3 -> 2 -> 1 -> None
            # since curr.value = 3 and curr.next = 2 -> 1 -> None
            prev = curr

            # curr = 2 -> 3 -> None
            # curr = 3 -> None
            # curr = None
            curr = temp
        return prev


def main():
    # Create a linked list 1 -> 2 -> 3
    head = ListNode(1)
    head.next = ListNode(2)
    # next = None by default
    head.next.next = ListNode(3)

    # Initialize the Solution class
    sol = Solution()

    # Reverse the linked list
    reversed_head = sol.reverseList(head)

    # Print the reversed linked list
    curr = reversed_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


if __name__ == "__main__":
    main()
