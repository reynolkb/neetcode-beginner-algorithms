from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # check if lists is None or empty
        if not lists:
            return None

        # Main loop to repeatedly merge pairs of linked-lists until only one remains
        while len(lists) > 1:
            # Initialize an empty list to store intermediate merged linked-lists
            mergedLists = []

            # Loop through 'lists' two at a time (0, 1), (2, 3), etc.
            for i in range(0, len(lists), 2):
                # Get the two linked-lists to be merged; if there's only one list left, the second will be None
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Merge the two lists and add the resulting merged list to 'mergedLists'
                mergedLists.append(self.mergeList(l1, l2))

            # Replace 'lists' with 'mergedLists' for the next iteration
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        # set dummy and node to the same instance of ListNode
        dummy = node = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 or l2
        # point to the first value, not the base value of 0
        return dummy.next


def main():
    # Create first linked list: 1 -> 4 -> 5
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)

    # Create second linked list: 1 -> 3 -> 4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # Create third linked list: 2 -> 6
    list3 = ListNode(2)
    list3.next = ListNode(6)

    # Create a Solution object
    sol = Solution()

    # Call the mergeKLists function with the created lists
    merged_list = sol.mergeKLists([list1, list2, list3])

    # Print the merged list
    curr = merged_list
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


if __name__ == "__main__":
    main()
