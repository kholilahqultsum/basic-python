pelanggan = {
    "nama": "Lila" ,
    "umur": "21"
}

pelanggan_2 = {
    "nama": "Adam" ,
    "umur": 25
}

# print(pelanggan[])
# print(pelanggan_2)

# pelanggan = ["Lila", "20"]
# print(pelanggan [0])

# print(pelanggan["nama"])
# print(pelanggan["umur"])

# pelanggan_2["umur"] = 17

# print(pelanggan_2["nama"])
# print(pelanggan_2["umur"])

# #Loop through dictionary
# for x in pelanggan:
#     print(x)
#     print(pelanggan[x]) #print values
#     print(pelanggan_2[x])

#list of dictionary
daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

for pelanggan in daftar_pelanggan:
    print("Nama: {} " . format(pelanggan["nama"]))
    print("Umur: {} " . format(pelanggan["umur"]))
