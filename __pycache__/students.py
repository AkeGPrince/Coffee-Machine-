import data
import random

data.emojis

def calcul_mean_name(students):
    len_name = []
    for student in data.students:
        len_name.append(len(student))
        mean_name = sum(len_name) / len(len_name)
    return int(mean_name)

def smart_sentence(student_len,students):
    compare = len(student_len) - calcul_mean_name(data.students)
    if compare == 0:
        sentence = "↗️"
    elif compare > 0:
        sentence = "➡️"
    else:
        sentence = "↘️"
    return sentence

def display_students(students):
    i = 0
    for student in students:
        i += 1
        print(f"{i} - {random.choice(data.emojis)} {student} --> {smart_sentence(student,data.students)}")
        print("*"*30)
    return None

display_students(data.students)
