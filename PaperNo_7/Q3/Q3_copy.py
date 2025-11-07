# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Employee:
    def  __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name
    
    def get_age(self):
        return self.age
    
    def get_salary(self):
        return self.salary
    
    def show_info(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.salary}")

class Manager(Employee):
    def __init__(self,name,age,salary,rank):
        super().__init__(name,age,salary)
        self.rank = rank
        
    def get_rank(self):
        return self.rank
    
    def set_rank(self):
        self.rank = rank
    
    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Salary: {self.salary}')
        print(f'Rank: {self.rank}')
        
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST STUDENT========
    def InputListEmployee(self):
        n = int(input("Enter the number of employees: "))
        employees = []
        for i in range(n):
            print(f"Enter employee {i +1}")
            name = input("Enter name: ")
            age = input('Enter age: ')
            salary = input('Enter salary: ')
            employee = Employee(name,age,salary)
            employees.append(employee)
        return employees
    
    def InputManager(self):
        n = int(input("Enter the number of managers: "))
        managers = []
        for i in range(n):
            print(f"Enter manager {i +1}")
            name = input("Enter name: ")
            age = input('Enter age: ')
            salary = input('Enter salary: ')
            rank = input('Enter rank: ')
            manager = Manager(name,age,salary,rank)
            managers.append(manager)
        return managers
    # ===END DEF

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================
        for i, employee in enumerate(employeeList):
            print(f'Employee {i +1}')
            employee.show_info()
        # ===END DEF

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        employeeList.sort(key=lambda x: x.get_name())
        for i, employee in enumerate(employeeList):
            print(f'Employee {i +1}')
            employee.show_info()

        # ===END DEF



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        total_salary = 0
        num_emp = 0
        for emp in employeeList:
            total_salary += int(emp.get_salary())
            num_emp += 1
        
        avg_salary = total_salary / num_emp
        filter_emp = []
        for e in employeeList:
            if int(e.get_salary())> avg_salary:
                filter_emp.append(e)
        filter_emp.sort(key=lambda x: int(x.get_salary()), reverse= True)
        for i, employee in enumerate(filter_emp):
            print(f'Employee {i +1}')
            employee.show_info()
        # ===END DEF

    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        list_manager = self.InputManager()
        print("OUTPUT")
        # ==========================================
        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i, manager in enumerate(list_manager):
            print(f'Manager {i +1}')
            manager.display_info()
        # ===END DEF   



#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
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
