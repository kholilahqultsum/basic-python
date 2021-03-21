count = 0
threshold = 3
user: "kholilahqultsum"
password: "123456"

while True: 
    if count == threshold:
        print("Percobaan login melewati batas")
        break
    user_name = input("Masukkan username Anda: ")
    user_pass = input("Masukkan password Anda: ")
    count += 1
    if user_name == user and user_pass == password:
        print("Login berhasil!")
    else:
        print("Username dan Password salah! coba lagi")