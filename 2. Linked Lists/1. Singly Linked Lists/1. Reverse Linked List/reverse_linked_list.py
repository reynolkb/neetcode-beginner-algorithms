class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head

        # prev = None
        # cur = 1 -> 2 -> 3 -> None
        while cur:
            # temp = 2 -> 3 -> None
            # temp = 3 -> None
            # temp = None
            temp = cur.next

            # cur.next = None
            # cur.next = 1 -> None
            # cur.next = 2 -> 1 -> None
            cur.next = prev

            # prev = 1 -> None
            # since cur.value = 1 and cur.next = None

            # prev = 2 -> 1 -> None
            # since cur.value = 2 and cur.next = 1 -> None

            # prev = 3 -> 2 -> 1 -> None
            # since cur.value = 3 and cur.next = 2 -> 1 -> None
            prev = cur

            # cur = 2 -> 3 -> None
            # cur = 3 -> None
            # cur = None
            cur = temp
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
    cur = reversed_head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")


if __name__ == "__main__":
    main()
