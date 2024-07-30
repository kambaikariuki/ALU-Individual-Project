from functions import *
def main():
    grade_book = GradeBook()
    
    while True:
        print("\nWelcome to the Grade Book Application")
        print("\n       Menu")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA for all Students")
        print("5. Update student GPA")
        print("6. Calculate Ranking")
        print("7. Search Students by Grade")
        print("8. Save Students to file")
        print("9. Save Courses to file")
        print("10. Exit")
        
        
        
        choice = input("\n\nEnter your choice: ")
        
        if choice == '1':
            grade_book.add_student()
            
        elif choice == '2':
            grade_book.add_course()
            
        elif choice == '3':
            grade_book.register_student_for_course()

        elif choice == '4':
            grade_book.calculate_GPA()
        
        elif choice == '5':
            email = input("Enter student's email to update GPA: ")
            grade_book.update_student_gpa(email)
        
        elif choice == '6':
            grade_book.calculate_ranking()
        
        elif choice == '7':
            filtered_students = grade_book.search_by_grade()
            print("Students within specified GPA range:")
            for student in filtered_students:
                print(f"{student.name} - GPA: {student.GPA:.2f}")
        
        elif choice == '8':
            filename = input("Enter filename to save students (e.g., students.csv): ")
            grade_book.save_students_to_csv(filename)
        
        elif choice == '9':
            filename = input("Enter filename to save courses (e.g., courses.csv): ")
            grade_book.save_courses_to_csv(filename)
        
        elif choice == '10':
            print("Exiting program.")
            break

        
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")

if __name__ == "__main__":
    main()
