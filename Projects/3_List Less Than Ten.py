
list_of_tuna = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
tunahan_great_list = []
for i in list_of_tuna:
    k = i - 5
    if k < 0 :
        tunahan_great_list.append(i)

print(tunahan_great_list)