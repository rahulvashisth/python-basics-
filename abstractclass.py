from abc import ABC, abstractmethod

class employee(ABC):

    @abstractmethod

    def calculate_salary(self, sal):
        pass


#emp_2 = employee()
#emp_2.sal = 10000
#print(emp_2.sal)
#-------if u want to check then uncomment upper three lines and check.
#it will show u the error cant instantiate.
class developer(employee):

    def calculate_salary(self, sal):

        finalsalary = sal * 1.10

        return finalsalary

emp_1= developer()
print(emp_1.calculate_salary(10000))
