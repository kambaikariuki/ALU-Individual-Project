from functions import *
def main():
    grade_book = GradeBook()
    
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA for all Students")
        print("5. Calculate Ranking")
        print("6. Search Students by Grade")
        print("7. Save Students to file")
        print("8. Save Courses to file")
        print("9. Exit")
        
        
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
                print(f"{student.name} - GPA: {student.GPA:.2f}")
        
        elif choice == '7':
            filename = input("Enter filename to save students (e.g., students.csv): ")
            grade_book.save_students_to_csv(filename)
        
        elif choice == '8':
            filename = input("Enter filename to save courses (e.g., courses.csv): ")
            grade_book.save_courses_to_csv(filename)
        
        elif choice == '9':
            print("Exiting program.")
            break
         
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()
