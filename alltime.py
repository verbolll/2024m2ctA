def all_time(file):

    with open(file, 'r') as file:
        lines = file.readlines()

    list_of_lists = []

    for line in lines:
        list_from_line = eval(line.strip())
        list_of_lists.append(list_from_line)

    return list_of_lists