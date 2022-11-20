     # Misol 1

son = int(input("Juft son kiriting \n>>>"))
if son%2 == 0:
    print("Raxmat")
else:
    print("Bu son juft emas.")

    # Misol 2

yosh = int(input("yoshingizni kiriting \n>>>"))
if yosh >= 4 or yosh <= 60:
    narh = 0
elif yosh >= 18:
    narh = 10000
else:
    narh = 20000

if narh == 0:
    print(f"Sizga kirish bepul.")
else:
    print(f"Sizga kirish {narh} so'm.")

    #  Misol 3

a = int(input("Birinchi sonni kiriting \n>>>"))
b = int(input("ikkinchi sonni kiriting \n>>>"))
if  a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")

mahsulotlar = ["Pepsi", "Fanta", "Coca-cola", "Lays", "Cheers", "Plumbir", "Xruc team", "Pekariki", "Bliss", "Viko", "Rich"]
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting : "))

for kerak in savat:
    if kerak in mahsulotlar:
        print(f"Do'konimizda {kerak} bor.")
    else:
        print(f"Do'konimizda {kerak} yoq")

     # Misol 4

mahsulotlar = ["Pepsi", "Fanta", "Coca-cola", "Lays", "Cheers", "Plumbir", "Xruc team", "Pekariki", "Bliss", "Viko", "Rich"]
savat = []
for n in range(5):
    savat.append(input(f" {n+1}-mahsulotni kiriting : "))

mavjud = []
bor_emas = []
for kerak in savat:
    if kerak in mahsulotlar:
        mavjud.append(kerak)
    else:
        bor_emas.append(kerak)
print("Do'konimizda ushbu mahsulotlar yoq \n", bor_emas)

     #  Misol 5
foydalanuvchilar = ['pro', 'alif_gamer', 'titan', 'odilion', 'odiljon']
user = input("Loginingizni kiriting \n>>>")
if user.lower() in foydalanuvchilar:
    print("Bu login tanlangan.")
else:
    print("Raxmat.")

     # Misol 6  
son = int(input("Istalgan butun son kiriting \n>>>"))
for n in range(2, 11):
    if son % n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")