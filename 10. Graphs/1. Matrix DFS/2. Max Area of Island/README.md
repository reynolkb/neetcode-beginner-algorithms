# [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

## Description
You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in `grid`. If there is no island, return `0`.

Example 1:\
![Example 1](example_1.jpeg)\
Input:\
```
grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
```
Output:`6`\
Explanation: `The answer is not 11, because the island must be connected 4-directionally.`

Example 2:\
Input:`grid = [[0,0,0,0,0,0,0,0]]`
Output:`0`

## Run Command
`poetry run python "10. Graphs/1. Matrix DFS/2. Max Area of Island/max_area_of_island.py"`