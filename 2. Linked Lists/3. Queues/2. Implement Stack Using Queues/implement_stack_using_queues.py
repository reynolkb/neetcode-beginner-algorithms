from collections import deque


class MyStack(object):
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        # Iterate through the queue until the last element.
        # We have to do last-in-first-out and only pop from the front. Therefore, we are returning rotating the deque so the last element is the first on the top so we can remove it.
        for i in range(len(self.q) - 1):
            """
            Remove the front element and push it to the back.
            Calling push function above, essentially doing self.q.append(self.q.popleft())
            """
            self.push(self.q.popleft())
        # Remove and return the last element which is now at the front.
        return self.q.popleft()

    def top(self):
        # Iterate through the queue until the last element.
        for i in range(len(self.q) - 1):
            # Remove the front element and push it to the back.
            self.push(self.q.popleft())
        # Store the last element (now at the front) in 'res'.
        res = self.q[0]
        # Move the last element back to its original position.
        self.push(self.q.popleft())
        # Return the stored last element.
        return res

    def empty(self):
        return len(self.q) == 0


def main():
    methods = ["MyStack", "push", "push", "top", "pop", "empty"]
    values = [[], [1], [2], [], [], []]

    obj = None
    outputs = []

    for i, method in enumerate(methods):
        if method == "MyStack":
            obj = MyStack()
            outputs.append(None)
        elif method == "push":
            obj.push(values[i][0])
            outputs.append(None)
        elif method == "pop":
            outputs.append(obj.pop())
        elif method == "top":
            outputs.append(obj.top())
        elif method == "empty":
            outputs.append(obj.empty())

    print("Outputs:", outputs)


if __name__ == "__main__":
    main()
