# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class book:
    def __init__(self, name, year, doi):
        self.name = name
        self.year = year
        self.doi = doi
    def getall(self):
        print(self.name)
        print(self.year)
        print(self.doi)        
    
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST BOOKS========
    def InputListBooks(self):
        list_book = []
        n = int(input('Enter the number of books: '))
        for i in range(n):
            print(f"Enter book {i+1}")
            name = input("Enter name: ")
            year = input("Enter year: ")
            doi = input("Enter doi:")
            b = book(name, year, doi)
            list_book.append(b)
        return list_book    

        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBooks()
        print("OUTPUT")
        #==========================================
 
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        i=1
        for b in bookList:
            print(f"Book {i}")
            b.getall()
            i +=  1    
        # end def
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        bookList.sort(key=lambda x: x.name, reverse=False)
        i = 1
        for b in bookList:
            print(f"Book {i}")
            b.getall()
            i += 1  
        
        # end def
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========

        filtered_books = filter(lambda x: x.doi.startswith('10.1000'), bookList)
        sorted_books = sorted(filtered_books, key=lambda x: x.year, reverse=True)
        for i, book in enumerate(sorted_books):
            print(f"Book {i+1}")
        b.getall()            
    pass
        # end def
    #==========================================




#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

