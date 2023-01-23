try:
    f = open(r"C:\Users\Користувач\Desktop\Палітєх\Програмування скриптовими\Лаб-8\text.txt", "r", encoding = "cp1251")  
except OSError:
    while True:
        try:
            w = str(input("Введіть шлях: "))
            break
        except ValueError:
            w = str(input("Введіть шлях: "))
    f = open(w)
s = f.readline()
arr = []
while s != "":
    arr.append(s.split(", "))
    s = f.readline()
f.close()

def action():
    print()
    print("Програма вміє")
    print("1 - Вивести весь список.\n2 - Додавати елементи до списку. \n3 -  Відсортувати список за заданим атрибутом. \n4 -  Видаляти елементи за заданим атрибутом. \n5 -  Видаляти елемент за заданим індексом. \n6 -  Виводити всі елементи за заданим атрибутом. \n7 - Закінчуватися. \n8 - Зберегти список у текстовий файл. \n9 - Зберегти список у файл як об’єкт. \n10 - Завантажити список з текстового файлу. \n11 - Завантажити список як об’єкт")
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while True:
        try:
            z = int(input("Що будемо робити?  "))
            l = b[z]
            break
        except ValueError:
            print("Введіть число з списку")
        except IndexError:
            print("Введіть число з списку")
    return z

def a(arr):
    print()
    s = ''
    for i in range(len(arr)):
        for j in range(5):
            s += "%s\t" % (arr[i][j])
        print(s)
        s = ""

def b(arr):
    print()
    try:
        arr.append([str(input('Назва: ')),
            str(input('Виробник: ')),
            str(input('Міцність: ')),
            str(input('Ціна: ')),
            str(input('Термін зберігання в днях: '))])
    except ValueError:
        print("Веденно не коректні дані")
        action()
    print("Вивести відредагований список?")
    print("1 - Так   2 - Ні")
    while True:
        try:
            v = int(input(""))
            break
        except ValueError:
            print("1 - Так   2 - Ні")
    if v == 1:
        print()
        a(arr)

def c(arr):
    print()
    while True:
        try:
            print('Атрибути: 1-Назва   2-Виробник   3-Міцність   4-Ціна   5-Термін ')
            j = int(input("За яким атрибуто сортуємо? "))
            l = arr[0][j - 1]
            break
        except ValueError:
            print("Ведіть число зі списку")
        except IndexError:
            print("Ведіть число зі списку")
    j -= 1
    arr.sort(key=lambda x: x[j]) 
    print("Вивести відредагований список?")
    print("1 - Так   2 - Ні")
    while True:
        try:
            v = int(input(""))
            break
        except ValueError:
            print("1 - Так   2 - Ні")
    if v == 1:
        a(arr)
        
def d(arr):
    print()
    while True:
        try:
            print('Атрибути: 1-Назва   2-Виробник   3-Міцність   4-Ціна   5-Термін ')
            p = int(input("За яким атрибуто видаляємо? "))
            l = arr[0][p - 1]
            break
        except ValueError:
            print("Ведіть число зі списку")
        except IndexError:
            print("Ведіть число зі списку") 
    p -= 1
    n = str(input("Значення: "))
    for el in arr.copy():
        if el[p] == n:
            arr.remove(el)
    print("Вивести відредагований список?")
    print("1 - Так   2 - Ні")
    while True:
        try:
            v = int(input(""))
            break
        except ValueError:
            print("1 - Так   2 - Ні")
    if v == 1:
        a(arr)
    
def e(arr):
    print()
    print("Індекс елементу, що видаляємо?")
    print("Пам'ятаймо, що рахунок почитати сліз з 0")
    while True:
        try:
            print("Індекс елементу, що видаляємо?")
            p = int(input("Рядок "))
            l = arr[0][p - 1]
            break
        except ValueError:
            print("Ведіть число")
        except IndexError:
            print("Індекс вийшов за межі") 
    arr.pop(p)
    print("Вивести відредагований список?")
    print("1 - Так   2 - Ні")
    while True:
        try:
            v = int(input(""))
            break
        except ValueError:
            print("1 - Так   2 - Ні")
    if v == 1:
        a(arr)
        
def f(arr):
    print()
    print('Атрибути: 1-Назва   2-Виробник   3-Міцність   4-Ціна   5-Термін ')
    while True:
        try:
            print("За яким атрибуто виводимо?")
            p = int(input("Рядок "))
            l = arr[0][p - 1]
            break
        except ValueError:
            print("Ведіть число зі списку")
        except IndexError:
            print("Ведіть число зі списку") 
    p -= 1
    n = str(input("Значення: "))
    print()
    s = ''
    for i in range(len(arr)):
        if arr[i][p] == n:
            for j in range(len(arr)):
                s += "%s\t" % (arr[i][j])
            print(s)
            s = ""

def end(arr):
    s =''
    f1 = open(r"C:\Users\Користувач\Desktop\Палітєх\Програмування скриптовими\Лаб-8\text1.txt", "w", encoding = "cp1251") 
    for i in range(len(arr)):
        for j in range(5):
            s += "%s\t" % (arr[i][j]) 
        f1.writelines(s)
        s = ""
    f1.close
    print()
    print("Виконано")

def g(arr):
    import pickle
    s = ''
    f2 = open(r"C:\Users\Користувач\Desktop\Палітєх\Програмування скриптовими\Лаб-8\text2.txt", "wb") 
    for i in range(len(arr)):
        for j in range(5):
            s += "%s\t" % (arr[i][j])
    s1 = [bytes(s, "cp1251")]
    pickle.dump(s1, f1)
    f2.close()
    print()
    print("Виконано")

def h(arr):
    print()
    n = str(input("Введіть шлях: "))
    while True:
        try:
            f3 = open(n, "r", encoding = "cp1251")
            break
        except OSError:
            print("Шлях не знайдено")
            n = str(input("Введіть шлях: "))
    s = f3.readline()
    arr.clear()
    while s != "":
        arr.append(s.split(", "))
        s = f3.readline()
    f3.close()
    print("Виконано")
    print("Вивести прочитаний список?")
    print("1 - Так   2 - Ні")
    while True:
        try:
            v = int(input(""))
            break
        except ValueError:
            print("1 - Так   2 - Ні")
    if v == 1:
        a(arr)

def i(arr):
    import pickle
    print()
    print("Подвойте слеші")
    n = str(input("Введіть шлях: "))
    while True:
        try:
            f4 = open(n, "rb")
            break
        except OSError:
            print("Шлях не знайдено")
            n = str(input("Введіть шлях: "))
    s = pickle.load(f4)
    f4.close()
    print("Виконано")
    print("Вивести прочитаний список?")
    print("1 - Так   2 - Ні")
    while True:
        try:
            v = int(input(""))
            break
        except ValueError:
            print("1 - Так   2 - Ні")
    if v == 1:
        a(arr)

z = 0
while z != 7:
    z = action()
    if z == 1: a(arr)
    if z == 2: b(arr)
    if z == 3: c(arr)
    if z == 4: d(arr)
    if z == 5: e(arr)
    if z == 6: f(arr)
    if z == 7: end(arr)
    if z == 8: end(arr)
    if z == 9: g(arr)
    if z == 10: h(arr)
    if z == 11: i(arr)
