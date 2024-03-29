class Student:

    def __init__(self):
        self.first_name = None
        self.last_name = None

        self.math_marks = None
        self.science_marks = None
        self.language_marks = None
        self.drama_marks = None
        self.music_marks = None
        self.biology_marks = None

        self.gpa = None
        self.assigned_school = None

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_math_marks(self):
        return self.math_marks

    def get_science_marks(self):
        return self.science_marks

    def get_language_marks(self):
        return self.language_marks

    def get_drama_marks(self):
        return self.drama_marks

    def get_music_marks(self):
        return self.music_marks

    def get_biology_marks(self):
        return self.biology_marks

    def get_gpa(self):
        return self.gpa

    def get_assigned_school(self):
        return self.assigned_school

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_math_marks(self, marks):
        self.math_marks = marks

    def set_science_marks(self, marks):
        self.science_marks = marks

    def set_language_marks(self, marks):
        self.language_marks = marks

    def set_drama_marks(self, marks):
        self.drama_marks = marks

    def set_music_marks(self, marks):
        self.music_marks = marks

    def set_biology_marks(self, marks):
        self.biology_marks = marks

    def set_gpa(self, gpa):
        self.gpa = gpa

    def set_assigned_school(self, school):
        self.assigned_school = school


class StudentOperations:

    def __init__(self):
        self.students_list = []
        self.students_count = None
        self.valid_count_flag = False

        self.math_credits = 4
        self.science_credits = 5
        self.language_credits = 4
        self.drama_credits = 3
        self.music_credits = 2
        self.biology_credits = 4

        self.accepted_students_count = 0
        self.engineering_students_count = 0
        self.business_students_count = 0
        self.law_students_count = 0

    def get_students_count(self):
        return self.students_count

    def get_valid_count_flag(self):
        return self.valid_count_flag

    def get_students_list(self):
        return self.students_list

    def verify_students_count(self):
        attempts_left = 3
        while self.valid_count_flag == False and attempts_left != 0:
            self.students_count = int(input("Enter the number of students (number must be between 1 and 50, inclusive): "))

            if self.students_count < 1 or self.students_count > 50:
                attempts_left = attempts_left - 1

                if attempts_left > 0:
                    print("Number of students should be between 1 and 50.")
                    print("Please try again...")
                    print("Number of attempts left: " + str(attempts_left))
                else:
                    print("\n" + "No attempts left now! The program has been terminated")


            else:
                print("The entered student counts meets the criteria. Let's proceed to the next step... ")
                self.valid_count_flag = True

        return self.valid_count_flag

    def accept_student_names(self):
        students_count = self.get_students_count()

        for i in range(0, students_count):
            student = Student()

            print("For student " + str(i + 1) + ", enter the following details:")
            f_name = input("First name: ")
            l_name = input("Last name: ")

            student.set_first_name(first_name=f_name)
            student.set_last_name(last_name=l_name)
            self.students_list.append(student)

        print("The system has recorded the names of all students. Please proceed to the next step..." + "\n")
        return None

    def accept_student_grades(self):
        print("Now, enter the marks of various courses for " + str(self.students_count) + " students" + "\n")

        for i in range(0, self.students_count):
            print("Enter marks for " + self.students_list[i].get_first_name() + " " + self.students_list[i].get_last_name())
            math_marks = int(input("Input your mark in Math (Credit hours = 4): "))
            science_marks = int(input("Input your mark in Science (Credit hours = 5): "))
            language_marks = int(input("Input your mark in Language (Credit hours = 4): "))
            drama_marks = int(input("Input your mark in Drama (Credit hours = 3): "))
            music_marks = int(input("Input your mark in Music (Credit hours = 2): "))
            biology_marks = int(input("Input your mark in Biology (Credit hours = 4): "))

            self.students_list[i].set_math_marks(marks=math_marks)
            self.students_list[i].set_science_marks(marks=science_marks)
            self.students_list[i].set_language_marks(marks=language_marks)
            self.students_list[i].set_drama_marks(marks=drama_marks)
            self.students_list[i].set_music_marks(marks=music_marks)
            self.students_list[i].set_biology_marks(marks=biology_marks)

        print("The marks of all students were accepted by the system \n")
        return None

    def calculate_gpa(self):

        total_credits = self.math_credits + self.science_credits + self.language_credits + self.drama_credits + self.music_credits + self.biology_credits
        for i in range(0, self.students_count):

            math_weight = self.students_list[i].get_math_marks() * self.math_credits
            science_weight = self.students_list[i].get_science_marks() * self.science_credits
            language_weight = self.students_list[i].get_language_marks() * self.language_credits
            drama_weight = self.students_list[i].get_drama_marks() * self.drama_credits
            music_weight = self.students_list[i].get_music_marks() * self.music_credits
            biology_weight = self.students_list[i].get_biology_marks() * self.biology_credits

            total_marks_weight = math_weight + science_weight + language_weight + drama_weight + music_weight + biology_weight
            computed_gpa = total_marks_weight / total_credits * 1.0
            self.students_list[i].set_gpa(gpa=computed_gpa)

            print(self.students_list[i].get_first_name() + " " + self.students_list[i].get_last_name() + " Computed GPA = " + str(round(computed_gpa, 2)))


        print("GPAs of all students have been generated")
        return None

    def assign_schools(self):

        for i in range(0, self.students_count):
            current_student_gpa = self.students_list[i].get_gpa()

            if current_student_gpa >= 90 and current_student_gpa <= 100:
                self.students_list[i].set_assigned_school(school="School of Engineering")
                self.engineering_students_count += 1
                self.accepted_students_count += 1

            elif current_student_gpa >= 80 and current_student_gpa < 90:
                self.students_list[i].set_assigned_school(school="School of Business")
                self.business_students_count += 1
                self.accepted_students_count += 1

            elif current_student_gpa >= 70 and current_student_gpa < 80:
                self.students_list[i].set_assigned_school(school="Law School")
                self.law_students_count += 1
                self.accepted_students_count += 1
            else:
                self.students_list[i].set_assigned_school(school="Not accepted")

        print("Schools have been assigned to students based on their GPAs" + "\n")
       # return None

    def generate_student_reports(self):

        print("Now, generating reports...." + "\n")

        print("Report 1")
        print("....................................................")
        print("Student Name \t \t School Name")
        for i in range(0, self.students_count):
            student = self.students_list[i]

            print(student.get_first_name() + " " + student.get_last_name() + "\t \t " + student.get_assigned_school())

        print("...................................................." + "\n")

        print("Report 2")
        print("....................................................")
        print("Total number of students accepted in Humber College: " + str(self.accepted_students_count) + "\n")
        print("Distribution of students per each school is as follows:")
        print("School of Engineering: " + str(self.engineering_students_count))
        print("School of Business: " + str(self.business_students_count))
        print("Law School: " + str(self.law_students_count))
        print("...................................................." + "\n")

        print("Report 3")
        print("....................................................")

        not_accepted_students = self.students_count - self.accepted_students_count
        print("Number of students that were not accepted: " + str(not_accepted_students))
        print("...................................................." + "\n")

        print("Report 4")
        print("....................................................")

        engineering_students_percentage = self.engineering_students_count/self.accepted_students_count * 100.0
        business_students_percentage = self.business_students_count/self.accepted_students_count * 100.0
        law_students_percentage = self.law_students_count/self.accepted_students_count * 100.0

        print("Percentage distribution of accepted students per school")
        print("School of Engineering: " + str(round(engineering_students_percentage, 2)) + "%")
        print("School of Business: " + str(round(business_students_percentage, 2)) + "%")
        print("Law School: " + str(round(law_students_percentage, 2)) + "%")
        print("...................................................." + "\n")

        # return None





