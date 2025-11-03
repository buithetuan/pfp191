# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class Book:
    def __init__(self, name, year, doi):
        self.name = name
        self.year = year
        self.doi = doi

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_doi(self):
        return self.doi

    def set_doi(self, doi):
        self.doi = doi

    def display_info(self):
        print(f"Year: {self.year}")
        print(f"DOI: {self.doi}")
        print(f"Name: {self.name}")


class Novel(Book):
    def __init__(self, name, year, doi, author):
        super().__init__(name, year, doi)
        self.author = author

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST BOOKS========
    def InputListBook(self):
        n = int(input('Enter the number of books: '))
        books = []
        for i in range(n):
            print(f"Enter book {i+1}")
            name = input("Enter name: ")
            year = input("Enter year: ")
            doi = input("Enter doi: ")
            book = Book(name, year, doi)
            books.append(book)
        return books
        # end def
    def InputNovel(self):
        name = input("Enter name: ")
        year = input("Enter year: ")
        doi = input("Enter doi: ")
        author = input("Enter author: ")
        novel = Novel(name, year, doi, author)
        return novel
        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i, book in enumerate(bookList):
            print(f"Book {i+1}")
            book.display_info()
                    
        # end def
    #==========================================

    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        bookList.sort(key=lambda x: x.get_name())
        for i, book in enumerate(bookList):
            print(f"Book {i+1}")
            book.display_info()
                   
        # end def
    #==========================================



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        bookList = self.InputListBook()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        filtered_books = filter(lambda x: x.get_doi().startswith("10.1000"), bookList)
        filtered_books = sorted(filtered_books, key=lambda x: int(x.get_year()), reverse=True)
        for i, book in enumerate(filtered_books):
            print(f"Book {i+1}")
            book.display_info()
        
        # end def
    #==========================================
    
    def f4(self):
        # =======DO NOT EDIT CODE BELOW===============
        nov = self.InputNovel()
        print("OUTPUT")
        # ==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        nov.display_info()
        

        # end def   



#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" 4. Test f4 (1 mark)")
        print(" Your selection (1 -> 4): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        elif choice == 4:
            self.f4()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
