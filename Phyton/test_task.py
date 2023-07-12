import math

def calculate_coordinates_center(a, b, c, d):       #обчислюємо координати центру
    center = []
    for i in range(0, 2):
        center.append(round(((a[i] + d[i] + c[i] + b[i])/4), 2))

    return center

def calculate_side_length(a, b):         #обчислюємо половину довжини сторони квадрата
    distance = round(((math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2))/2), 2)

    return distance

def check(center, distance, point):         #перевіряємо, чи координати точки знаходяться всередині квадрата
    if (abs(point[0] - center[0]) <= distance) and (abs(point[1] - center[1]) <= distance):
        return True
    else:
        return False

def square_check(a, b, c, d):       #перевіряємо, чи задана послідовність утворює квадрат
    if (round(calculate_side_length(a, b))) == (round(calculate_side_length(a, d))) == (round((calculate_side_length(a, c)*math.sqrt(2))/2)):
        return True
    else:
        return False
        
def data_entry():       #приймаємо дані від користувача
    global a, b, c, d, point
    a = []
    while True:
        try:
            print("Введіть координати вершини А")
            a.append(float(input("x: ")))
            a.append(float(input("y: ")))
            break
        except ValueError:
            print("Введіть число")

    b = []
    while True:
        try:
            print("Введіть координати вершини B")
            b.append(float(input("x: ")))
            b.append(float(input("y: ")))
            break
        except ValueError:
            print("Введіть число")

    c = []
    while True:
        try:
            print("Введіть координати вершини C")
            c.append(float(input("x: ")))
            c.append(float(input("y: ")))
            break
        except ValueError:
            print("Введіть число")

    d = []
    while True:
        try:
            print("Введіть координати вершини D")
            d.append(float(input("x: ")))
            d.append(float(input("y: ")))
            break
        except ValueError:
            print("Введіть число")
    
    point = []
    while True:
        try:
            print("Введіть координати точки, що перевіряється")
            point.append(float(input("x: ")))
            point.append(float(input("y: ")))
            break
        except ValueError:
            print("Введіть число")

print("Програма приймає координати вершин квадрата ABCD та точки, розташування якої перевіряється.")
print("Програма повертає дані про розміщення точки відносно квадрата.")
print("Програму написала Захарова Ярина.")
print()

data_entry()
if square_check(a, b, c, d):
    center = calculate_coordinates_center(a, b, c, d)
    distance = calculate_side_length(a, b)
    if check(center, distance, point):
        print("Точка належить квадрату")
    else:
        print("Точка не належить квадрату")
else:
    print("Задана послідовність вершин не утворює квадрат")

