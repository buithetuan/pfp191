import math
class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open(fileName, 'r') as file:
            numbers = file.readlines()
            for number in numbers:
                print(number.strip())
        pass
        # ===END DEF

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========     
        def is_prime(num):
            num = int(num)
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)+1)):
                if num % i == 0:
                    return False
            return True
        prime_list = []
        with open(fileName, 'r') as file:
            numbers = file.readlines()
            for number in numbers:
                if is_prime(number):
                    prime_list.append(int(number.strip()))
        prime_list.sort()
        print(prime_list)


        # ===END DEF   
        
#====================DO NOT CHANGE THE CODE BELOW====================================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        fileName = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(fileName)
        elif choice == 2:
            self.f2(fileName)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
