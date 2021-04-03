count = int(input("Berapa banyak data: "))
nama_pelanggan = []
umur_pelanggan = []

for i in range(count):
    print("Data ke {}" . format (i+1))
    nama = input("Nama: ")
    umur = int(input("Umur: "))

    nama_pelanggan.append(nama)
    umur_pelanggan.append(umur)
    
for i in range(len(nama_pelanggan)):
    print("Pelanggan: {} dengan usia: {}" . format(nama_pelanggan [i], umur_pelanggan [i]))

# student_name = str(input("nama siswa:"  ))
# marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
# for student in marks:
#     if student_name == student:
#         print(marks[student])
#         break