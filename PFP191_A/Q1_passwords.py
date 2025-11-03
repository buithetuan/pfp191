class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        passwords = inputString.split(",")
        for password in passwords:
            if any(char.isalpha() and char != "c" for char in password):
                print(password)
        pass
        # end def


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        passwords = inputString.split(",")
        for password in passwords:
            if any(int(char) % 2 != 0 for char in password if char.isnumeric()):
                print(password)
        pass
        # end def


    #====================f3====================
    def f3(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        passwords = inputString.split(",")
        for password in passwords:
            if any(char.isupper() for char in password):
                print(password)
        pass
        # end def


    #====================f4====================
    def f4(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        passwords = inputString.split(",")
        for password in passwords:
            if any(char in ["$", "#", "@", "&"] for char in password):
                print(password)

        pass
        # end def


    #====================f5====================
    def f5(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        passwords = inputString.split(",")
        for password in passwords:
            if len(password) >= 6:
                print(password)
        pass
        # end def


    #====================f6====================    
    def f6(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        passwords = inputString.split(",")
        for password in passwords:
            if len(password) <= 12:
                print(password)
        pass
        # end def


    #====================f7====================
    def f7(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        passwords = inputString.split(",")
        for password in passwords:
            if (any(char.isalpha() and char != "c" for char in password)
                    and any(int(char) % 2 != 0 for char in password if char.isnumeric())
                    and any(char.isupper() for char in password)
                    and any(char in ["$", "#", "@", "&"] for char in password)
                    and len(password) >= 6
                    and len(password) <= 12):
                print(password)
        pass
        # end def

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (0.25 mark)")
        print(" 2. Test f2 (0.25 mark)")
        print(" 3. Test f3 (0.25 mark)")
        print(" 4. Test f4 (0.25 mark)")
        print(" 5. Test f5 (0.25 mark)")
        print(" 6. Test f6 (0.25 mark)")
        print(" 7. Test f7 (1 mark)")
        print(" Your selection (1 -> 7): ")
        choice = int(input())
        inputString = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        elif choice == 3:
            self.f3(inputString)
        elif choice == 4:
            self.f4(inputString)
        elif choice == 5:
            self.f5(inputString)
        elif choice == 6:
            self.f6(inputString)
        elif choice == 7:
            self.f7(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
