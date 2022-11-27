class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1 , y1 = self.coor1
        x2 , y2 = self.coor2   
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5 

    def slope(self):
        x1 , y1 = self.coor1
        x2 , y2 = self.coor2 
        return ((y2 - y1)/(x2 - x1))

coor1 = (3,2)
coor2 = (8,10)

my_line = Line(coor1,coor2)
my_line.distance()
my_line.slope()

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        r = self.radius
        h = self.height
        return (3.14*(r)**2*(h))

    def surface_area(self):
        r = self.radius
        h = self.height
        return (2*(3.14)*r*h + 2*(3.14)*(r)**2)

mycylinder = Cylinder(2,3)
mycylinder.volume()
mycylinder.surface_area()


class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,dep_amount):
        self.balance += dep_amount
        print(f"The Amount ${dep_amount} has been deposited to your bank account. your current balance is {self.balance}")
        
    def withdraw(self,with_amount):
        if with_amount <= self.balance:
            self.balance -= with_amount
            print(f"The Amount ${with_amount} has been credited from your bank account. your current balance is {self.balance}")
        else:
            print("Your account does not have sufficient Funds.")
    def __str__(self):
        return f"Owner: {self.name} \nBalance:{self.balance}"
    
            
account1 = Account("Kaustubh",100)
print(account1)
account1.withdraw(50)
account1.deposit(400)
account1.withdraw(500)
account1.balance