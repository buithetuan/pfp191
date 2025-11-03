class Main:
    #====================f1====================
    def f1(self, num):
        """
        Bài 1: Tính tổng chuỗi S = 2^1 - 2^2 + 2^3 - 2^4 + ... + 2^(2n-1)
        - Tổng gồm 2n - 1 số hạng, mũ chạy từ 1 đến 2n - 1
        - Các mũ lẻ: cộng, mũ chẵn: trừ
        Ví dụ: n = 5 → S = 2^1 - 2^2 + 2^3 - 2^4 + ... + 2^9 = 410
        """
        total = 0
        sign = 1
        for i in range(1, 2 * num, 2):
            total += sign * (2 ** i)
            sign *= -1  
        print(total)

    #====================f2====================
    def f2(self, row):
        """
        Bài 2: In tam giác chữ cái từ 'A' đến 'Z' (tuần hoàn lại 'A' nếu vượt quá 'Z')
        - Dòng 1 có 1 ký tự, dòng 2 có 2 ký tự, ..., dòng n có n ký tự
        - Mỗi ký tự tiếp theo tăng theo bảng chữ cái tiếng Anh
        Ví dụ: row = 3 → A → BC → DEF
        """
        ch = ord('A')
        for i in range(1, row + 1):
            for j in range(i):
                print(chr(ch), end='')
                ch += 1
                if ch > ord('Z'):
                    ch = ord('A')
            print()

    #====================f3====================
    def f3(self, Str):
        """
        Bài 3: Tính tổng các chữ số có trong chuỗi đầu vào
        - Chỉ cộng các ký tự là chữ số (0-9)
        Ví dụ: "PFP191 PE 2023" → 1 + 9 + 1 + 2 + 0 + 2 + 3 = 18
        """
        total = 0
        for c in Str:
            if c.isdigit():
                total += int(c)
        print(total)

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        if choice == 1:
            num = int(input("Enter the n of terms: "))
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


#=============================================================================================
class Main:
    #====================f1====================
    def f1(self, num):
        """
        Bài 1: Tính tổng chuỗi S = 1 - 2^2 + 3^2 - 4^2 + ... ± n^2
        - Cộng nếu chỉ số lẻ, trừ nếu chỉ số chẵn
        Ví dụ: n = 5
        S = 1 - 4 + 9 - 16 + 25 = 15
        OUTPUT
        15
        """
        total = 0
        for i in range(1, num + 1):
            if i % 2 == 0:
                total -= i ** 2
            else:
                total += i ** 2
        print(total)

    #====================f2====================
    def f2(self, row):
        """
        Bài 2: In tam giác vuông ngược rỗng bằng số
        - Dòng 1 in từ 1 đến n
        - Các dòng giữa in số đầu, khoảng trắng, số cuối
        - Dòng cuối chỉ in 1
        Ví dụ: row = 5
        OUTPUT
        1 2 3 4 5      
        1     4
        1   3
        1 2
        1
        """
        for i in range(row, 0, -1):
            for j in range(1, i + 1):
                if i == row or j == 1 or j == i:
                    print(j, end=' ')
                else:
                    print(' ', end=' ')
            print()

    #====================f3====================
    def f3(self, Str):
        """
        Bài 3: Đếm số lần xuất hiện của các ký tự lặp lại trong chuỗi và lưu dưới dạng dictionary
        - Bỏ qua khoảng trắng
        - Chỉ in ra các ký tự xuất hiện từ 2 lần trở lên
        Ví dụ: "PE PFP191"
        OUTPUT
        {'P': 3, '1': 2}
        """
        count = {}
        for ch in Str:
            if ch != ' ':
                count[ch] = count.get(ch, 0) + 1
        result = {k: v for k, v in count.items() if v > 1}
        print(result)

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        if choice == 1:
            num = int(input("Enter the number of terms: "))
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
#=============================================================================================
class Main:
    #====================f1====================
    def f1(self, num):
        """
        Bài 1: In ra danh sách các số Fibonacci với số lượng n phần tử do người dùng nhập
        - Dãy Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
        - Mỗi số sau là tổng của hai số trước đó
        Ví dụ: n = 10
        OUTPUT
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        """
        fib = []
        a, b = 0, 1
        for _ in range(num):
            fib.append(a)
            a, b = b, a + b
        print(fib)      
        
        pass
        # end def
    
    #====================f1====================
    def f2(self, row):
        """
        Bài 2: In tam giác nhị phân với số dòng do người dùng nhập
        - Dùng quy luật: (i + j) % 2 == 0 → in 1, ngược lại in 0
        Ví dụ: row = 5
        OUTPUT
        1
        10
        101
        0101
        10101
        """
        for i in range(row):
            for j in range(i + 1):
                if (i + j) % 2 == 0:
                    print("1", end='')
                else:
                    print("0", end='')
            print()   
        
        pass      
        # end def


    #====================f2====================
    def f3(self, Str):
        """
        Bài 3: Đếm số lượng nguyên âm và phụ âm trong chuỗi
        - Không phân biệt hoa thường
        - Bỏ qua khoảng trắng và ký tự đặc biệt
        Ví dụ:
        "Truong dai hoc FPT co so Ha Noi"
        OUTPUT
        Number of Vowels: 10
        Number of Consonants: 14
        """
        vowels = "aeiouAEIOU"
        vowel_count = 0
        consonant_count = 0
        for ch in Str:
            if ch.isalpha():
                if ch in vowels:
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

