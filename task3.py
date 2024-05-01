task = {'A': [1, 2, 3, 4], 'B': [], 'C': []}

def sort_func(task):
    for key in task:
        value = task[key]
        print(value)

sort_func(task)