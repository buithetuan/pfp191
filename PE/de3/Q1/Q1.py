class Main:
    # ====================f1====================
    def f1(self, n):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        total = 0
        num = 0
        for i in range(n):
            num = num * 10 + 1
            total += num
        print(total)

    # ====================f2====================
    def f2(self, n):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i in range(n):
            left_part = ''.join(chr(65+j) for j in range(i+1)) #ABCD
            right_part = left_part[-2::-1]
            full_row = left_part + right_part
            print(full_row.center(2*n+1))
        # end def

    # ====================f3====================
    def f3(self, s):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if not s:
            return ""
        
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                result.append(s[i-1] + str(count))
                count = 1
        result.append(s[-1] + str(count))
        print("".join(result))

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
            n = int(input('Enter the number'))
            self.f1(n)
        elif choice == 2:
            n = int(input('Enter the number of row'))
            self.f2(n)
        elif choice == 3:
            string = input('Enter the string: ')
            self.f3(string)
        else:
            print("Wrong select")
        print("FINISH")


main = Main()
main.main()