#==========================================================================================
import math

class Main:
    #====================f1====================
    def f1(self, x, n):
        """
        Bài 1: Tính tổng của chuỗi:
        S = 1 - X^2/2! + X^4/4! - X^6/6! + ... + (-1)^n * X^(2n)/(2n)!
        - Với X và n được nhập từ người dùng
        - Sử dụng vòng lặp để tính từng hạng tử theo công thức
        Ví dụ:
        Input: X = 2, n = 4
        OUTPUT
        -0.41587301587301595
        """
        S = 1.0
        for i in range(1, n + 1):
            term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
            S += term
        print(S)

    #====================f2====================
    def f2(self, row):
        """
        Bài 2: In tam giác binary xen kẽ theo quy luật:
        - Hàng 1 in: 1
        - Hàng 2 in: 0 1
        - Hàng 3 in: 1 0 1
        - Căn phải bằng khoảng trắng
        Ví dụ: row = 4
        OUTPUT
           1
          0 1
         1 0 1
        0 1 0 1
        """
        for i in range(row):
            print(' ' * (row - i - 1), end='')
            val = (i + 1) % 2
            for j in range(i + 1):
                print(val, end=' ')
                val = 1 - val
            print()

    #====================f3====================
    def f3(self, Str):
        """
        Bài 3: Đảo ngược từng từ trong chuỗi
        - Mỗi từ được giữ nguyên vị trí, nhưng các ký tự trong từ thì đảo ngược
        - Khoảng trắng giữa các từ giữ nguyên
        Ví dụ:
        Input: "Truong dai hoc FPT Ha Noi"
        OUTPUT
        gnuorT iad coh TPF aH ioN
        """
        words = Str.split()
        re_words = [word[::-1] for word in words]
        result = ' '.join(re_words)
        print(result)

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        if choice == 1:
            x = int(input("Enter the value of X: "))
            n = int(input("Enter the number of terms: "))


#=============================================================================================
class Main:
    #====================f1====================
    def f1(self, num):
        """
        Bài 1: Tính tổng của chuỗi:
        S = 1 + 11 + 111 + ... + (n số hạng)
        - Mỗi số hạng tạo bằng cách thêm số 1 vào cuối số trước đó
        Ví dụ: num = 5
        OUTPUT
        12345
        """
        s = 0
        current = 0
        for _ in range(num):
            current = current * 10 + 1
            s += current
        print(s)

    #====================f2====================
    def f2(self, row):
        """
        Bài 2: In tam giác chữ cái như sau:
        - Dòng 1: A
        - Dòng 2: ABA
        - Dòng 3: ABCBA
        - Dòng 4: ABCDCBA
        ...
        Ví dụ: row = 5
        OUTPUT
         A
        ABA
       ABCBA
      ABCDCBA
     ABCDEDCBA
        """
        for i in range(1, row + 1):
            print(" " * (row - i), end="")
            for j in range(65, 65 + i):
                print(chr(j), end="")
            for j in range(65 + i - 2, 64, -1):
                print(chr(j), end="")

            print()

    #====================f3====================
    def f3(self, Str):
        """
        Bài 3: Nén chuỗi theo ký tự lặp lại liên tiếp
        - Nếu chuỗi là: pppppppppffffffffpppppppp → in: p9f8p8
        - Mỗi nhóm ký tự lặp lại → in 1 lần kèm số lượng
        Ví dụ:
        Input: "pppppppppffffffffpppppppp"
        OUTPUT
        p9f8p8
        """
        if not Str:
            print("")
            return

        result = ''
        count = 1
        for i in range(1, len(Str)):
            if Str[i] == Str[i - 1]:
                count += 1
            else:
                result += Str[i - 1] + str(count)
                count = 1
        result += Str[-1] + str(count)
        print(result)

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
