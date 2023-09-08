class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    # O(1)
    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    # O(n)
    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    # O(n)
    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val


def main():
    methods = [
        "BrowserHistory",
        "visit",
        "visit",
        "visit",
        "back",
        "back",
        "forward",
        "visit",
        "forward",
        "back",
        "back",
    ]
    values = [
        ["leetcode.com"],
        ["google.com"],
        ["facebook.com"],
        ["youtube.com"],
        [1],
        [1],
        [1],
        ["linkedin.com"],
        [2],
        [2],
        [7],
    ]

    obj = None
    outputs = []

    for i, method in enumerate(methods):
        if method == "BrowserHistory":
            obj = BrowserHistory(values[i][0])
            outputs.append(None)
        elif method == "visit":
            obj.visit(values[i][0])
            outputs.append(None)
        elif method == "back":
            res = obj.back(values[i][0])
            outputs.append(res)
        elif method == "forward":
            res = obj.forward(values[i][0])
            outputs.append(res)

    print("Outputs:", outputs)


if __name__ == "__main__":
    main()
