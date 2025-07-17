class Book:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
   
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Admin():
    def __init__(self):
        self.listbook=[]
        self.listuser=[]
        self.borrowinguser=[]
        self.borrowedbooks=[]

    def addbook(self,book):
        self.listbook.append(book)
    def allbooks(self):
        for x in self.listbook:
            if x.quantity>0:
                print(x.name)
    def search(self,bookname):
        found=False
        for x in self.listbook:
            if bookname==x.name and x.quantity>0:
                found=True
                print(f"found the book : {bookname}")
                break
        if(found!=True):
            print(f"{bookname} isn't avalible ")
    
    def adduser(self,user):
        self.listuser.append(user)

    def allusers(self):
        for x in self.listuser:
            print(x.name)
    
    def borrowing(self,bookid,userid):
        founduser=False
        for x in self.listuser:
            if userid==x.id :
                founduser=True
                self.borrowinguser.append(x)
                break
        if founduser:
            foundbook=False
            for x in self.listbook:
                if(bookid==x.id):
                    if(x.quantity>0):
                        foundbook=True
                        x.quantity=x.quantity-1
                        self.borrowedbooks.append(x)
                        print("you have borrowed your book succseffuly")
                        break
                    else : print("the book is sold out")
            if(foundbook==False) : print("Book id isn't avalible pls try again")
        else : print("invalid user id pls try again")

    def returnbook(self,userid,bookid):
        found = False
        for i in range(len(self.borrowinguser)):
            if userid==self.borrowinguser[i].id and bookid==self.borrowedbooks[i].id:
                found=True
                self.borrowedbooks[i].quantity+=1
                self.borrowinguser.pop(i)
                self.borrowedbooks.pop(i)
                print("Book returned succssefully")
                break
        if(found==False): print("invalid user or book id")
                



   

print("=================   Welcome to the my library please enter the number of your request   ==========================")
choice=0
admin=Admin()
while(choice!=8):
    
    print("\n1-Add Book\n2-Add User/n3-print all avalible users\n4-Borrow a book\n5-return a borrowed book\n6-print all books\n7-Search for a book\n8-EXIT")
    choice=int(input())
    match choice:
        case 1:
            name=input("please enter the book name \n")
            id=int(input("please enter the book id\n"))
            q=int(input("please enter the book quantity\n"))
            book=Book(id,name,q)
            admin.addbook(book)
            print("Book added")
        case 2:
            name=input("please enter the user name\n")
            id=int(input("please enter the user id\n"))
            user=User(id,name)
            admin.adduser(user)
            print("user added")
        case 3:
            admin.allusers()
        case 4:
            bookid=int(input("please enter the id of the book\n"))
            userid=int(input("please enter your id\n"))
            admin.borrowing(bookid,userid)
        case 5:
            bookid=int(input("please enter thr book id\n"))
            userid=int(input("please enter your id\n"))
            admin.returnbook(userid,bookid)
        case 6:
            admin.allbooks()
        case 7:
            bookname=input()
            admin.search(bookname)
        case _:
            print("invalid input please try again")

else : print("Thank you for using my system <3")