fileName = input("Введите имя файла: ")
print("Начните вводить строки")

stroki = []
timely = ''

for i in range(999):
    timely = input("> ")

    if timely != '':
        stroki.append(1)
        stroki[i] = timely
    else:
        break

with open(f"{fileName}.txt", "w") as file:
    for i in range(len(stroki)):
        file.write(f"{stroki[i]}\n")

print("Файл записан")