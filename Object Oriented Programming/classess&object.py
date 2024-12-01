class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee: %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

# Example usage:
emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)

emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
