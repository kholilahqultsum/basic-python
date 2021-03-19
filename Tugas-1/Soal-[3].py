a = input("Masukkan nilai teori: ")
c = float(a)
b = input("Masukkan nilai praktik: ")
d = float(b) 
x = 70
if x <= c and x <= d:
    print("Selamat, Anda lulus!")
elif x <= c and x >= d:
    print("Anda harus mengulang ujian praktik")
elif x >= c and x <= d:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktik" )
