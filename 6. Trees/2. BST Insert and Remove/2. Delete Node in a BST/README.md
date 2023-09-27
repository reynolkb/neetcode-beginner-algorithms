# [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

## Description
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

Example 1:\
![Example 1A](example_1a.jpeg)\
Input: `root = [5,3,6,2,4,null,7], key = 3`\
Output: `[5,4,6,2,null,null,7]`\
Explanation:\
```
Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```
![Example 1B](example_1b.jpeg)

Example 2:\
Input: `root = [5,3,6,2,4,null,7], key = 0`\
Output: `[5,3,6,2,4,null,7]`\
Explanation: `The tree does not contain a node with value = 0.`

Example 3:\
Input: `root = [], key = 0`\
Output: `[]`

## Run Command
`poetry run python "6. Trees/2. BST Insert and Remove/2. Delete Node in a BST/delete_node_in_a_bst.py"`