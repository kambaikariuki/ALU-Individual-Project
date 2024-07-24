class Student:
    def __init__(self, email, name, GPA):
        self.email = email
        self.name = name
        self.courses_registered = []
        self.GPA = 0
    
    def calculate_GPA(self):
        if not self.courses_registered:
            return 0.0
        total_credits = 0
        weighted_sum = 0.0
        for course in self.courses_registered:
            total_credits += course.credits
            weighted_sum += course.credits * course.grade_point
        self.GPA = weighted_sum / total_credits if total_credits > 0 else 0.0
    
    def register_for_course(self, course):
        self.courses_registered.append(course)

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade_point = 0.0  # Assuming grade points can be added in future versions if needed

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
    
    def add_student(self):
        name = input("Enter student's name : ")
        email = input("Enter student's email: ")
        student = Student(email, name)
        self.student_list.append(student)
        print(f"{student.name} has been added succesfully!")
    
    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter trimester: ")
        credits = int(input("Enter credits: "))
        course = Course(name, trimester, credits)
        self.course_list.append(course)
    
    def register_student_for_course(self):
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
        for student in self.student_list:
            student.calculate_GPA()
            print(f"Student {student.name} has GPA: {student.GPA}")
    
    def calculate_ranking(self):
        self.student_list.sort(key=lambda x: x.GPA, reverse=True)
        print("Student Ranking:")
        for i, student in enumerate(self.student_list, start=1):
            print(f"{i}. {student.name} - GPA: {student.GPA}")
    
    def search_by_grade(self):
        min_gpa = float(input("Enter minimum GPA: "))
        max_gpa = float(input("Enter maximum GPA: "))
        
        filtered_students = [student for student in self.student_list if min_gpa <= student.GPA <= max_gpa]
        return filtered_students
    