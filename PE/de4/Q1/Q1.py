class Main:
    # ====================f1====================
    def f1(self, a, b, c):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        # if a < b:
        #     if a < c:
        #         print(a)
        #     else:
        #         print(c)
        # else:
        #     if b < c:
        #         print(b)
        #     else:
        #         print(c)
        print(min(a, b, c))
        # end def
    # ====================DO NOT CHANGE THE CODE BELOW====================================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f2 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        print("OUTPUT")
        if choice == 1:
            a = int(input('Enter the a:'))
            b = int(input('Enter the b:'))
            c = int(input('Enter the c:'))
            self.f1(a, b, c)
        else:
            print("Wrong select")
        print("FINISH")


main = Main()
main.main()