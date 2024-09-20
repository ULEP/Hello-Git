import os


class Student:
    def __init__(self, name, age, gender, id, hobbies, gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id
        self.hobbies = hobbies
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, ID: {self.id}, Hobbies: {self.hobbies}, GPA: {self.gpa}"

    def save_to_file(students, filename="students.txt"):
        with open(filename, "w") as file:
            for student in students:
                file.write(
                    f"{student.name},{student.age},{student.gender},{student.id},{student.hobbies},{student.gpa}\n")


    def load_from_file(filename="students.txt"):
        students = []
        if not os.path.exists(filename):
            return students
        with open(filename, "r") as file:
            for line in file:
                name, age, gender, id, hobbies, gpa = line.strip().split(',')
                students.append(Student(name, int(age), gender, id, hobbies, float(gpa)))
        return students


    def sort_by_id(students):
        return sorted(students, key=lambda x: x.id)


    def sort_by_gpa(students):
        return sorted(students, key=lambda x: x.gpa, reverse=True)


def main():
    students = Student.load_from_file()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student by ID")
        print("3. Sort Students by ID")
        print("4. Sort Students by GPA")
        print("5. View All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            id = input("Enter ID: ")
            hobbies = input("Enter hobbies (comma separated): ")
            gpa = float(input("Enter GPA: "))
            students.append(Student(name, age, gender, id, hobbies, gpa))
            Student.save_to_file(students)

        elif choice == '2':
            id_to_delete = input("Enter ID to delete: ")
            students = [student for student in students if student.id != id_to_delete]
            Student.save_to_file(students)

        elif choice == '3':
            sorted_by_id = Student.sort_by_id(students)
            for student in sorted_by_id:
                print(student)

        elif choice == '4':
            sorted_by_gpa = Student.sort_by_gpa(students)
            for student in sorted_by_gpa:
                print(student)

        elif choice == '5':
            for student in students:
                print(student)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()