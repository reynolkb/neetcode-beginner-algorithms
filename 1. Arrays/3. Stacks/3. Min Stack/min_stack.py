class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


def main():
    methods = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    values = [[], [-2], [0], [-3], [], [], [], []]

    minStack = None
    outputs = []

    for i, method in enumerate(methods):
        if method == "MinStack":
            minStack = MinStack()
            outputs.append(None)
        elif method == "push":
            minStack.push(values[i][0])
            outputs.append(None)
        elif method == "pop":
            minStack.pop()
            outputs.append(None)
        elif method == "top":
            outputs.append(minStack.top())
        elif method == "getMin":
            outputs.append(minStack.getMin())

    print("Outputs:", outputs)


if __name__ == "__main__":
    main()
