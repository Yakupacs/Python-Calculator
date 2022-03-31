from cgitb import text
from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))

hesap = 5
s1 = 0

def islemler(x):
    global hesap
    hesap = x
    global s1                         
    s1 = float(giris.get())
    giris.delete(0, 'end')

s2 = 0

def hesapla():
    global s2
    s2 = float(giris.get())
    global hesap
    sonuc = 0
    if hesap == 0:
        sonuc = s1 + s2
    elif hesap == 1:
        sonuc = s1 - s2
    elif hesap == 2:
        sonuc = s1 * s2
    elif hesap == 3:
        sonuc = s1 / s2
    giris.delete(0, 'end')
    giris.insert(0,str(sonuc))

pencere = Tk()
pencere.geometry("430x470")
pencere.configure(background='#282925')


giris = Entry(font = "Arial 14 bold", width=35, justify=RIGHT)
giris.place(x = 20, y = 20)

b = []

for i in range(1,10):
    b.append(Button(text=str(i),font="Arial 30 bold",fg='white', width=3, command=lambda x=i:yaz(x)))

sayac = 0

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x = 22 + j * 100, y = 60 + 100 * i)
        b[sayac].configure(background='black')
        sayac += 1

islem = []

for i in range(0,4):
    islem.append(Button(font='Arial 30 bold',fg='white', width=3, command = lambda x = i : islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-" 
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(0,4):
    islem[i].place(x = 322, y= 60 + 100 * i)
    islem[i].configure(background='#191A18')

altSatir = []

sb = Button(text = "0", font = "Arial 30 bold",fg='white', width=3, command = lambda x=0:yaz(x))
nb = Button(text = ".", font = "Arial 30 bold",fg='white', width=3, command = lambda x=".":yaz(x))
eb = Button(text = "=", font = "Arial 30 bold",fg='white', width=3, command = hesapla)
eb.configure(background='#191A18')
nb.configure(background='#191A18')
sb.configure(background='#191A18')

altSatir.append(sb)
altSatir.append(nb)
altSatir.append(eb)

for i in range(0,3):
    altSatir[i].place(x = 22 + 100 * i, y= 360)

pencere.mainloop()