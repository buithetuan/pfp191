# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0
        self.age = 0
    
    def input(self):
        self.name = input("Enter name: ")
        self.salary = int(input("Enter salary: "))
        self.age = int(input("Enter age: "))
        
    def show_info(self):
        print(self.name)
        print(self.salary)
        print(self.age)
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST EMPLOYEE========
    def InputListEmployee(self):
        n = int(input('Enter the number of students: '))
        emp_list = []
        for i in range(n):
            print(f"Enter employees {i+1}")
            temp_emp = Employee()
            temp_emp.input()
            emp_list.append(temp_emp)
        return emp_list
        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i, emp in enumerate(employeeList, start=1):
            print(f"Employee {i}")
            emp.show_info()
        # end def


    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        # === Sort employees by decreasing age ===
        employeeList.sort(key=lambda x: x.age, reverse=True)

        # === Print list after sorting ===
        for i, emp in enumerate(employeeList, start=1):
            print(f"Employees {i}")
            emp.show_info()
        # end def



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        # === Filter employees age >= 18 ===
        filtered_list = [emp for emp in employeeList if emp.age >= 18]

        # === Sort by decreasing salary ===
        filtered_list.sort(key=lambda x: x.salary, reverse=True)

        # === Print sorted list ===
        for i, emp in enumerate(filtered_list, start=1):
            print(f"Employees {i}")
            emp.show_info()
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
