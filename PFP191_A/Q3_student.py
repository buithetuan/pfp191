# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark
    
    def show(self):
        print(self.name)
        print(self.age)
        print(self.mark)

#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST STUDENT========
    def InputListStudent(self):
        n = int(input('Enter the number of students: '))
        students_list = []
        for i in range (n):
            print(f'Enter student {i+1}')
            name = input('Enter name: ')
            age = input('Enter age: ')
            mark = input('Enter mark: ')
            student = Student(name, age, mark)
            students_list.append(student)
        return students_list
        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        studentList = self.InputListStudent()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        i = 1
        for student in studentList:
            print(f'Student {i}')
            student.show()
            i += 1
        # end def

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        studentList = self.InputListStudent()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        studentList.sort(key = lambda x: x.name, reverse = False)
        i = 1
        for student in studentList:
            print(f'Student {i}')
            student.show()
            i += 1
        # end def



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        studentList = self.InputListStudent()
        print("OUTPUT")
        #==========================================
        studentList_new = []
        total_mark = 0.0
        for student in studentList:
            total_mark += float(student.mark)
        average_mark = total_mark/int(len(studentList))
        i = 1
        for student in studentList:
            if float(student.mark) >= average_mark:
                studentList_new.append(student) 
        studentList_new.sort(key = lambda x: x.mark, reverse = True)
        i = 1
        for student in studentList_new:
            print(f'Student {i}')
            student.show()
            i += 1
        

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========

        # end def




#==================DO NOT CHANGE THE CODE BELOW=====================
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

