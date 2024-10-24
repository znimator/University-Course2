def countExcellentStudents(exam_results):
    count = 0
    for student in exam_results:
        marks = student.split()[1:]
        if all(mark == '5' for mark in marks):
            count += 1
    return count

n = int(input())
exam_results = []
for _ in range(n):
    exam_results.append(input())
print(countExcellentStudents(exam_results))