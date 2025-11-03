class Main:
    # ====================f1====================
    def f1(self, lst_number, x):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        total = 0
        count = 0
        for element in lst_number:
            if element % x == 0:
                total += element
                count += 1
        print(total/count)
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
            lst_number = []
            n = int(input('Enter the number of element:'))
            for i in range(n):
                element = int(input("Enter the element:"))
                lst_number.append(element)
            x = int(input('Enter x:'))
            self.f1(lst_number, x)
        else:
            print("Wrong select")
        print("FINISH")


main = Main()
main.main()