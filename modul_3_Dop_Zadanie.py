
def calculate_structure_sum(*data_structure):
    print()
    sum_list = []
    for i in data_structure:
        sum_list += i[0]
    for i in data_structure:
        for key, velues in i[1].items():
            sum_list.append(len(key[0]))
            sum_list.append(velues)
    for i in data_structure:
        for j in i[2][0:1]:
            sum_list.append(j)
        for key_1, velues_1 in i[2][-1].items():
            sum_list.append(len(key_1))
            sum_list.append(velues_1)
    for i in data_structure:
        sum_list.append(len(i[3]))
    for i in data_structure:
        for j_1 in i[4]:
            #print(len(j_1[0]), j_1[0])
            for j_1_1 in j_1:
                for j_1_1_1 in j_1_1:
                    for j_1_1_1_1 in j_1_1_1:
                        if isinstance(j_1_1_1_1, int):
                            sum_list.append(j_1_1_1_1)
                        if isinstance(j_1_1_1_1, str):
                            sum_list.append(len(j_1_1_1_1))
                        if isinstance(j_1_1_1_1, tuple):
                            for j_1_1_1_1_1 in j_1_1_1_1:
                                if isinstance(j_1_1_1_1_1, str):
                                    sum_list.append(len(j_1_1_1_1_1))
                                if isinstance(j_1_1_1_1_1, int):
                                    sum_list.append(j_1_1_1_1_1)
                                #print('Итоговый sum_list', sum_list, sum(sum_list))
    return print(sum(sum_list))






result = calculate_structure_sum([[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])])

