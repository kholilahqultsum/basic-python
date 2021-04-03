# # def times(x):
# #     return 5 * x

# # print(times(6))

# def luas_lingkaran (r):
#     # r = input("Masukkan jari-jari: ")
#     luas = 22/7 * r ** 2
#     return luas

# print(luas_lingkaran(10))

# #kalo pake return dia jadi gausah di dalem def printnya

def grade_list(marks):
    sum_of_grade = sum(marks)
    number_of_grade = len(marks)
    average_of_grade = sum_of_grade / number_of_grade
    return average_of_grade

def score_grade(average_of_grade):
    if average_of_grade >= 80:
        grade = 'A'
    elif average_of_grade >= 60:
        grade = 'B'
    elif average_of_grade >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55, 64, 75, 80, 65]
average_of_grade = grade_list(marks)
print("Your average score is", average_of_grade)
grade = score_grade(average_of_grade)
print ("Your grade is", grade)