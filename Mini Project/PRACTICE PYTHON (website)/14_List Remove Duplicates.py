# take a list and remove the duplicates elements

list = [1, 3, 5, 6, 4, 3]

def check_duplicates (list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return (new_list)

print (check_duplicates(list))