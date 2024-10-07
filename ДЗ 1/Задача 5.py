class Student(object):

    def __init__(self, name):
        self.name = name
        self.disciplines = {}

    def  __str__(self):
        return f'Студент {self.name} получил оценки по дисциплинам {", ".join(self.disciplines.keys())}'

    def put(self, discipline, mark):
        self.disciplines[discipline.strip()] = int(mark)
    
    def done(self):
        filtered_dict = {k: v for k, v in self.disciplines.items() if v > 2}
        return filtered_dict
    
stud1 = Student('Шеманов')

stud1.put('математика', 5)
stud1.put('картография', 3)
stud1.put('теория вероятности', 2)
stud1.put('алгоритмы python', 4)
print(str(stud1))
print(stud1.done())