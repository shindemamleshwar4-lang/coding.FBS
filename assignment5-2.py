num_student = int(input("Enter number of student:"))

total_percentage_sum = 0

for i in range (1, num_student + 1 ):
    print(f"Enter marks for student{i}")

    student_marks_sum = 0

    for j in range (1, 6):
        mark = float(input(f"Enter marks for subject {j}:"))
        student_marks_sum += mark

        percentage = ( student_marks_sum / 500)*100

        total_percentage_sum += percentage

        print(f"Student {i} percentage: {percentage:.2f}%")
        average_percentage = total_percentage_sum / num_student

        print(f"\n===final class_average ===")
        print(f"average percentage of all student:{average_percentage:.2f}%")


