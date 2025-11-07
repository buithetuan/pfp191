class Main:
    #====================f1====================
    def f1(self, num):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        fib_seq = [0, 1]
        for _ in range(num - 2):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        print(fib_seq[:num])
        
        pass
        # end def
    
    #====================f1====================
    def f2(self, row):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i in range(2, row + 2):  # Lặp từ dòng 1 đến dòng n
            row_text = ""  # Chuỗi cho mỗi dòng
            for j in range(1, i):  # Tạo từng phần tử của dòng
                row_text += str(j % 2 + 1 - 1)  # Luân phiên 1 và 0
            print(row_text)  # In dòng đã tạo
        
        pass      
        # end def


    #====================f2====================
    def f3(self, Str):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        vowels = "aeiouAEIOU"
        vowel_count = 0
        consonant_count = 0
        for char in Str:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        print("Number of Vowels:", vowel_count)
        print("Number of Consonants:", consonant_count)
        pass     
        # end def   

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        if choice == 1:
            num = int(input("Enter a number: "))
            print("OUTPUT")
            self.f1(num)
        elif choice == 2:
            row = int(input("Enter the number of rows: "))
            print("OUTPUT")
            self.f2(row)
        elif choice == 3:
            Str = input("Enter a string: ")
            print("OUTPUT")
            self.f3(Str)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()



