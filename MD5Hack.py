# библиотеки

import hashlib # для хеша
import gc # для очистки памяти
import colorama # для цвета
colorama.init()

# переменные

path = ""
md5 = ""
answer = ""
whileanswer = False
done = False

# методы

def Show(): # для показа логотима
    print(bcolors.WARNING + ".88b  d88. d8888b.   ooooo db   db  .d8b.   .o88b. db   dD")
    print("88'YbdP`88 88  `8D  8P~~~~ 88   88 d8' `8b d8P  Y8 88 ,8P'")
    print("88  88  88 88   88 dP      88ooo88 88ooo88 8P      88,8P  ")
    print("88  88  88 88   88 V8888b. 88~~~88 88~~~88 8b      88`8b  ")
    print("88  88  88 88  .8D     `8D 88   88 88   88 Y8b  d8 88 `88. ")
    print("YP  YP  YP Y8888D' 88oobY' YP   YP YP   YP  `Y88P' YP   YD \n")
    print("v1.0 by damiralmaev\n"   + bcolors.ENDC)

def MD5HECH(): # MD5 хешировать
    answer = input("Видете хеш: ")
    h = hashlib.md5(answer.encode('ascii')).hexdigest()
    print(h)

def MD5Hack(): # Взлом md5
    done = False

    path = input("Видете путь к словарю: ")
    file = open(path)
    donestr = ""
    filelines = file.readlines()
    print(bcolors.OKBLUE + "Всего паролей обнаружено: " + str(len(filelines)) + bcolors.ENDC)
    answermd5 = input("Видете хеш md5: ")
    print(bcolors.OKGREEN + "работа началась!" + bcolors.ENDC)
    for line in filelines: # тут наоборот как в C#
        h = hashlib.md5(line.encode('ascii')).hexdigest()
        if h == answermd5:
            done = True
            donestr = line
            print(bcolors.OKGREEN + "Пароль найден! Пароль " + hashlib.md5(line.encode('ascii')).hexdigest() + " " + answermd5 + bcolors.ENDC)
            break
        else:
            print(bcolors.FAIL + "Неверный пароль: " + hashlib.md5(line.encode('ascii')).hexdigest() + " " + answermd5  + bcolors.ENDC)
    
    print(bcolors.OKGREEN + "Подбор закончен" + bcolors.ENDC)
    if done == True:
        print(bcolors.OKGREEN + 'Взлом закончен успешно!')
        print(bcolors.OKGREEN + "ПАРОЛЬ - " + donestr + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Взлом закончен провалом!" + bcolors.ENDC)

def About(): # для показа о программе
    print(bcolors.WARNING + "Автор: Дамир Алмаев Маратович")
    print("мой github - https://github.com/damiralmaev")
    print("Версия программы - 1.0")
    print("Язык программирования - Python" + bcolors.ENDC)

class bcolors: # для цветов
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def  Setting():
	answer = input("Вы подтверждаете это действие?")
	if answer == "ДA".islower:
		print(bcolors.OKGREEN + "Это действие принято!" + bcolors.ENDC)

# сама работа

Show()

while whileanswer == False: # почему-то я сделал наоборот
	print("Дополнительно: Настройки (4)")
    answer = input('Что сделать?\nMD5 хешировать (1), MD5 Attack (2) или "О программе"(3): ')

    # проверка

    if answer == "1":
        MD5HECH()
    elif answer == "2":
        MD5Hack()
    elif answer == "3":
        About()
    elif answer == "3":
    	Setting()
    else:
        print("Ошибка!")

    whileanswer = False
    gc.collect()
    answerwhile = input("Хотите ещё? (Y - да, N - нет или случайные симболы): ")

    # проверка цикла

    if answerwhile.lower() == "y":
        whileanswer = False
    else:
        whileanswer = True

    print("" + bcolors.ENDC)