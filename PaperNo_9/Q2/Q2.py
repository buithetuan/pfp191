class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open(fileName, 'r') as fi:
            data = fi.readlines()
        for line in data:
            line = line.strip()
            num_lst = line.split(' ')
            for num in num_lst:
                print(num)
        pass
        # end def

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        def analysis_to_prime_number(n):
            i = 2
            listNumbers = []
            text = f'{n} ='
            while (n > 1):
                if (n % i == 0):
                    n = int(n / i);
                    listNumbers.append(str(i))
                else:
                    i = i + 1
            if len(listNumbers) == 0:
                listNumbers.append(str(n))
            for i in listNumbers[:-1]:
                text += f' {i} x'
            text += f' {listNumbers[-1]}'
            return text
        with open(fileName, 'r') as fi:
            data = fi.readlines()
        for line in data:
            line = line.strip()
            num_lst = line.split(' ')
            for num in num_lst:
                print(analysis_to_prime_number(int(num)))

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
