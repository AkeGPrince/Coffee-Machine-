students = [{"first_name": "Thomas"},
{"first_name": "Nariné"},
{"first_name": "Esperance"},
{"first_name": "Mathieu"},
{"first_name": "Louise"},
{"first_name": "Hémon"},
{"first_name": "Quentin"},
{"first_name": "Chouki"},
{"first_name": "Camille"},
{"first_name": "Django"},
{"first_name": "Marie"},
{"first_name": "Matthieu"},
{"first_name": "Laurendi"},
{"first_name": "Lauriane"},
{"first_name": "Rémy"},
{"first_name": "Hugues"},
{"first_name": "Jérôme"},
{"first_name": "Constance"},
{"first_name": "Leona"},
{"first_name": "Hadi"},
{"first_name": "Michaël"}]


import csv

with open('data/students.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=students[0].keys())
    writer.writeheader()
    for student in students:
          writer.writerow(student)
