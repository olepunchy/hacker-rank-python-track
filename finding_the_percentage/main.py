def print_average(marks, name):

    student_marks = marks[name]
    total = 0.0

    for mark in student_marks:
        total += mark

    total = total / len(student_marks)

    print(f"{total:.2f}")


if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    print_average(student_marks, query_name)
