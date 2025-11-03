class Main:
    # ====================f1====================
    def f1(self, string):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        total = 0
        for s in string:
            if s.isdigit():
                total += int(s)
        print(total)
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
            string = input('Enter string:')
            self.f1(string)
        else:
            print("Wrong select")
        print("FINISH")


main = Main()
main.main()