

class Employee:

    def __init__(self, first, last, pay,):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+ '.'+last + '@company.com'

    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)

emp_1 = Employee('Daniel', 'Galvan', 50000)
emp_2 = Employee('Test','Tester', 40000)
5print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
difference = emp_1.pay - emp_2.pay
print("Employee 1 makes this much more than employee2:\n" + '$' + str(difference))
