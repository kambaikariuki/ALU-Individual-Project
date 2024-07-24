from functions import *
def main():
    grade_book = GradeBook()
    
    while True:
        print("\n   Hello! \n\nWelcome to the Grade Book App\n")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA for all Students")
        print("5. Calculate Ranking")
        print("6. Search Students by Grade")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            grade_book.add_student()
        elif choice == '2':
            grade_book.add_course()
        elif choice == '3':
            grade_book.register_student_for_course()
        elif choice == '4':
            grade_book.calculate_GPA()
        elif choice == '5':
            grade_book.calculate_ranking()
        elif choice == '6':
            filtered_students = grade_book.search_by_grade()
            print("Students within specified GPA range:")
            for student in filtered_students:
                print(f"{student.names} - GPA: {student.GPA}")
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

student1 = Student('joe@mail.com', 'Joseph', 4.0)
student2 = Student('fredy@mail.com', "Fredy", 3.5)
student3 = Student('kassa@mail.com', 'Kassaz', 3.8)
student4 = Student('maria@mail.com', 'Maria', 3.2)

if __name__ == "__main__":
    main()
