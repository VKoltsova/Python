import csv
import names


# for i in range(10):
#     print(i, names.get_full_name())


# Вариант 1: Генерировать данные на лету, не создавая предварительных списков.
# Вариант 2: Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.
#
#
# Создать пустой empty.csv файл.
file_path = 'D:/QA/git_group26/Python/text_files/'
cvs_file_title = 'empty.csv'

file_title = file_path + cvs_file_title
f = open(file_title, 'w')
f.close()
#
# Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
cvs_file_title_2 = 'digits.csv'
file_title_2 = file_path + cvs_file_title_2

with open((file_title_2), 'w', newline='') as f: #newline - чтобы не пропускать строку
    writer = csv.writer(f)
    for i in range(151):
        row = [i]
        writer.writerow(row)
#
# Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
cvs_file_title_3 = 'names.csv'
file_title_3 = file_path + cvs_file_title_2

with open((file_title_3), 'w', newline='') as n:
    writer = csv.writer(n)
    for i in range(100):
        row = [names.get_last_name()]
        writer.writerow(row)
#
# Вариант 1. Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
cvs_file_title_4 = 'emals.csv'
file_title_4 = file_path + cvs_file_title_4

with open((file_title_4), 'w', newline='') as e:
    writer = csv.writer(e)
    for i in range(100):
        row = [f'{names.get_last_name().lower()}@gmail.com']
        writer.writerow(row)
#
# Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. Имя и часть email до @ должны совпадать.
#
cvs_file_title_5 = 'nne.csv'
file_title_5 = file_path + cvs_file_title_5

with open(file_title_5, 'w', newline='') as n:
    columns = ["Number", "Name", "Email"]
    writer = csv.DictWriter(n, fieldnames=columns)
    writer.writeheader()
    for i in range(1, 100):
        nam = names.get_last_name()
        em = f'{nam.lower()}@gmail.com'
        row = {"Number": i, "Name": nam, "Email": em}
        writer.writerow(row)

# Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310
cvs_file_title_6 = 'digits_2.csv'
file_title_6 = file_path + cvs_file_title_6

num = [i for i in range(10, 311)]
with open(file_title_6, 'w', newline='') as f:
    columns = ["Number"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for i in num:
        row = {"Number": i}
        writer.writerow(row)


# Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами
cvs_file_title_7 = 'names_2.csv'
file_title_7 = file_path + cvs_file_title_7

my_names = [names.get_last_name() for _ in range(400)]
with open(file_title_7, 'w', newline='') as f:
    columns = ["Name"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for i in my_names:
        row = {"Name": i}
        writer.writerow(row)


# Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com
#
cvs_file_title_8 = 'emails_2.csv'
file_title_8 = file_path + cvs_file_title_8

mail = '@gmail.com'
emails = [(i.lower()+mail) for i in my_names]
with open(file_title_8, 'w', newline='') as f:
    columns = ["Email"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for i in emails:
        row = {"Email": i}
        writer.writerow(row)

# Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.
#
cvs_file_title_9 = 'nne_2.csv'
file_title_9 = file_path + cvs_file_title_9

names = [names.get_last_name() for i in range(450)]
mails = [i.lower()+mail for i in names]

with open(file_title_9, 'w', newline='') as f:
    columns = ["Number", "Name", "Email"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for i, v in enumerate(names):
        row = {"Number": i+1, "Name": names[i], "Email": mails[i]}
        writer.writerow(row)