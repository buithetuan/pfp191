# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Teacher:
    def __init__(self, name, age, cls):
        self.name = name
        self.age = age
        self.cls = cls

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_cls(self):
        return self.cls

    def set_cls(self, cls):
        self.cls = cls

    def display_info(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.cls}")

class Professor(Teacher):
    def __init__(self, name, age, cls, address):
        super().__init__(name, age, cls)
        self.address = address

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def display_info(self):
        super().display_info()
        print(f'Address: {self.address}')
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST TEACHERS========
    def InputListTeacher(self):
        n = int(input('Enter the number of teachers: '))
        teachers = []
        for i in range(n):
            print(f'Enter teacher {i+1}')
            name = input('Enter name: ')
            age = input('Enter age: ')
            cls = input('Enter class: ')
            teacher = Teacher(name, age, cls)
            teachers.append(teacher)
        return teachers
        # end def
    
    def InputProfessor(self):
        n = int(input('Enter the number of professor: '))
        professors = []
        for i in range(n):
            print(f'Enter professor {i+1}')
            name = input('Enter name: ')
            age = input('Enter age: ')
            cls = input('Enter class: ')
            address = input('Enter address: ')
            professor = Professor(name, age, cls, address)
            professors.append(professor)
        return professors
    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i, teacher in enumerate(teacherList):
            print(f'Teacher {i+1}')
            teacher.display_info()
        # end def
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        teacherList.sort(key=lambda x: x.get_age(), reverse=True)
        for i, teacher in enumerate(teacherList):
            print(f'Teacher {i+1}')
            teacher.display_info()
        # end def
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        teacherList = self.InputListTeacher()
        print("OUTPUT")
        #==========================================
        fillterteacherList =[]
        for teacher in teacherList:
            if teacher.get_cls().startswith('SE'):
                fillterteacherList.append(teacher)
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        fillterteacherList.sort(key=lambda x: x.get_name())
        for i, teacher in enumerate(fillterteacherList):
            print(f'Teacher {i+1}')
            teacher.display_info()
        # end def
    #==========================================

    # ====================f4====================
    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        pro = self.InputProfessor()
        print("OUTPUT")
        # ==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i, professor in enumerate(pro):
                print(f'Professor {i+1}')
                professor.display_info()
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
