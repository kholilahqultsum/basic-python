# pelanggan = {
#     "nama": "Lila" ,
#     "umur": "21"
# }

# pelanggan_2 = {
#     "nama": "Adam" ,
#     "umur": "25"
# }

# print(pelanggan)
# print(pelanggan_2)

# pelanggan = ["Lila", "20"]
# print(pelanggan [0])

# print(pelanggan["nama"])
# print(pelanggan["umur"])

# # pelanggan_2["umur"] = 17

# print(pelanggan_2["nama"])
# print(pelanggan_2["umur"])

# #Loop through dictionary
# for x in pelanggan:
#     print(x)
#     print(pelanggan[x]) #print values
#     print(pelanggan_2[x])

#list of dictionary
# daftar_pelanggan = []
# daftar_pelanggan.append(pelanggan)
# daftar_pelanggan.append(pelanggan_2)

# for pelanggan in daftar_pelanggan:
#     print("Nama: {} " . format(pelanggan["nama"]))
#     print("Umur: {} " . format(pelanggan["umur"]))

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict)

# #Accessing items:
# x = thisdict["model"]
# print(x)

# # #Change Value:
# # y = thisdict ["year"] = 2018
# # print(y)

#dictionary kosong
my_dict = {}
#dictionary dengan kunci integer
my_dict = {1: 'apple', 2:'ball'}
#dictionary dengan kunci mixed
my_dict = {'name':'John', 1:[2, 4, 3]}
#using dict()
my_dict = dict({1:'apple', 2:'ball'})
#having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'ball')])

#ACCESING ELEMENTS FROM DICTIONARY

# # get vs [] for retrieving elements
# my_dict = {'name': 'Jack', 'age': 26}

# # Output: Jack
# print(my_dict['name'])

# # Output: 26
# print(my_dict.get('age'))

# # Trying to access keys which doesn't exist throws error
# # Output None
# print(my_dict.get('address'))

# # KeyError
# print(my_dict['address'])

#CHANGING AND ADDING DICTIONARY ELEMENTS
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

#REMOVING ELEMENTS FROM DICTIONARY
