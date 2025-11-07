class Main:
    #====================f1====================
    def f1(self, num):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        total = 0
        number = 2*num - 1
        i = 0
        for j in range(1, number+1):
            if j % 2 != 0:
                if i % 2 == 0:
                    total += 2**j
                else:
                    total -= 2**j
                i += 1
        print(total)

        # end def
        
    #====================f2====================
    def f2(self, row):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        '''
        A
        B C
        D E F
        G H I J
        K L M N O
        .....
        '''
        char_code = ord('A')
        for i in range(1, row+1):
            for j in range(i):
                print(chr(char_code), end=" ")
                char_code += 1
                if char_code > ord('Z'):
                    char_code = ord('A')
            print()

        pass
        # end def

    #====================f3====================
    def f3(self, Str):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        total = 0
        for i in Str:
            if i.isdigit():
                total += int(i)
        print(total)
        # end def   
    
#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        if choice == 1:
            num = int(input("Enter the n of terms: "))
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



