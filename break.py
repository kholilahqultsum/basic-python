# for i in range(6):
#     if i == 3:
#         break
#     print(i)

# for i in range(6):
#     if i == 3:
#         break
#     print(i)

text = input("Masukkan text: ")
while True:
    if text == "stop" or text == "end":
        break
    print("text: {}". format(text))
    text = input("Masukkan text: ")
