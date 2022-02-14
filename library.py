class Library:
    def __init__(self, bookList, name):
        self.bookList = bookList
        self.name = name
        self.bookDict = {}
        self.bookUsed = False
    def displayBooks(self):
        for book in self.bookList:
            print(book)
    def lendBook(self, name, book):
        if book not in self.bookDict.keys():
            self.bookDict[book] = name
            print(f"Take your book {name}")
        else:
            print(f"This book has been already taken by {self.bookDict[book]}")
    def addBook(self, book):
        self.bookList.append(book)
    def returnBook(self, book):
        self.bookDict.pop(book, None)
        print(self.bookDict)
library = Library(["python", "C++", "Ruby", "php"], "CodeWithTariq")
while True:
    print(f"Welcome to {library.name} Enter your choice to continue")
    print("Press 1 for displaybooks\nPress 2 for lendbook\nPress 3 for addbook\nPress 4 for returnbook")
    choice = int(input("Enter Here: "))
    if choice == 1:
        library.displayBooks()
    elif choice == 2:
        name = input("Enter your name")
        book = input("Enter the book name")
        library.lendBook(name, book)
    elif choice == 3:
        book = input("Type the book name you want to add")
        library.addBook(book)
    elif choice == 4:
        book = input("Type the book name you want to remove")
        library.returnBook(book)
    else:
        print("Not a valid option")

    choice2 = ""
    while choice2 != "c" and choice2 != "q":
        choice2 = input("Press q to quit c to continue")
        if choice2 == "q":
            quit()
        elif choice2 == "c":
            continue
        else:
            print("Invailed")
