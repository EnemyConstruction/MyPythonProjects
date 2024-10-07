class Employee(object):

    def __init__(self, name, age, post):
        self.name = name
        self.age = age
        self.post = post
    
    def __str__(self) -> str:
        return f'Работник {self.name} занимает должность {self.post}'


class Teacher(Employee):

    def __init__(self, name, age, disciplines):
        self.name = name
        self.age = age
        self.post = 'Teacher'
        self.disciplines = disciplines

    def __str__(self) -> str:
        return f'Преподаватель {self.name} ведет дисциплины {", ".join(self.disciplines)}'
    
    def add_dis(self, discipline):
        self.disciplines.append(discipline.lower().strip())

    def delete_dis(self, discipline):
        if discipline.lower().strip() in self.disciplines:
            self.disciplines.remove(discipline.lower().strip())
        else:
            print("Такой дисциплины не существует. Попробуйте ещё раз.")

emp1 = Employee('Антон', 35, 'Гастарбайтер')
print(str(emp1))

emp2 = Teacher('Михаил', 28, ['математика', 'теория вероятности'])
print(str(emp2))
emp2.add_dis('картоведение')
print(str(emp2))
emp2.delete_dis('картография')
emp2.delete_dis('картоведение')
print(str(emp2))