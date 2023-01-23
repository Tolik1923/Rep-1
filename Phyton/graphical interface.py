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

from tkinter import *

class bar:
    def __init__(self):
        self.__arr = [
            beer('Львівське Різдвяне', 'ПАТ Карлсберг Україна', "4.4", "21.00" ,  "180"),
            beer('Львівське Кнайпа', 'ПАТ Карлсберг Україна', "4.7", "16.00" ,  "180"),
            beer('Львівське 1715    ', 'ПАТ Карлсберг Україна', "4.5", "16.30" ,  "180"),
            beer('Львівське Cвітле  ', 'ПАТ Карлсберг Україна', "4.6", "16.21" ,  "180"),
            beer('Львівське Портер', 'ПАТ Карлсберг Україна', "4.6", "24.95" ,  "360")]

    def butt1(self):
        w1.withdraw()
        root.deiconify()

    def home(self):
        w2.destroy()
        root.deiconify()   
        
    def v(self):
        global w2 
        w2.destroy()
        w2 = Toplevel(root)
        w2.title("Виводити весь список")
        w2.configure(bg = "#E6E6FA")
        Label3 = Label (w2, text = "\t     Назва\t\t       Виробник\t   Міцність    Ціна    Террмін   ", font = ("Times New Roman", "14", "bold italic"), fg = "#191970", bg = "#E6E6FA")
        Label3.pack()
        arr = ['name', 'manufacturer', 'strength', 'price', 'term']
        for x in self.__arr:
           s = "{0}\t  {1}\t{2}\t{3}\t{4}".format(getattr(x, arr[0]), getattr(x, arr[1]), getattr(x, arr[2]), getattr(x, arr[3]), getattr(x, arr[4]))
           Label2 = Label (w2, text = s, font = ("Times New Roman", "14", "bold italic"), fg = "#2F4F4F", bg = "#E6E6FA")
           Label2.pack()
        button21 = Button(w2, text = "Меню", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.home)
        button21.pack(anchor = 'se')

    def butt2(self):
        root.withdraw() 
        global w2 
        w2 = Toplevel(root)
        w2.title("Виводити весь список")
        w2.configure(bg = "#E6E6FA")
        Label3 = Label (w2, text = "\t     Назва\t\t       Виробник\t   Міцність    Ціна    Террмін   ", font = ("Times New Roman", "14", "bold italic"), fg = "#191970", bg = "#E6E6FA")
        Label3.pack(anchor = "center")
        arr = ['name', 'manufacturer', 'strength', 'price', 'term']
        for x in self.__arr:
           s = "{0}\t  {1}\t{2}\t{3}\t{4}".format(getattr(x, arr[0]), getattr(x, arr[1]), getattr(x, arr[2]), getattr(x, arr[3]), getattr(x, arr[4]))
           Label2 = Label (w2, text = s, font = ("Times New Roman", "14", "bold italic"), fg = "#2F4F4F", bg = "#E6E6FA")
           Label2.pack(anchor = "center")
        button21 = Button(w2, text = "Меню", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.home)
        button21.pack(anchor = 'se')
         
    def butt3(self):
         root.withdraw() 
         global w2, e1, e2, e3, e4, e5
         w2 = Toplevel(root)
         w2.title("Додаємо елементи до списку")
         w2.configure(bg = "#E6E6FA")
         buttonB = Button(w2, text = "Додати", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.b, width=8, height=1)
         buttonB.pack(anchor = 'n')
         l1 = Label(w2, text = "Назва", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l1.pack(anchor = 'w', padx = 20, pady = 5)
         e1 = Entry(w2)
         e1.pack(padx = 20, pady = 5)
         l2 = Label(w2, text = "Виробник", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l2.pack(anchor = 'w', padx = 20, pady = 5)
         e2 = Entry(w2)
         e2.pack(padx = 20, pady = 5)
         l3 = Label(w2, text = "Міцність", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l3.pack(anchor = 'w', padx = 20, pady = 5)
         e3 = Entry(w2)
         e3.pack(padx = 20, pady = 5)
         l4 = Label(w2, text = "Ціна", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l4.pack(anchor = 'w', padx = 20, pady = 5)
         e4 = Entry(w2)
         e4.pack(padx = 20, pady = 5)
         l5 = Label(w2, text = "Термін", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l5.pack(anchor = 'w', padx = 20, pady = 5)
         e5 = Entry(w2)
         e5.pack(padx = 20, pady = 5)
         buttonS = Button(w2, text = "Виводимо?", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.v, width=9, height=1)
         buttonS.pack(anchor = 'se', pady = 10)
         buttonH = Button(w2, text = "Меню", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.home, width=9, height=1)
         buttonH.pack(anchor = 'se', pady = 10)
         
    def b(self):
        new = beer(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
        self.__arr.append(new)

    def butt4(self):
         root.withdraw() 
         global w2, var
         w2 = Toplevel(root)
         w2.title("Додаємо елементи до списку")
         w2.configure(bg = "#E6E6FA")
         l1 = Label(w2, text = "Сортуємо за?", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l1.pack(anchor = "center", padx = 20, pady = 5)
         var = IntVar()
         r1 = Radiobutton(w2, text = "Назвoю", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 0, command = b.c)
         r1.pack(anchor = "w", padx = 20, pady = 5)
         r1.select()
         r2 = Radiobutton(w2, text = "Виробником", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 1, command = b.c)
         r2.pack(anchor = "w", padx = 20, pady = 5)
         r3 = Radiobutton(w2, text = "Міцністю", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 2, command = b.c)
         r3.pack(anchor = "w", padx = 20, pady = 5)
         r4 = Radiobutton(w2, text = "Ціною", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 3, command = b.c)
         r4.pack(anchor = "w", padx = 20, pady = 5)
         r5 = Radiobutton(w2, text = "Терміном", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 4, command = b.c)
         r5.pack(anchor = "w", padx = 20, pady = 5)
         buttonS = Button(w2, text = "Виводимо?", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.v, width=9, height=1)
         buttonS.pack(anchor = 'se', pady = 10)
         buttonH = Button(w2, text = "Меню", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.home, width=9, height=1)
         buttonH.pack(anchor = 'se', pady = 10)
    
    def c(self):
        arr = ['name', 'manufacturer', 'strength', 'price', 'term']
        self.__arr.sort(key=lambda x: getattr(x, arr[var.get()]))
   
    def butt5(self): 
         root.withdraw() 
         global w2, var, e7
         w2 = Toplevel(root)
         w2.title("Видаляємо елементи за заданим атрибутом")
         w2.configure(bg = "#E6E6FA")
         l1 = Label(w2, text = "Атрибут?", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l1.pack(anchor = "center", padx = 20, pady = 5)
         var = IntVar()
         r1 = Radiobutton(w2, text = "Назвoю", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 0)
         r1.pack(anchor = "w", padx = 20, pady = 5)
         r1.select()
         r2 = Radiobutton(w2, text = "Виробником", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 1)
         r2.pack(anchor = "w", padx = 20, pady = 5)
         r3 = Radiobutton(w2, text = "Міцністю", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 2)
         r3.pack(anchor = "w", padx = 20, pady = 5)
         r4 = Radiobutton(w2, text = "Ціною", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 3)
         r4.pack(anchor = "w", padx = 20, pady = 5)
         r5 = Radiobutton(w2, text = "Терміном", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 4)
         r5.pack(anchor = "w", padx = 20, pady = 5)
         l2 = Label(w2, bg = "#E6E6FA")
         l2.pack(anchor = "center", padx = 10)
         l3 = Label(w2, text = "Значення?", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l3.pack(anchor = "center", padx = 20)
         e7 = Entry(w2)
         e7.pack(padx = 20)
         l2 = Label(w2, bg = "#E6E6FA")
         l2.pack(anchor = "center", padx = 10)
         buttonD = Button(w2, text = "Видалити", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.d, width=9, height=1)
         buttonD.pack(anchor = 'se', pady = 10)
         buttonS = Button(w2, text = "Виводимо?", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.v, width=9, height=1)
         buttonS.pack(anchor = 'se', pady = 10)
         buttonH = Button(w2, text = "Меню", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.home, width=9, height=1)
         buttonH.pack(anchor = 'se', pady = 10)

    def d(self):
         arr = ['name', 'manufacturer', 'strength', 'price', 'term']
         for x in self.__arr:
            if getattr(x, arr[var.get()]) == e7.get():
                self.__arr.remove(x)

    def butt6(self): 
         root.withdraw() 
         global w2, var1
         w2 = Toplevel(root)
         w2.title("Видаляємо елементи за заданим індексом")
         w2.configure(bg = "#E6E6FA")
         l1 = Label(w2, text = "Індекс?", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l1.pack(anchor = "center", padx = 20, pady = 5)
         arr = ['name', 'manufacturer', 'strength', 'price', 'term']
         a1 = []
         for x in self.__arr:
            s = "{0}\t  {1}\t{2}\t{3}\t{4}".format(getattr(x, arr[0]), getattr(x, arr[1]), getattr(x, arr[2]), getattr(x, arr[3]), getattr(x, arr[4]))
            a1.append(s) 
         var1 = IntVar()
         var2 = IntVar()
         var3 = IntVar()
         var4 = IntVar()
         var5 = IntVar()
         cb1 = Checkbutton(w2, text = "0 - {0}".format(a1[0]), font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var1, onvalue = 0)
         cb1.pack(anchor = "w", padx = 20, pady = 5)
         cb2 = Checkbutton(w2, text = "1 - {0}".format(a1[1]), font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var1, onvalue = 1)
         cb2.pack(anchor = "w", padx = 20, pady = 5)
         cb3 = Checkbutton(w2, text = "2 - {0}".format(a1[2]), font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var1, onvalue = 2)
         cb3.pack(anchor = "w", padx = 20, pady = 5)
         cb4 = Checkbutton(w2, text = "3 - {0}".format(a1[3]), font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var1, onvalue = 3)
         cb4.pack(anchor = "w", padx = 20, pady = 5)
         cb5 = Checkbutton(w2, text = "4 - {0}".format(a1[4]), font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var1, onvalue = 4)
         cb5.pack(anchor = "w", padx = 20, pady = 5)
         buttonE = Button(w2, text = "Видалити", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.e, width=9, height=1)
         buttonE.pack(anchor = 'se', pady = 10)
         buttonS = Button(w2, text = "Виводимо?", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.v, width=9, height=1)
         buttonS.pack(anchor = 'se', pady = 10)
         buttonH = Button(w2, text = "Меню", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.home, width=9, height=1)
         buttonH.pack(anchor = 'se', pady = 10)

    def e(self):
        self.__arr.pop(var1.get())

    def butt7(self):
         root.withdraw() 
         global w2, var, e8
         w2 = Toplevel(root)
         w2.title("Виводимо всі елементи за заданим атрибутом")
         w2.configure(bg = "#E6E6FA")
         l1 = Label(w2, text = "Атрибут?", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l1.pack(anchor = "center", padx = 20, pady = 5)
         var = IntVar()
         r1 = Radiobutton(w2, text = "Назвoю", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 0)
         r1.pack(anchor = "w", padx = 20, pady = 5)
         r1.select()
         r2 = Radiobutton(w2, text = "Виробником", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 1)
         r2.pack(anchor = "w", padx = 20, pady = 5)
         r3 = Radiobutton(w2, text = "Міцністю", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 2)
         r3.pack(anchor = "w", padx = 20, pady = 5)
         r4 = Radiobutton(w2, text = "Ціною", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 3)
         r4.pack(anchor = "w", padx = 20, pady = 5)
         r5 = Radiobutton(w2, text = "Терміном", font = ("Times New Roman", "14", "bold italic"), bg = "#E6E6FA", variable = var, value = 4)
         r5.pack(anchor = "w", padx = 20, pady = 5)
         l2 = Label(w2, bg = "#E6E6FA")
         l2.pack(anchor = "center", padx = 10)
         l3 = Label(w2, text = "Значення?", bg = "#E6E6FA", font = ("Times New Roman", "14"))
         l3.pack(anchor = "center", padx = 20)
         e8 = Entry(w2)
         e8.pack(anchor = "w", padx = 20)
         l2 = Label(w2, bg = "#E6E6FA")
         l2.pack(anchor = "center", padx = 10)
         buttonS = Button(w2, text = "Виводимо?", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.f, width=9, height=1)
         buttonS.pack(anchor = 'se', pady = 10)
         buttonH = Button(w2, text = "Меню", font = ("Times New Roman", "14", "bold italic"), bg = "#DDA0DD", activebackground = "#FF00FF", command = b.home, width=9, height=1)
         buttonH.pack(anchor = 'se', pady = 10)
         l2 = Label(w2, bg = "#E6E6FA")
         l2.pack(anchor = "center", padx = 10)

    def f(self):
         Label3 = Label (w2, text = "\t     Назва\t\t       Виробник\t   Міцність    Ціна    Террмін   ", font = ("Times New Roman", "14", "bold italic"), fg = "#191970", bg = "#E6E6FA")
         Label3.pack()
         arr = ['name', 'manufacturer', 'strength', 'price', 'term']
         for x in self.__arr:
            if getattr(x, arr[var.get()]) == e8.get():
                s = "{0}\t  {1}\t{2}\t{3}\t{4}".format(getattr(x, arr[0]), getattr(x, arr[1]), getattr(x, arr[2]), getattr(x, arr[3]), getattr(x, arr[4]))
                Label2 = Label (w2, text = s, font = ("Times New Roman", "14", "bold italic"), fg = "#2F4F4F", bg = "#E6E6FA")
                Label2.pack(anchor = "center")

b = bar()
root = Tk()
root.title("Lab10")
root.configure(bg = "#FFFACD")
root.withdraw()

w1 = Toplevel(root)
w1.title("Hello!")
w1.configure(bg = "#E6E6FA")

button1 = Button(w1, text = "Натистіть для початку роботи", bg = "MediumOrchid2", font = ("Times New Roman", "14", "bold italic"), activebackground = 'plum1', command = b.butt1)
button1.pack(anchor = "center", padx = 50, pady = 30)

Label1 = Label (root, text = "Що будемо робити?", font = ("Times New Roman", "14", "bold italic"), fg = "#191970", bg = "#FFFACD")
Label1.pack(anchor = "center")

button2 = Button(root, text = "Виводити весь список", font = ("Times New Roman", "14", "bold italic"), bg = "#40E0D0", activebackground = 'turquoise1', width=38, height=1, command = b.butt2)
button2.pack(anchor = "center", padx = 50, pady = 10)

button3 = Button(root, text = "Додавати елементи до списку", font = ("Times New Roman", "14", "bold italic"), bg = "#40E0D0",  activebackground = 'turquoise1', width=38, height=1, command = b.butt3)
button3.pack(anchor = "center", padx = 50, pady = 10)

button4 = Button(root, text = "Відсортувати список за заданим атрибутом", font = ("Times New Roman", "14", "bold italic"), bg = "#40E0D0",  activebackground = 'turquoise1', width=38, height=1, command = b.butt4)
button4.pack(anchor = "center", padx = 50, pady = 10)

button5 = Button(root, text = "Видаляти елементи за заданим атрибутом", font = ("Times New Roman", "14", "bold italic"), bg = "#40E0D0",  activebackground = 'turquoise1', width=38, height=1, command = b.butt5)
button5.pack(anchor = "center", padx = 50, pady = 10)

button6 = Button(root, text = "Видаляти елемент за заданим індексом", font = ("Times New Roman", "14", "bold italic"), bg = "#40E0D0",  activebackground = 'turquoise1', width=38, height=1, command = b.butt6)
button6.pack(anchor = "center", padx = 50, pady = 10)

button7 = Button(root, text = "Виводити всі елементи за заданим атрибутом", font = ("Times New Roman", "14", "bold italic"), bg = "#40E0D0",  activebackground = 'turquoise1', width=38, height=1, command = b.butt7)
button7.pack(anchor = "center", padx = 50, pady = 10)

root.mainloop()

