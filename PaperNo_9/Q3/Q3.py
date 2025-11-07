# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Student:
    def __init__(self, name, cls, gpa):
        self.name = name
        self.cls = cls
        self.gpa = gpa

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cls(self):
        return self.cls

    def set_gpa(self, cls):
        self.cls = cls

    def get_gpa(self):
        return self.gpa

    def set_cls(self, gpa):
        self.gpa = gpa

    def display_info(self):
        print(f"{self.name}")
        print(f"{self.cls}")
        print(f"{self.gpa}")

class Rating(Student):
    def __init__(self, name, cls, gpa):
        super().__init__(name, cls, gpa)
        self.rank = None

    def get_rank(self):
        return self.rank

    def set_rank(self, gpa):
        if 9 <= gpa <= 10:
            self.rank = 'Excellent'
        elif 7.5 <= gpa <= 8.99:
            self.rank = 'Good'
        elif 6.0 <= gpa <= 7.49:
            self.rank = 'Average'
        elif 5.0 <= gpa <= 5.99:
            self.rank = 'Needs Improvement'
        elif 0 <= gpa <= 4.99:
            self.rank = 'Fail'
        else:
            self.rank = 'cannot be rank'

    def display_info(self):
        print("Name: ", self.name)
        print("Class: ", self.cls)
        print("GPA: ", self.gpa)
        print("Rank: ", self.rank)
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST TEACHERS========
    def InputListStudent(self):
        n = input('Enter the number of Students: ')
        students = []
        for i in range(int(n)):
            print(f"Enter student {i + 1}")
            name = input("Enter name: ")
            cls = input("Enter class: ")
            gpa = float(input("Enter gpa: "))
            student = Student(name, cls, gpa)
            students.append(student)
        return students
        # end def
    def InputStudentRanking(self):
        n = input('Enter the number of Students: ')
        students = []
        for i in range(int(n)):
            print(f"Enter student {i + 1}")
            name = input("Enter name: ")
            cls = input("Enter class: ")
            gpa = float(input("Enter gpa: "))
            student = Rating(name, cls, gpa)
            student.set_rank(gpa)
            students.append(student)
        return students
        # end def
    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        StudentList = self.InputListStudent()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i, student in enumerate(StudentList):
            print(f"Student {i+1}")
            student.display_info()
        # end def


    #====================f2====================
    def f2(self):
        StudentList = self.InputListStudent()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        StudentList.sort(key=lambda x: x.get_gpa(), reverse=True)
        for i, student in enumerate(StudentList):
            print(f"Student {i + 1}")
            student.display_info()
        # end def
    #==========================================


    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        StudentList = self.InputListStudent()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        filterstudent = []
        for student in StudentList:
            if student.cls.startswith('SE'):
                filterstudent.append(student)
        filterstudent.sort(key=lambda x: x.get_name())
        for i, student in enumerate(filterstudent):
            print(f"Student {i + 1}")
            student.display_info()
        # end def
    #==========================================
    
    # ====================f4====================
    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        IMS = self.InputStudentRanking()
        print("OUTPUT")
        # ==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for ims in IMS:
            ims.display_info()
        # end def    
    # ==========================================


#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" 4. Test f4 (1 mark)")
        print(" Your selection (1 -> 4): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        elif choice == 4:
            self.f4()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

