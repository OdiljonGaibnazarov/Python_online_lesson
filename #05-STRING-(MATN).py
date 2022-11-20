                     # Dasrda o'tilgan narsalar.
ism = 'Anvar'
shahar = "Qo'qon"
viloyat = "Farg'ona"
matn = 'Men yangi 📱 oldim'
smile = '😆'     # UNICODE bu stikerlar
print(matn)
             # String ustida amallar
ism = 'Ahad'
print ('Mening ismim ' + ism)       

ism = 'Ahad '
Familiya = 'Qayum'
print(ism + Familiya)
             # f-string
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = 'James'
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")
             # Maxsus belgilar
print('Hello world')
print('Hello \tworld')
print('Hello \nworld')
             # String metodlari
ism = 'James'
familiya = 'Bond'
ism_sharif = f'{ism} {familiya}'
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())

meva = '      olma     '
print(meva)
print('Men ' + meva.lstrip() + "yaxshi ko'aman")
print('Men ' + meva.rstrip() + " yaxshi ko'raman")
print('Men ' + meva.strip() + " yaxshi ko'raman")
print('Men ' + meva + "yaxshi ko'raman")
             # INPUT
ism = input('Ismingiz nima?')
print('Assalomu aleykum ' + ism)

ism = input('Ismingiz nima \n>>>')
print('Assalomu aleykum ' + ism.title())
                     # Mustaqil bajarilgan narsalar
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = 'Bodomzor'
viloyat = 'Samarqand'
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati.")

kocha = input("Ko'chamgizni kiriting \n>>>")
mahalla = input("Mahallangizni kiriting \n>>>")
tuman = input("Tumaningizni kiriting \n>>>")
viloyat = input('Viloyatingizni kiriting \n>>>')
print("Siz " + kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyatidansiz!")

kocha= input("Ko'chamgizni kiriting \n>>>")
mahalla = input("Mahallangizni kiriting \n>>>")
tuman = input("Tumaningizni kiriting \n>>>")
viloyat = input('Viloyatingizni kiriting \n>>>')
print("Siz " + kocha + " ko'chasi, \n" + mahalla + " mahallasi, \n" + tuman + " tumani, \n" + viloyat + " viloyatidansiz!")

kocha = input("Ko'chamgizni kiriting \n>>>")
mahalla = input("Mahallangizni kiriting \n>>>")
tuman = input("Tumaningizni kiriting \n>>>")
viloyat = input('Viloyatingizni kiriting \n>>>')
manzil = f"{kocha} {mahalla} {tuman} {viloyat}"
print("Siz " + manzil + "dansiz")

kocha = input("Ko'chamgizni kiriting \n>>>")
mahalla = input("Mahallangizni kiriting \n>>>")
tuman = input("Tumaningizni kiriting \n>>>")
viloyat = input('Viloyatingizni kiriting \n>>>')
manzil = f"{kocha.title()} {mahalla.upper()} {tuman.capitalize()} {viloyat.lower()}"
print("Siz " + manzil + "dansiz")
                     # Javoblari
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")   

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
      tuman + " tumani,\n" + viloyat + " viloyati")

# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())