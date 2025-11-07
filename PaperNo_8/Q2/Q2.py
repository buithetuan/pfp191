class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        pass
        with open('data.txt', 'r') as file:
            data = file.read().strip()
            print(data)
        # end def

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        pass
        final = 0
        with open('data.txt', 'r') as file:
            data = file.read().strip()
            lst1 = data.split(',')
            for element in lst1:
                element = element.strip()
                lst2 = element.split(' ')
                tag = lst2[0]
                money = lst2[1]
                if tag == 'D':
                    final += int(money)
                elif tag == 'W':
                    final -= int(money)
        print(final)


        # end def
        
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
