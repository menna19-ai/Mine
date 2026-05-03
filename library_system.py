import random
books={}
members={}
def add_new_book(book_name):
    if book_name in books:
        print("Book already exists!")
        return
    books[book_name]="available"
def view_books():
    if len(books)==0:
        print("There is no books!")
        return
    print(books)
def register_new_member(member_name,date):
    if member_name in members:
        print("member already exists!")
        return
    members[member_name]=date
def borrow_book(bookName, member_name):
    if bookName not in books:
        print("Book does not exist in library!")
        return
    if books[bookName] == "unavailable":
        print("Book not available right now")
        return
    books[bookName] = "unavailable"
    if member_name in members:
        members[member_name] += 1
    else:
        members[member_name] = 1
    print("Book borrowed successfully!")  
def return_book(bookName):
    if bookName in books.keys() and books.values() =="available" :
        print("Book is available in the library,please Enter The right name!")
        return
    elif bookName in books.keys() and books.values() =="unavailable" :
        books[bookName]="available"
        print("Book returned sucessfully!")
    else:
        print("This book does not belong to this , library")
def random_book():
    if len(books)==0:
        print("There is no books!")
        return
    randombook=random.choice(list(books.keys()))
    print(randombook)
def statistics():
   def statistics():
    if len(books) == 0:
        print("There is no books!")
        return
    else:
        total = len(books)
        print("Total number of books:", total)
    available = 0
    borrowed = 0
    for status in books.values():
        if status == "available":
            available += 1
        else:
            borrowed += 1
    print("Number of available books:", available)
    print("Number of borrowed books:", borrowed)
    borrowed_percentage = (borrowed / total) * 100
    print("Borrowed %:", borrowed_percentage)
def most_active_member():
    if len(members) == 0:
        print("No members yet!")
        return
    top_member = max(members, key=members.get)
    print("Most active member:", top_member)
    print("Activities:", members[top_member])
while True:
  print("\n====== Library Menu ======")
  print("""
1- Add Book
2- View Books
3- Borrow Book
4- Return Book
5- statistics
0- Exit
""")
  print("==========================")
  choice = input("Enter choice: ")
  if choice == "1":
    add_new_book(input("Book name: "))
  elif choice == "2":
    view_books()
  elif choice == "3":
    borrow_book(input("Book name: "), input("Member name: "))
  elif choice == "4":
    return_book(input("Book name: "))
  elif choice == "5":
    statistics()
  elif choice == "6":
    most_active_member()
  elif choice == "0":
    break
    print("Bye Bye dear reader✨")