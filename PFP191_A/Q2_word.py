class Main:
    #====================f1====================
    def f1(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        file1 = open(fileName, 'r')
        content = file1.read()
        print(content)
        
        
                
        pass

        # end def

    #====================f2====================
    def f2(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        count = 0
        with open(fileName, 'r') as file:
            for line in file:
                count +=1
        print(count)
        pass

        # end def
    #====================f3====================
    def f3(self, fileName):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        dict2 = {}
        with open(fileName, 'r') as file:
            for line in file:
                line = line.strip().split(" ")
                for word in line:
                    if word not in dict2:
                        dict2[word] = 1
                    else:
                        dict2[word] +=1
        big_list = []
        for key, value in dict2.items():
            small_list = key,value
            small_list = list(small_list)
            big_list.append(small_list)
        #new_list = sorted(big_list, key = lambda x: x[1], reverse = True)
        big_list.sort(key = lambda x: (x[1], x[0]))
        
       
        for i in range(len(big_list)-1, len(big_list) - 11, -1):
            str1 = "{} {}".format(big_list[i][0], big_list[i][1])
            print(str1)
            
        pass

        # end def
        
#====================DO NOT CHANGE THE CODE BELOW====================================
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
