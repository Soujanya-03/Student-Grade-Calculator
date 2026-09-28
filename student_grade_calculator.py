
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
def main():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)
    subjects = [
        "Python",
        "Data Science",
        "Mathematics",
        "Database",
        "Communication"
    ]

    marks = []
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter marks between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    if all(mark >= 35 for mark in marks):
        result = "PASS"
    else:
        result = "FAIL"

    print("\n" + "=" * 40)
    print("             RESULT")
    print("=" * 40)

    for subject, mark in zip(subjects, marks):
        print(f"{subject:<20}: {mark:.2f}")

    print("-" * 40)
    print(f"{'Total Marks':<20}: {total:.2f}/500")
    print(f"{'Percentage':<20}: {percentage:.2f}%")
    print(f"{'Grade':<20}: {grade}")
    print(f"{'Result':<20}: {result}")
    print("=" * 40)
if __name__ == "__main__":
    main()
