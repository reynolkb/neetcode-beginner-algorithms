class MyHashSet:
    def __init__(self):
        # Initialize an array with a fixed size (for simplicity)
        self.buckets = [[] for _ in range(1000)]

    def getIndex(self, key: int) -> int:
        # Simple hash function to map keys to buckets
        # For example, if key = 1 then 1 % 1000 = 1 since 1 cannot be divided by 1000 giving a remainder of 1
        return key % len(self.buckets)

    def add(self, key: int) -> None:
        # Get the index of the bucket
        index = self.getIndex(key)
        # If key is not already present in the bucket, add it
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        # Get the index of the bucket
        index = self.getIndex(key)
        # If key is present in the bucket, remove it
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        # Get the index of the bucket
        index = self.getIndex(key)
        # Check if key is present in the bucket
        return key in self.buckets[index]


def main():
    results = []
    obj = MyHashSet()
    operations = [
        "MyHashSet",
        "add",
        "add",
        "contains",
        "contains",
        "add",
        "contains",
        "remove",
        "contains",
    ]
    args = [[], [1], [2], [1], [3], [2], [2], [2], [2]]

    for operation, arg in zip(operations, args):
        if operation == "MyHashSet":
            results.append(None)
        elif operation == "add":
            obj.add(arg[0])
            results.append(None)
        elif operation == "remove":
            obj.remove(arg[0])
            results.append(None)
        elif operation == "contains":
            results.append(obj.contains(arg[0]))

    print(results)


if __name__ == "__main__":
    main()
