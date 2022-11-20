                     # Dasrda o'tilgan narsalar.

avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']

for avto in avtolar:
    print(avto.title())

for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())

print(avto)
print(avto == 'bmw')
print(avto == 'hyundai')

a = 10
print(a == 10)
print(a == 5)

ism = 'Ali'
print(ism == 'Ali')
print(ism == 'ali')
print(ism.lower() == 'ali')

a = 5
print(a == 5)
print(a == 6)
print(a != 6)

ism = input("Ismingiz nima? \n>>>")
if ism.lower() != 'ali':
    print(f'Uzr, {ism.title()} biz Alini kutayapmiz.')
else:
    print("Salom, Ali")

javob = float(input("12*6 nechiga teng? \n>>>"))
if javob != 72:
    print("Javob xato.")
else:
    print("To'g'ri javob.")

yosh = int(input("Yoshingiz nechida? \n>>>"))
if yosh >= 18:
    print("Kirishingiz mumkin. MARHAMAT!")
else:
    print("Kirishingiz mumkin emas. Siz hali kichkinasiz.")

login = input("Yangi login kiriting \n>>>")
if len(login) <= 5:
    print("Login 5 ta harfdan ko'proq bo'lishi shart.")
else:
    print("Loginingiz qabul qilindi.")

yil = int(input("Tug'ilgan yilingizni kiriting: \n>>>"))
if 2022-yil < 18:
    print(f"Yoshingiz {2022-yil}da ekan.")
    print("Kirishingiz mumkin emas.")
else:
    print("Xush kelibsiz. Kiring MARHAMAT.")

yosh = int(input("Yoshingizni kiriting \n>>>"))
if yosh > 65:    print("Siz COVID-19 risk guruhuda ekansiz.")

x, y = 25, 50
print("x>y") if x > y else print("x<y")

                     # Mustaqil bajarilgan narsalar

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())

    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login.title()}!")

a = int(input("Birinchi sonni kiriting \n>>>"))
b = int(input("Ikkinchi sonni kiriting \n>>>"))
if a == b :
    print("Sonlar teng ekan.")

son = int(input("Istalgan sonni kiriting \n>>>"))
if son < 0:
    print("Manfiy son.")
else:
    print("Musbat son.")

son1 = int(input("Istalgan sonni kiriting \n>>>"))
if son1 > 0:
    print(f"Bu sonni ildizi {son1**(1/2)}ga teng.")
else:
    print("Musbat sonni kiriting.")

                     # Javoblar 

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car=='gm':
    print(car.upper())
  else:
    print(car.title())

#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car!='gm':
    print(car.title())
  else:
    print(car.upper()) 

#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks xolda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
login = input("Login kiriting: ")
if login.lower() == 'admin':
  print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz {login.title()}!")

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son<0 else print("Son musbat")


#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')

