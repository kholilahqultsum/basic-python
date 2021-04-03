f = open("hello.txt", "a")

# f.write("Apa kabar\n")

# f.write(input("Masukkan email: "))

# f.close()

count = int(input("Berapa banyak email: "))
for i in range(count):
    print("Data ke {}" . format (i+1))
    f.write(str(input("Masukkan email: ")))
     

