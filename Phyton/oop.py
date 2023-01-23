class beer:
    def __init__(self, name, manufacturer, strength, price, term):
        self._name = name
        self._manufacturer = manufacturer
        self._strength = strength
        self._price = price
        self._term = term

    def get_list(self):
        return [self.name, self.manufacturer, self.strength, self.price, self.term]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
 
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value  

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value

    def __eq__(self, y):  
        return self._term == y

    def __gt__(self, y):
        return self._term > y

    def __lt__(self, y):
        return self._term < y

    def __ne__(self, y):  
        return y != self._term

    def __le__(self, y):  
        return y <= self._term

    def __ge__(self, y):  
        return y >= self._term
 
class bar:
    def __init__(self):
        self.__arr = [
            beer('�������� г������', '��� ��������� ������', 4.4, 21.00 ,  180),
            beer('�������� ������  ', '��� ��������� ������', 4.7, 16.00 ,  180),
            beer('�������� 1715    ', '��� ��������� ������', 4.5, 16.30 ,  180),
            beer('�������� C����  ', '��� ��������� ������', 4.6, 16.21 ,  180),
            beer('�������� ������  ', '��� ��������� ������', 4.6, 24.95 ,  360)]

    def action(self):
        print()
        print("�������� �쳺")
        print("1 - ������� ���� ������.\n2 - �������� �������� �� ������. \n3 -  ³���������� ������ �� ������� ���������. \n4 -  �������� �������� �� ������� ���������. \n5 -  �������� ������� �� ������� ��������. \n6 -  �������� �� �������� �� ������� ���������. \n7 - ������������. \n8 - ĳ������� �� � ����� � ������")
        m = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
        while True:
            try:
                self.__z = int(input("�� ������ ������?  "))
                l = m[z]
                break
            except ValueError:
                print("������ ����� � ������")
            except IndexError:
                print("������ ����� � ������")
        return self.__z

    def v(self):
        print("1 - ����� + enter   2 - ����")
        self.__v = str(input(""))
        if self.__v == " ":
            b.a()

    def a(self):
        print()
        arr = ['name', 'manufacturer', 'strength', 'price', 'term']
        for x in self.__arr:
            print("{0}\t{1}\t{2}\t{3}\t{4}".format(getattr(x, arr[0]), getattr(x, arr[1]), getattr(x, arr[2]), getattr(x, arr[3]), getattr(x, arr[4])))
    
    def b(self):
        print()
        try:
            new = beer(str(input('�����: ')),
            str(input('��������: ')),
            float(input('̳�����: ')),
            float(input('ֳ��: ')),
            int(input('����� ��������� � ����: ')))
        except ValueError:
            print("������� �� ������� ���")
            b.action()
        self.__arr.append(new)
        print("������� ��������� ������?")
        b.v()

    def c(self):
        print()
        m = [1, 2, 3, 4, 5, 6]
        while True:
            try:
                print('��������: 1-�����   2-��������   3-̳�����   4-ֳ��   5-����� ')
                self.__j = int(input("�� ���� �������� �������? "))
                l = m[self.__j]
                break
            except ValueError:
                print("����� ����� � ������")
            except IndexError:
                print("����� ����� � ������")
        self.__j -= 1
        arr = ['name', 'manufacturer', 'strength', 'price', 'term']
        self.__arr.sort(key=lambda x: getattr(x, arr[self.__j]))
        print("������� ������������ ������?")
        b.v()
        
    def d(self):
        print()
        m = [1, 2, 3, 4, 5, 6]
        while True:
            try:
                print('��������: 1-�����   2-��������   3-̳�����   4-ֳ��   5-����� ')
                self.__p = int(input("�� ���� �������� ���������? "))
                l = m[self.__p]
                break
            except ValueError:
                print("����� ����� � ������")
            except IndexError:
                print("����� ����� � ������") 
        self.__p -= 1
        if self.__p == 1 or self.__p == 0:
            self.__n = str(input("��������: "))
        if self.__p == 3 or self.__p == 2:
            while True:
                try:
                    self.__n = float(input("��������: "))
                    break
                except ValueError:
                    print("����� �������� � ��������� �������")
        if self.__p == 4:
            while True:
                try:
                    self.__n = int(input("��������: "))
                    break
                except ValueError:
                    print("����� ���� �����")
        arr = ['name', 'manufacturer', 'strength', 'price', 'term']
        for x in self.__arr:
            if getattr(x, arr[self.__p]) == self.__n:
                self.__arr.remove(x)
        print("������� ������������� ������?")
        b.v()
    
    def e(self):
        print("������ ��������, �� ���������?")
        print("���'������, �� ������� �������� ��� � 0")
        m = [1, 2, 3, 4, 5, 6]
        while True:
            try:
                self.__p = int(input("����� "))
                l = m[self.__p]
                break
            except ValueError:
                print("������ ���� �����")
            except IndexError:
                print("����� ����� � ����� ������")
        self.__arr.pop(self.__p)
        print("������� ������������� ������?")
        b.v()

    def f(self):
        print()
        m = [1, 2, 3, 4, 5, 6]
        while True:
            try:
                print('��������: 1-�����   2-��������   3-̳�����   4-ֳ��   5-����� ')
                self.__p = int(input("�� ���� �������� �������? "))
                l = m[self.__p]
                break
            except ValueError:
                print("����� ����� � ������")
            except IndexError:
                print("����� ����� � ������")
        self.__p -= 1
        if self.__p == 1 or self.__p == 0:
            self.__n = str(input("��������: "))
        if self.__p == 3 or self.__p == 2:
            while True:
                try:
                    self.__n = float(input("��������: "))
                    break
                except ValueError:
                    print("����� �������� � ��������� �������")
        if self.__p == 4:
            while True:
                try:
                    self.__n = int(input("��������: "))
                    break
                except ValueError:
                    print("����� ���� �����")
        print()
        arr = ['name', 'manufacturer', 'strength', 'price', 'term']
        for x in self.__arr:
            if getattr(x, arr[self.__p]) == self.__n:
                print("{0}\t{1}\t{2}\t{3}\t{4}".format(getattr(x, arr[0]), getattr(x, arr[1]), getattr(x, arr[2]), getattr(x, arr[3]), getattr(x, arr[4])))

    def g(self):
        term = [item.term for item in self.__arr]
        while True:
            try:
                t = int(input("������ �����: "))
                break
            except ValueError:
                print("����� ���� �����")
        print("����� � � ������" if  t in term else "� ������ ���� ������ ������" )

b = bar()
z = 0
while z != 7:
    z = b.action()
    if z == 1: b.a()
    if z == 2: b.b()
    if z == 3: b.c()
    if z == 4: b.d()
    if z == 5: b.e()
    if z == 6: b.f()
    if z == 8: b.g()
