

def calculate_structure_sum(data_structure):
    end_sum = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            end_sum += calculate_structure_sum(key)
            end_sum += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            end_sum += calculate_structure_sum(item)
    elif isinstance(data_structure (int, float)):
        end_sum += data_structure
        #end_list().append(data_structure)
    elif isinstance(data_structure, str):
        end_sum += len(data_structure)
        #end_list().append(len(data_structure))

    return end_sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)



