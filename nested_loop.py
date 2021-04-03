for i in range(3):
    print("i: {}". format(i))
    for j in range(3):
        print("j: {}". format(j))

for baris in range(5):
    for kolom in range(5):
        print("{},{}" .format(baris + 1 , kolom + 1), end=" ")
    print()
tanda print() diatas untuk ngerjadiin formatting jd kolom (kebawah) sedangkan end=" " biar ada baris (kepinggir)

num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)

list_of_lists = [['luffy', 'zoro', 'sanji'],[0, 1, 2],[9.9, 8.8, 7.7]]
for list in list_of_lists:
    print(list)

Apabila ingin mengkases masing2 unit nya maka pake nested loop
list_of_lists = [['luffy', 'zoro', 'sanji'],[0, 1, 2],[9.9, 8.8, 7.7]]
for list in list_of_lists:
    for unit in list:
        print(unit)