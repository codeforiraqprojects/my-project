class Employee:
    fullname = ""
    age = 0
    IsActive =""
    dept =""
    def __init__(self):
        fullname = input("Enter the Fullname:")
        age = int(input("Enter the Age:"))
        IsActive = input("Enter the IsActive:")
        dept = input("Enter the Dept:")
        self.fullname = fullname
        self.age = age
        self.IsActive = IsActive
        self.dept = dept



class Data(Employee):
    def __init__(self,salary = 0,address = ""):
        self.salary = salary
        self.address = address
        salary = int(input("Enter the Salary:"))
        address = input("Enter the Address:")
    def employee_Info(self):
        super().fullname()
        super().age()
        super().IsActive()
        super().dept()
        print("His name is",self.fullname,"\nHis age is:",self.age,"\nIsActive",self.IsActive,"\ndept",self.dept,"\nSalary is",self.salary,"\nAddress is",self.address)

def emp():
    Age = int(input("Enter the age emp:"))
    if Age < 20:
        print("Beggar than 20")
    elif Age > 50:
        print("smaller than 50")
    else:
        print("refused age")

has1 = Employee()
has = Data()
#has1.fullname
#has1.age
# has1.IsActive
# has1.dept
# has.salary
# has.address
myfile1 = open("FinalProject.py","r")
myfile2 = open("Hassan.txt","w")
for i in myfile1:
    print(i,file=myfile2,end="")