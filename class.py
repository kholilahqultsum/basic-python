# class MyClass:
#     x = 5


# p1 = MyClass()
# p2 = MyClass()

# print(p1.x)
# print(p2.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greetings(self):
        print("Hello" + self.name)

#kalo class yang paling pertama, itu nilainya fixed, tp class yg kedua memiliki atribut yg beda2
#learnpython.org coba baca disitu

#bikin kodingan yg bisa send ke email kita (for real), trs kalo ka awan dia udh ada template yg otomatis ngirim subjek dan gambar

p1 = Person("Kholilah", 21)
p2 = Person("Adam", 25)

# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)

#penerapannya untuk contoh kasus no telp assign 2 (kelebihannya yaitu lebih well-definded)

p1.greetings()
p2.greetings()