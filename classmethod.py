class Employee:
    name = "ben"
    designation = "sales manager"
    numberofsales = 6
    def hasachivedtarget(self):
        if self.numberofsales>=5:
            print("achieved")
        else:
            print("not achieved")


employeeone=Employee()
print(employeeone.name)
print(employeeone.hasachivedtarget())

numbers=[1,2,3]
da=type(numbers)
print(da)

Employee.name='elsy'
print(employeeone.name)

employeeone.name='john'
print(employeeone.name)
