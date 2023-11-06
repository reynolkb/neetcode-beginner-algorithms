from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # Create a dictionary to map original nodes to their clones.
        oldToNew = {}

        def dfs(node):
            # If the node has already been cloned, return the clone.
            if node in oldToNew:
                return oldToNew[node]

            # Create a new node with the same value as the original node.
            copy = Node(node.val)
            # Map the original node to its clone.
            oldToNew[node] = copy
            # Iterate through the neighbors of the original node.
            for nei in node.neighbors:
                # Recursively clone the neighbors and add them to the clone's neighbors list.
                copy.neighbors.append(dfs(nei))
            # Return the clone of the node.
            return copy

        # If the input node is not None, start cloning from the input node. Otherwise, return None.
        return dfs(node) if node else None


def graph_to_adj_list(node):
    visited = {}

    def dfs(node):
        if node is None:
            return
        if node.val in visited:
            return

        visited[node.val] = []

        for neighbor in node.neighbors:
            visited[node.val].append(neighbor.val)
            dfs(neighbor)

    dfs(node)

    return [visited[key] for key in sorted(visited)]


def main():
    node_mapping = {val: Node(val) for val in range(1, 5)}
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

    for idx, neighbors in enumerate(adjList, 1):
        node_mapping[idx].neighbors = [node_mapping[neigh] for neigh in neighbors]

    solution = Solution()
    cloned_node = solution.cloneGraph(node_mapping[1])
    cloned_adj_list = graph_to_adj_list(cloned_node)
    print("Output:", cloned_adj_list)


if __name__ == "__main__":
    main()
