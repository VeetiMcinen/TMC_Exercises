def row_sums(my_matrix:list):
    for i in my_matrix:
        i.append(sum(i))

my_matrix = [[1, 2], [3, 4]]
row_sums(my_matrix)

print(my_matrix)