class Main:
    # ====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open(fileName, 'r') as fi:
            data = fi.read()
        print(data)
        # end def

    # ====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        count = 0
        with open(fileName, 'r') as fi:
            data = fi.read()
        data = data.replace('\n', ' ')
        print(len(data.split(' ')))

        # end def

    # ====================f3====================
    def f3(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open(fileName, 'r') as fi:
            data = fi.read()
        
        lst_line = data.split('\n')
        for line_id in range(len(lst_line)-1, -1, -1):
            line = lst_line[line_id]
            line = line.replace('.', '')
            line = line.replace(',', '')
            line = line.replace('?', '')
            line = line.replace('!', '')
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace('{', '')
            line = line.replace('}', '')
            line = line.replace('"', '')
            line = line.replace('\\', '')
            line = line.replace("'", '')
            print(line)


        # print(lst_line)


        # end def

    # ====================DO NOT CHANGE THE CODE BELOW====================================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f2 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        fileName = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(fileName)
        elif choice == 2:
            self.f2(fileName)
        elif choice == 3:
            self.f3(fileName)
        else:
            print("Wrong select")
        print("FINISH")


main = Main()
main.main()
