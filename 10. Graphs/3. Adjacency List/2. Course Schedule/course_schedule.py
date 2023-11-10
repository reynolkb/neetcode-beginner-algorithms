from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # Populate the preMap with the prerequisites for each course.
        # You have to take the pre before you take the crs
        for crs, pre in prerequisites:
            if crs >= numCourses or pre >= numCourses:
                continue
            preMap[crs].append(pre)

        # Set to keep track of courses currently being visited in DFS.
        visiting = set()

        # Define a depth-first search (DFS) function to check if a course can be completed.
        def dfs(crs):
            # If the current course is already being visited, it means there's a cycle, so return False.
            if crs in visiting:
                return False
            # If there are no prerequisites for the current course, it can be completed, so return True.
            if preMap[crs] == []:
                return True

            # Add the current course to the visiting set.
            visiting.add(crs)
            # Iterate over the prerequisites for the current course.
            for pre in preMap[crs]:
                # If any prerequisite course cannot be completed, return False.
                if not dfs(pre):
                    return False
            # Remove the current course from the visiting set once all prerequisites are visited.
            visiting.remove(crs)
            # Clear the prerequisites for the current course to avoid reprocessing in future DFS calls.
            preMap[crs] = []
            # Return True as the current course can be completed.
            return True

        # Iterate over all courses and use DFS to check if each can be completed.
        for c in range(numCourses):
            if not dfs(c):
                return False
        # If all courses can be completed, return True.
        return True


def main():
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print("Output:", result);


if __name__ == "__main__":
    main()
