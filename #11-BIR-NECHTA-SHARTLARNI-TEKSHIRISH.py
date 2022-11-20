                     # Dasrda o'tilgan narsalar.

son = 50
if son < 0:
    print("Manfiy son.")
else:
    print("Musbat son.")

yosh = int(input("Yoshingiz nechida \n>>>"))
if yosh <= 4:
    print("Sizga kirish bepul.")
elif yosh <= 12:
    print("Sizga kirish 5 000 so'm.")
elif yosh <= 18:
    print("Sizga kirish 8 000 so'm")
else:
    print("Sizga kirish 10 000so'm.")

yosh = int(input("Yoshingiz nechida \n>>>"))
if yosh <= 4:
    narh = 0
elif yosh <= 12:
    narh = 5000
elif yosh <= 18:
    narh = 8000
else:
    narh = 10000

if narh == 0:
    print("Sizga kirish bepul.")
else:
    print(f"Sizga kirish {narh} so'm.")

kun = input("Bugun qaysi kun \n>>>")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print("Bugun dam olish kuni.")
else:
    print("Bugun ish kuni.")

kun = input("Bugun qanday kun \n>>>")
harorat = float(input("Havo harorati qanday \n>>>"))
if kun.lower() == "yakshanba" and harorat >= 30:
    print("Cho'milgani kettik!")
elif kun.lower() == "yakshanba" and harorat <= 30:
    print("Uyda dam olamiz!")

kun = input("Bugun qanday kun \n>>>")
harorat = float(input("Havo harorati qanday \n>>>"))
if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30:
    print("Cho'milgani kettik!")
if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat <= 30:
    print("Uyda dam olamiz!")

narh = 15000
choy = True
salat = False

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000
else:
    narh = narh
print(f"Jami {narh} so'm")

narh = 15000 
choy = True
salat = False
non = True
kompot = True
assorti = False
if choy:   
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: 
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti:
    print("Mijoz assorti oldi.")
    narh = narh + 15000    
print(f"Jami {narh} so'm")

# True = 1     False = 0

narh = 15000 
choy = 1
salat = 0
non = 1
kompot = 1
assorti = 1
if choy:   
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: 
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti:
    print("Mijoz assorti oldi.")
    narh = narh + 15000    
print(f"Jami {narh} so'm")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
print('manti' in menu)
print('somsa' in menu)

menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz? \n>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunday ovqat yo\'q')

menu = ['osh','qazonkabob','shashlik','norin','somsa']
print('osh' not in menu)
print('sho\'rva' not in menu)

menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')

menu = ['osh', 'qqazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
if buyurtmalar:
    for taom in buyurtmalar :
        if taom in menu:
            print(f'Menda {taom} bor.')
        else:
            print(f'Kechirasiz, menuda {taom} yo\'q.')

if buyurtmalar:
    print(f"Ro'yxatda {len(buyurtmalar)}ta taom bor.")
else:
    print(f"Ro'yxat bo'sh")

                     # Mustaqil bajarilgan narsalar

juft_son = int(input("Juft son kiriting \n>>>"))
if juft_son % 2 == 0:
    print("Raxmat.")
else:
    print("Bu son juft emas.")

yosh = int(input("Yoshingiz nechida \n>>>"))
if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh <= 18:
    narh = 10000
else:
    narh = 20000

if narh == 0:
    print("Sizga kirish bepul. Kirishingiz mumkin.")
else:
    print(f"Sizga kirish {narh} so'm. To'lang va be'malol muzeyni aylaning.")

a = float(input("Birinchi sonni kiriting \n>>>"))
b = float(input("Ikkinchi sonni kiriting \n>>>"))
if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print("Bu sonlar teng.")


mahsulotlar = ["Pepsi", "Fanta", "Coca-cola", "Lays", "Cheers", "Plumbir", "Xruc team", "Pekariki", "Bliss", "Viko", "Rich"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

for kk in savat:
    if kk in mahsulotlar:
        print(f"Do'konimizda {kk} bor.")
    else:
        print(f"Do'konimizda {kk} yo'q")


mahsulotlar = ["Pepsi", "Fanta", "Coca-cola", "Lays", "Cheers", "Plumbir", "Xruc team", "Pekariki", "Bliss", "Viko", "Rich"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
bor_mahsulotlar = []
mavjud_emas = [] 
for kk in savat:
    if kk in mahsulotlar:
        bor_mahsulotlar.append(kk)
    else:
        mavjud_emas.append(kk)

if mavjud_emas:
    print("Do'konda quyidagi mahsulotlar yo'q: ")
    for kk in mavjud_emas:
        print(kk)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

foydalanuvchilar = ['Pro', 'Alif_gamer', 'titan', 'odilion', 'odiljon']
login_kirit = input("Yangi login tanlang: ")
if login_kirit in foydalanuvchilar:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!") 

son = int(input("Istalgan sonni kiriting: "))
for n in range(2,11):
    if not (son % n ):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

                     # Javoblar

son = float(input("Juft son kiriting: "))
if son%2!=0:
    print('Bu son juft emas.')
else:
    print("Rahmat!")


yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0;
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")


mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")            


mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    

users = ['alisher1983','aziza','yasina','umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")


son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")