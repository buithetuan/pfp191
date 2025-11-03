class Main:
    # ====================f1====================
    def f1(self, n):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        def check_prime(number):
            if number < 2:
                return False
            for i in range(2, int(number ** 0.5)+1):
                if number % i == 0:
                    return False
            return True

        total = 0
        for i in range(2, n):
            if check_prime(i):
                total += i
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
            n = int(input('Enter n:'))
            self.f1(n)
        else:
            print("Wrong select")
        print("FINISH")


main = Main()
main.main()