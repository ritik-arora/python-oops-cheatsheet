#Initiate a class
class employee:
    # Special Method / Magic Method / Dunder Method - Constructor
    def __init__(self):
        print("Started Initiating Attributes/Data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/Data have been initiated")

    # Defining a Method
    def printDetails(self):
        print("Id of Employee is : ", self.id)
        print("Salary of Employee is : ", self.salary)
        print("Designation of Employee is : ", self.designation)

    #Defining another Method
    def travel(self, destination):   
        print("travel function was called manually")
        print(f"The employee is travelling to : {destination}")
    
# Creating an Object/Instance of a Class
sam = employee()
#sam.printDetails()
#sam.travel("Kerala")

