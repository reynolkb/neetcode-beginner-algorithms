class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # set dummy and node to the same instance of ListNode
        dummy = node = ListNode()

        while list1 and list2:
            # first iteration
            # list1 = 1 -> 2 -> 4 -> None
            # list2 = 1 -> 3 -> 4 -> None

            # second iteration
            # list1 = 1 -> 2 -> 4 -> None
            # list2 = 3 -> 4 -> None

            # third iteration
            # list1 = 2 -> 4 -> None
            # list2 = 3 -> 4 -> None

            # fourth iteration
            # list1 = 4 -> None
            # list2 = 3 -> 4 -> None

            # fifth iteration
            # list1 = 4 -> None
            # list2 = 4 -> None
            if list1.val < list2.val:
                # second iteration
                # node.next = 1 -> 2 -> 4 -> None

                # third iteration
                # node.next = 2 -> 4 -> None
                node.next = list1

                # second iteration
                # list1 = 2 -> 4 -> None

                # third iteration
                # list1 = 4 -> None
                list1 = list1.next
            else:
                # first iteration
                # node.next = 1 -> 3 -> 4 -> None

                # fourth iteration
                # node.next = 3 -> 4 -> None

                # fifth iteration
                # node.next = 4 -> None
                node.next = list2

                # first iteration
                # list2 = 3 -> 4 -> None

                # fourth iteration
                # list2 = 4 -> None

                # fifth iteration
                # list2 = None
                list2 = list2.next
            # first iteration
            # node = 1

            # second iteration
            # node = 1 -> 1

            # third iteration
            # node = 1 -> 1 -> 2

            # fourth iteration
            # node = 1 -> 1 -> 2 -> 3

            # fifth iteration
            # node = 1 -> 1 -> 2 -> 3 -> 4
            node = node.next

        # node.next = 4 -> None
        node.next = list1 or list2

        # point to the first value, not the base value of 0
        return dummy.next


def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    sol = Solution()

    merged_list = sol.mergeTwoLists(list1, list2)

    curr = merged_list
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


if __name__ == "__main__":
    main()
