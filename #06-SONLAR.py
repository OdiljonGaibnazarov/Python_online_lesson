                     # Dasrda o'tilgan narsalar.
a = 20
b = 5.5
temp = 36.6
print(type(a))
print(type(temp))
aholi_soni = 7_594_376_567
print("aholil soni: ", aholi_soni)

x, y, z = 10, 5.6, -23.5
print(x, "\n", y, "\n", z)

c = a*b
print(c)

d = 100/2
print(d, type(d))

radius = 20
PI = 3.14159
diametr = radius * 2
print("Aylana uzunligi =", PI*diametr)

ism = "Jobir"
yosh = 36
xabar = ism + " " + str(yosh) + " yoshda"
print(xabar)

t_yil = int(input("Tug'ilgan yilingizni kiriting >>> "))
yosh = 2022 - t_yil
print("Siz ", yosh, 'yoshda ekansiz.')

a = int("10")
b = float('10')
temp = str(36.6)
                     # Mustaqil bajarilgan narsalar
son = int(input("Istalgan sonni kiriting: \n>>>"))
kvadrati = son * son
kubi = son * son * son
print(son, 'ning kvadrati ', kvadrati, 'ga teng.', '\n', son, "ning kubi ", kubi, 'ga teng.')

yosh = int(input("Yoshingiz nechida: \n >>>"))
yil = 2022 - yosh
print('Siz', yil, "da tug'ilgansiz")

son1 = float(input("Birinchi sonni kiriting: \n>>>"))
son2 = float(input("Ikkinchi sonni kiriting: \n>>>"))
qushish = son1 + son2
print(son1, '+', son2, '=', qushish)
ayirish = son1 - son2
print(son1, '-', son2, '=', ayirish)
kupaytirish = son1 * son2
print(son1, '*', son2, '=', kupaytirish)
bulish = son1 / son2
print(son1, '/', son2, '=', bulish)
                     # Javoblar 
x = int(input("Istalgan son kiriting:\n>>>"))
print(x, " ning kvadrati ", x**2, " ga teng")
print(x, " ning kubi ", x**3, " ga teng")

# Foydalanuvchining yoshini so'rang, 
# va uning tug'ilgan yilini hisoblab, konsolga chiqaring.
yosh = int(input("Yoshingiz nechida? \n>>>"))
t_yil = 2020-yosh
print("Siz ", t_yil, " da tug'ilgansiz")

# Foydalanuvchidan ikki son kiritshni so'rab, 
# kiritilgan sonlarning yig'indisi, ayirmasi, 
# ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print("a+b=", a+b)
print("a-b=", a-b)
print("axb=", a*b)
print("a/b=", a/b)
