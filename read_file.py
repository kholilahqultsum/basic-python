# f = open("hello.txt", "r")

# # print(f.read())

# # #membaca sebagian tulisan
# # print(f.read(5))

# #membaca per baris
# print(f.readline())
# print(f.readline())

# f.close()

file_bio = open("hello.txt", "r+")
teks = file_bio.read()
email_receiver = int(input("Berapa banyak email: "))
for i in range(email_receiver):
    email = input("masukkan alamat email: ")
    teks = "\n {}". format(email)
    file_bio.write(teks)
file_bio.close()