class Sheet:

    def __init__(self, discipline_list, discipline, group):
        self.discipline_list = discipline_list
        while True:
            self.discipline = discipline
            if self.discipline.lower().strip() in self.discipline_list:
                break
            self.discipline = input("Такой дисциплины не существует. Повторите ввод: ").strip()
        self.group = group
        self.dict = {}

    def __str__(self):
        return f'Название экзамена: {self.discipline}\nГруппа: {self.group}'
    
    def put(self, surname, mark):
        self.dict[surname.strip()] = mark

    def get(self, surname):
        return self.dict[surname]
    
    def change(self, surname, mark):
        self.dict[surname] = mark

    def delete(self, surname):
        del self.dict[surname]
    
    def result(self):
        tmp_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        for elem in self.dict:
            if self.dict[elem] in tmp_dict:
                tmp_dict[self.dict[elem]] +=1

        return tuple(tmp_dict.values())
    
    def count(self):
        return len(self.dict)
    
    def names(self):
        keys_list = list(self.dict.keys())
        return keys_list

discipline_list = ['математика', 'литература', 'русский язык', 'химия', 'физика', 'информатика']
maths = Sheet(discipline_list, 'Математика', 'ДПИ23-1с')
print(str(maths))

maths.put('Антошкин', 3)
maths.put('Шеманов', 5)
maths.put('Федосеева', 4)
maths.put('Горохов', 4)
maths.put('Хомякова', 3)
print(str(maths))

print(maths.get('Шеманов'))
print(maths.get('Горохов'))

maths.change('Горохов', 3)
print(str(maths))

maths.delete('Хомякова')
print(str(maths))

print(maths.result())
print(maths.count())
print(maths.names())