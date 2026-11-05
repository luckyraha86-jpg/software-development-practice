from tracker import add_student, show_all_records, search_student, average

def main():
    while True:
        print("========================================")
        print("========================================")
        print("============STUDENTS-TRACKER============")
        print("========================================")
        print("========================================")
        print("1. Show all records")
        print("2. Check student marks")
        print("3. Add new student")
        print("4. Show all averages")
        print("5. Exit")
        try:
            choice = int(input("Choose the option you want to do: "))
        except ValueError:
            print("ony numbers allowed between 1-5")
            continue

        if choice == 1:
            records = show_all_records()
            print("All records of students")
            for index, record in enumerate(records, start=1):
                print(f"{index}.     {record['name']}     {record['subject']}")

        elif choice == 2:
            try:
                roll = int(input("Enter the roll number of the student you want to check marks: "))
            except ValueError:
                print("It must be an integer")
                continue

            student = search_student(roll)
            if len(student) > 0:
                print(f"The student with roll number {roll}:")
                print(f"Name : {student['name']}")
                print(f"Roll number : {student['roll']}")
                print(f"Subject marks : {student['subject_marks']}")
                print(f"Total marks out of 100 : {student['total_marks']}")
            else:
                print(f"The student with roll number {roll} not found in the database")

        elif choice == 3:
            name = input("Enter the student name: ")
            try:
                roll = int(input("Enter the roll number: "))
            except ValueError:
                print("It must be an integer")
                continue

            try:
                subject = list(map(int, input("Enter the marks of the student: ").split()))
            except:
                print("It must be an integer")
                continue

            add_student(name, roll, subject)

        elif choice == 4:
            avgs = average()
            for index, avg in enumerate(avgs, start=1):
                print(f"{index}.    {avg['name']}    {avg['avg']}")

        elif choice == 5:
            print("Student tracker system successfully shutdown bye bye take care!")
            break

        else:
            print("Invalid input choose numbers between 1-5")

if __name__ == "__main__":
    main()