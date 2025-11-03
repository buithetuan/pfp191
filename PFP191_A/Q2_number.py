class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open(fileName, "r") as f:
            content = f.read()
            number_list = content.split()
            for number in number_list:
                print(number)
            #for number in number_list:
                #print(number)
        # end def

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        with open(fileName, "r") as f:
            content = f.read()
            number_list = content.split()
            for number in number_list:
                self.prime_factor(number)
        pass
        # end def
    def prime_factor(self, number):
        number = int(number)
        prime = []
        num = number
        i = 2
        while number != 1:
            if number % i == 0:
                prime.append(i)
                number = number / i
            else:
                i += 1
        
        print(f'{num} = ', end = '')
        for i in range(len(prime)): 
            if i == (len(prime) - 1):
                print(prime[i])
            else:
                print(prime[i], end = ' x ')
        
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


