# [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

## Description
You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:\
![Example 1A](example_1a.jpeg)\
Input: `root = [4,2,7,1,3], val = 5`\
Output: `[4,2,7,1,3,5]`\
Explanation: `Another accepted tree is:`\
![Example 1B](example_1b.jpeg)

Example 2:\
Input: `root = [40,20,60,10,30,50,70], val = 25`\
Output: `[40,20,60,10,30,50,70,null,null,25]`

Example 3:\
Input: `root = [4,2,7,1,3,null,null,null,null,null,null], val = 5`\
Output: `[4,2,7,1,3,5]`

## Run Command
`poetry run python "6. Trees/2. BST Insert and Remove/1. Insert into a Binary Search Tree/insert_into_a_binary_search_tree.py"`