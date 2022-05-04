#Step 1: Make Employee Class
class Employee:
    def __init__(self, first, last, salary):
        self.firstname = first
        self.lastname = last
        self.salary = salary

#Step 2: Make the from_string() fn
# String --> Employee

def from_string(str):
    params = str.split("-")
    #params = ["Pseu","Donym","50000"]
    employee1 = Employee(params[0], params[1], params[2])
    return employee1

emp1 = Employee("Mary", "Sue", 60000)
emp2 = from_string("John-Smith-55000")

print(emp1.salary)
print(emp2.firstname)
