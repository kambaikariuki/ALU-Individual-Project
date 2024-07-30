import csv

class Student:
    '''Represents a student in the Grade Book system.'''

    def __init__(self, email, name):
        """Initialization of student class"""
        self.email = email
        self.name = name
        self.courses_registered = []
        self.GPA = 0.0
    
    def calculate_GPA(self):
        """
        Method to calculate GPA
        """
        
        if not self.courses_registered:
            return 0.0
        total_credits = 0
        weighted_sum = 0.0
        for course in self.courses_registered:
            total_credits += course.credits
            weighted_sum += course.credits * course.grade_point
        self.GPA = weighted_sum / total_credits if total_credits > 0 else 0.0
    
    def register_for_course(self, course):
        """
        Register a student for a course
        """
        self.courses_registered.append(course)

class Course:
    def __init__(self, name, trimester, credits):
        """Initialization of student class"""
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade_point = 0.0  # Placeholder 

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
    
    def add_student(self):
        """
        Add a new student
        """


        name = input("Enter student's name: ")
        email = input("Enter student's email: ")
        student = Student(email, name)
        self.student_list.append(student)
        print(f"Student {student.name} has been added successfully!")
    
    def add_course(self):
        """
        Adds a new course
        """

        name = input("Enter course name: ")
        trimester = input("Enter trimester: ")
        credits = int(input("Enter credits: "))
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        print(f"Course {course.name} has been added successfully!")
    
    def register_student_for_course(self):
        """
        Registers the student for a new course.
        """

        email = input("Enter student's email: ")
        course_name = input("Enter course name: ")
        
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        
        if student and course:
            student.register_for_course(course)
            print(f"Student {student.name} registered for course {course.name}.")
        else:
            print("Student or course not found.")
    
    def calculate_GPA(self):
        """
        Calculates the GPA of the student based on the registered courses.
        """

        for student in self.student_list:
            student.calculate_GPA()
            print(f"Student {student.name} has GPA: {student.GPA:.2f}")
    
    def calculate_ranking(self):
        """
        Sorts and prints students by GPA in descending order.
        """

        self.student_list.sort(key=lambda x: x.GPA, reverse=True)
        print("Student Ranking:")
        for i, student in enumerate(self.student_list, start=1):
            print(f"{i}. {student.name} - GPA: {student.GPA:.2f}")
    
    def search_by_grade(self):
        """
        Filters students by GPA range.
        """


        min_gpa = float(input("Enter minimum GPA: "))
        max_gpa = float(input("Enter maximum GPA: "))
        
        filtered_students = [student for student in self.student_list if min_gpa <= student.GPA <= max_gpa]
        return filtered_students
    
    def save_students_to_csv(self, filename):
        """
        Saves student data to a CSV file.
        """

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            for student in self.student_list:
                writer.writerow([student.email, student.name, ', '.join(course.name for course in student.courses_registered), student.GPA])
        print("Student data has been saved to CSV successfully!")
    
    
    def save_courses_to_csv(self, filename):
        """
        Saves courses data to a CSV file.
        """

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            for course in self.course_list:
                writer.writerow([course.name, course.trimester, course.credits])
        print("Course data has been saved to CSV successfully!")
    def load_students_from_csv(self, filename):
        """
        Loads student data from a CSV file.
        """
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    email, name, courses_str, gpa_str = row
                    student = Student(email, name)
                    student.GPA = float(gpa_str)
                    # Handle registered courses
                    if courses_str:
                        course_names = courses_str.split(', ')
                        for course_name in course_names:
                            course = next((c for c in self.course_list if c.name == course_name), None)
                            if course:
                                student.register_for_course(course)
                    self.student_list.append(student)
            print("Student data has been loaded from CSV successfully!")
        except IOError:
            print(f"Error: Unable to read file {filename}.")
        except ValueError:
            print("Error: Data format in CSV file is incorrect.")
    
    def load_courses_from_csv(self, filename):
        """
        Loads course data from a CSV file.
        """
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, trimester, credits_str = row
                    try:
                        credits = int(credits_str)
                    except ValueError:
                        print(f"Invalid data for course credits: {credits_str}. Skipping row.")
                        continue
                    course = Course(name, trimester, credits)
                    self.course_list.append(course)
            print("Course data has been loaded from CSV successfully!")
        except IOError:
            print(f"Error: Unable to read file {filename}.")
        except ValueError:
            print("Error: Data format in CSV file is incorrect.")
    
    def update_student_gpa(self, email):
        """
        Updates the GPA for a specific student based on user input.
        """
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            while True:
                try:
                    new_gpa = float(input(f"Enter new GPA for {student.name} (current GPA: {student.GPA:.2f}): "))
                    if 0.0 <= new_gpa <= 4.0:  # Assuming GPA is on a 0.0 to 4.0 scale
                        student.GPA = new_gpa
                        print(f"Student {student.name}'s GPA has been updated to {student.GPA:.2f}.")
                        break
                    else:
                        print("Error: GPA must be between 0.0 and 4.0. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value for GPA.")
        else:
            print(f"No student found with email {email}.")