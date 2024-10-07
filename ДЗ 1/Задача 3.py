class People(object):
     
    def __init__(self, x): 
        self.x = x

    def reverseName(self):
        self.x = ''.join(reversed(self.x))
        return self.x

class Worker(People):
    
    def __init__(self, x, post, salary): 
        self.x = x
        self.post = post
        self.salary = salary

    def __str__(self):
        return f'ФИО: {self.x}\nДолжность: {self.post}\nЗарплата: {self.salary}'
    
    def is_top(self):
        return self.salary > 25000
    
    def is_reversed(self, x2):
        return self.x == x2.x
    

people1 = People('Антон')
people1.reverseName()

people2 = Worker('Павел', 'Кондуктор', 35000)
print(str(people2))
print(people2.is_top())
print(people2.is_reversed(people1))