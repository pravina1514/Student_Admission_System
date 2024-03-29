
# Importing classes
from userlogin import Authenticator
from students_reporting import StudentOperations

# Creating objects
user_authenticator = Authenticator()
student_operations = StudentOperations()

# Task-1: Displaying a welcoming message
user_authenticator.display_greeting_message(message="Welcome in Humber College")

# Task-2: Allowing user to enter a password which satisfies the stated conditions in the assignment
proceed_ahead_flag = user_authenticator.process_password()

# Proceeding only if a valid password was entered within 3 attempts
if proceed_ahead_flag == True:

    # Task-3: Accepting count of students which satisfies the stated conditions in the assignment
    further_proceed_flag = student_operations.verify_students_count()

    # Proceeding only if a valid count of students was entered within 3 attempts
    if further_proceed_flag == True:

        # Task-4: Accepting the names of students
        student_operations.accept_student_names()

        # Task-5: Accepting the grades of every student
        student_operations.accept_student_grades()

        # Task-6: Calculating GPA of students based on their marks
        student_operations.calculate_gpa()

        # Task-7: Assigning schools to the students based on their GPAs
        student_operations.assign_schools()

        # Task-8: Generating student reports as per GPA and assigned schools
        student_operations.generate_student_reports()