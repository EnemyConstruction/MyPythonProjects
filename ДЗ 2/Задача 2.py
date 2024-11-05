names = [
    {
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать"
    },
    {
        0: 'ноль',
        1: 'один',
        2: 'два',
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    },
    {
        1: "десять",
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяноста"
    },
    {
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот", 
        9: "девятьсот"
    },
    [
        "тысяч",
        "миллионов",
        "миллиардов",
        "триллионов",
        "квадриллионов",
        "квинтиллионов"
    ]
]

def len_count(count):
    length = 0
    while count:
        count //= 10
        length += 1
    return length

def translate_to_word(count):
    if count < 0:
        return 'undefined'
    elif count < 9:
        if(count in names[1]):
            return names[1][count]
    elif count < 20:
        if(count in names[0]):
            return names[0][count]
    elif count > 19:
        result = []
        while count > 0:
            levelups = len_count(count) // 3
            local_level = 3 if len_count(count) % 3 == 0 else len_count(count) % 3
            tmp_count = count // pow(10,(len_count(count)-1))
            double_count = count // pow(10,(len_count(count)-2))
            if local_level == 2 and 10 <= double_count <= 19:
                result.append(names[0][double_count])
                local_level -=1
                if levelups > 0:
                    count -= double_count * pow(10,(len_count(count)-2))
                else:
                    count -= double_count
            else:
                result.append(names[local_level][tmp_count])
                count -= tmp_count * pow(10,(len_count(count)-1))
            if levelups > 0 and local_level == 1:
                result.append(names[4][levelups - 1])
        return ' '.join(result)

counts = list(map(lambda s: int(s.strip()), input('Введите числа в строку через пробел: ').split(' ')))
result = ' '.join(list(map(translate_to_word, counts)))
print(result)