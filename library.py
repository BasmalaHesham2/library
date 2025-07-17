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
            print(x.name)
    def search(self,bookname):
        found=False
        found=False
        for x in self.listbook:
            if bookname==x.name :
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
                        found=True
                        x.quantity=x.quantity-1
                        self.borrowedbooks.append(x)
                        print("you have borrowed your book succseffuly")
                        break
                    else : print("the book is sold out")
            if(foundbook==False) : print("Book id isn't avalible pls try again")
        else : print("invalid user id pls try again")

    def returnbook(self,userid,bookid):
        founduser=False
        foundbook=False
        for x in self.borrowinguser:
            if userid==x.id:
                founduser=True
        if founduser:
            for x in self.borrowedbooks:
                if bookid==x.id:
                    foundbook=True
                    x.quantity+=1
                    self.borrowedbooks.remove(x)
                    self.borrowinguser.remove(borrowinguser)
                    break
            if foundbook==False : print("Book id isn't avalible pls try again")
        else : print("invalid user id pls try again")


   
choice = 0
print("=================Welcome to the my library pls enter a the number of your request==========================")
print("1-Add Book\n2-Add User")

   