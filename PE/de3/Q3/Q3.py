# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Student:
    def __init__(self, name, Class, assessment, practice_exam, final_exam):
        self.name = name
        self.cls = Class
        self.assessment = assessment
        self.pe = practice_exam
        self.fe = final_exam

    def show(self):
        print(self.name)
        print(self.cls)
        print(self.assessment)
        print(self.pe)
        print(self.fe)


# =========================================================
class Main:

    # ====EDIT THIS FUNCTION TO READ AND RETURN LIST STUDENT========
    def InputListStudent(self):
        n = int(input('Enter the number of Students: '))
        student_list = []
        for i in range(n):
            print(f"Enter student {i+1}")
            name = input("Enter name: ")
            cls = input('Enter class')
            assess = input('Enter Assessment')
            pe = input('Enter Practice Exam')
            fe = input('Enter Final Exam')
            student = Student(name, cls, assess, pe, fe)
            student_list.append(student)
        return student_list
        # end def

    # ====================f1====================
    def f1(self):
        # =======DO NOT EDIT CODE BELOW===============
        studentList = self.InputListStudent()
        print("OUTPUT")
        # ==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        i = 1
        for student in studentList:
            print(f'Student {i}')
            student.show()
            i += 1

        # end def

    # ====================f2====================
    def f2(self):
        # =======DO NOT EDIT CODE BELOW===============
        studentList = self.InputListStudent() #
        print("OUTPUT")
        # ==========================================
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        studentList.sort(key=lambda x: x.name, reverse=False)
        i = 1
        for student in studentList:
            print(f'Student {i}')
            student.show()
            i += 1
        # end def

    # ==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())

        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        else:
            print("Wrong select")
        print("FINISH")


main = Main()
main.main()