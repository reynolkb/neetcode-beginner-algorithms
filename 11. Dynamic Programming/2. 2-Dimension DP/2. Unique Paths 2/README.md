# [Unique Paths 2](https://leetcode.com/problems/unique-paths-ii/)

## Description

You are given an `m x n` integer array `grid`. There is a robot initially located at the top-left corner (
i.e., `grid[0][0]`).
The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or
right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include any
square
that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

Example 1:\
![Example 1](example_1.jpeg)\
Input: `obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]`\
Output: `2`\
Explanation:\

```
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

Example 2:\
![Example 2](example_2.jpeg)\
Input: `obstacleGrid = [[0,1],[0,0]]`\
Output: `1`\
Explanation:

## Run Command

`poetry run python "11. Dynamic Programming/2. 2-Dimension DP/2. Unique Paths 2/unique_paths_2.py"`
