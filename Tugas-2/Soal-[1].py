x = ["Selamat Datang!", "---Menu---", "1. Daftar Kontak", "2. Tambah Kontak", "3. Keluar"]
y = ["Selamat Datang!", "---Menu---", "1. Daftar Kontak", "2. Tambah Kontak", "3. Keluar"] 
daftarkontak = 1
tambahkontak = 2
keluar = 3

kontak_1 = {
        "Nama": "Farhan" ,
        "NoTelepon": "08123456789"
    }

kontak_2 = {
        "Nama": "Joko" ,
        "NoTelepon": "08987654321"
    }

daftar_nama = []
daftar_nomor = []
daftar_nama.append(kontak_1["Nama"])
daftar_nomor.append(kontak_1["NoTelepon"])
daftar_nama.append(kontak_2["Nama"])
daftar_nomor.append(kontak_2["NoTelepon"])


while True:
    if x == y:
        for greetings in x:
            print(greetings)

    count = int(input("Pilih Menu: "))

    if count == daftarkontak:
        for kontak in range(len(daftar_nama)):
            print("Nama: {}" . format(daftar_nama[kontak]))
            print("No. Telepon: {}" . format(daftar_nomor[kontak]))

    if count == tambahkontak:
        Nama = (input("Masukkan Nama: "))
        NoTelepon = int(input("Masukkan Nomor: "))
        
        daftar_nama.append(Nama)
        daftar_nomor.append(NoTelepon)

        print("Kontak berhasil ditambahkan!")

    if count == keluar:
        print("Program selesai, sampai jumpa!")
        break

    else:
        print("Menu Tidak Tersedia") 
        

