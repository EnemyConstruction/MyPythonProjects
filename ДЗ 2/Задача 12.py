def sort_surnames(e):
    return e[0]

def sort_first_mark(e):
    return e[1]

def sort_sum_marks(e):
    return e[1] + e[2] + e[3]

def generate_table(arr, key_sorting, direction):
    temple_arr = sorted(arr, key=key_sorting, reverse=direction)
    surnames_list = list(map(lambda x: x[0], temple_arr))
    string_long = len(max(surnames_list, key=len)) + 3*2
    table = f'{'-'*(string_long + 5 + 2*8)}\n'
    for i in range(len(temple_arr)):
        spaces = (string_long - len(surnames_list[i]))//2
        residue = (string_long - len(surnames_list[i]))%2
        for j in range(len(temple_arr[i])):
            if j == 0:
                if(residue == 0):
                    table += f'|{' '*spaces}{temple_arr[i][0]}{' '*spaces}|'
                elif residue == 1:
                    table += f'| {' '*spaces}{temple_arr[i][0]}{' '*spaces}|'
            else:    
                table += f'  {temple_arr[i][j]}  |'
        table +='\n'
    table += f'{'-'*(string_long + 5 + 2*8)}\n\n'
    print(table)

arr = [["Иванов", 3,5,4], ["Петров", 4, 5, 5], ["Сидоров", 3, 3, 3], ["Николаев", 4, 4, 3]]
generate_table(arr, sort_surnames, False)
generate_table(arr, sort_first_mark, False)
generate_table(arr, sort_sum_marks, True)