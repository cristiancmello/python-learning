# Odds and Ends
# Podemos utilizar uma definição vazia para uma classe.

class Employee:
    pass

john = Employee()

john.name = 'John Doe'
john.salary = 1000

print('Name: {0};\nSalary: {1};'.format(john.name, john.salary))