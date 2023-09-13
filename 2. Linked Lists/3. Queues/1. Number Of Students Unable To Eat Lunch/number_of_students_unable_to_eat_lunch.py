from collections import deque


class Solution(object):
    def countStudents(self, students, sandwiches):
        students = deque(students)
        sandwiches = deque(sandwiches)

        # Currnet count of students who cannot eat
        count = 0

        while len(students) > 0:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                # Reset count to 0 since a student ate
                count = 0
            else:
                # Send the student to the back of the queue
                students.rotate(-1)
                count += 1

            # If count becomes equal to the length of the students queue,
            # it means no one can eat the top sandwich
            if count == len(students):
                break

        return len(students)


def main():
    sol = Solution()
    print(sol.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))  # Output should be 0


if __name__ == "__main__":
    main()
