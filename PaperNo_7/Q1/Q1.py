import math
class Main:
    #====================f1====================
    def f1(self, num):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        total = 0
        for i in range(1, num+1):
            if i % 2 == 0:
                total -= i**2
            else:
                total += i**2
        print(total)
        # ===END DEF
    
    #====================f1====================
    def f2(self, row):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i in range(row, 0, -1):
            for j in range(1, i+1):
                if j == 1 or j==i or i==row:
                    print(j, end=" ")
                else:
                    print(" ", end=" ")
            print()
        # ===END DEF

    #====================f2====================
    def f3(self, Str):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        freq = {}
        for char in Str:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        new_freq = {}
        for key, val in freq.items():
            if val > 1:
                new_freq[key] = val
        print(new_freq)
        pass     
        # ===END DEF   

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        if choice == 1:
            num = int(input("Enter the number of terms: "))
            print("OUTPUT")
            self.f1(num)
        elif choice == 2:
            row = int(input("Enter the number of rows: "))
            print("OUTPUT")
            self.f2(row)
        elif choice == 3:
            Str = input("Enter a string: ")
            print("OUTPUT")
            self.f3(Str)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()





