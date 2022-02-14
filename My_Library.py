class Library:
    def __init__(self, name, list_books):
        self.list_books = list_books
        self.name = name
        self.lenddict = {}
    def displaybooks(self):
        print(f"Welcome to our {self.name} Library")
        for books in self.list_books:
            print(books)
    def lend_book(self, user, book):
        if book not in self.lenddict.keys():
            print("Book is available-- You can Take please..")
            self.lenddict.update({book:user})
        else:
            print(f"Book is already taken by {self.lenddict[book]}")
    def addbook(self, book):
        self.list_books.append(book)
        print("Your book has been added ")
    def return_book(self, book):
        self.lenddict.pop(book)
        print("Thank you for returned the book")
tariq = Library("CodeWithTariq", ["Python", "C++", "JavaScript", "Urdu", "Algorithm Development"])
while True:
    print(f"Welcome to {tariq.name} Library")
    print("1 for Display Books")
    print("2 for Lendbook Book")
    print("3 for Addbook Book")
    print("4 for Return Book")
    user_choice = input("Choice from above: ")
    if user_choice == "1":
        tariq.displaybooks()
    elif user_choice == "2":
        user = input("What is your Name: ")
        book = input("Which book do you want: ")
        tariq.lend_book(user, book)
    elif user_choice == "3":
        book = input("Which book do you want to add: ")
        tariq.addbook(book)
    elif user_choice == "4":
        book = input("Which book do you return: ")
        tariq.return_book(book)
    else:
        print("Wrong Input ")
        continue

    user_choice2 = ''
    while user_choice2 != "c" and user_choice2 !="q":
        user_choice2 = input("Enter c to continue q for quit: ")
        user_choice2 = user_choice2.lower()
        if user_choice2 == "c":
            continue
        elif user_choice2 == "q":
            exit()