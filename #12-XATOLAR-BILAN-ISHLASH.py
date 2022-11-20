                     # Dasrda o'tilgan narsalar.
         # IndentationError
# print("Hello world.")     # True
#   print("Hello world.")      # Xato boshida joy tashash kerak emas.
# print("O'ngacha sanaymiz.")
# for n in range(10):
# print(n+1)     # Bunda esa joy tashlash shart chunki undan oldingi qatorda : bor

         # RunTimeError
     # TypeError
son = input("Istalgan son kiriting: ")
print(f"{son} ning kvadrati {son**2} ga teng")     # Xato

son = input("Istalgan son kiriting: ")
son = int(son)
print(f"{son} ning kvadrati {son**2} ga teng")     # To'g'ri
     # NameError
     # ValueError
     # IndexError
     # ZeroDivisionError
         # Mantiqiy xatolar


                     # Mustaqil bajarilgan narsalar

# son = float(input("Juft son kiriting: ")
# if son%2==0:
#     print("Bu son juft emas.')
# else:     # Xato

son = float(input("Juft son kiriting: "))
if son%2==0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")     # True


# yosh = (input("Yoshingiz nechida?"))
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")     # Xato

yosh = int((input("Yoshingiz nechida?")))
if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")     # True


# x = float(input("Birinchi sonni kiriting: ")
# y = float(input("Ikkinchi sonni kiriting: ")
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}")
# else
#     print(f"{x}>{y}")     # Xato

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}')
else:
    print(f"{x}>{y}")     # True


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun'
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# if savat:
#     for mahsulot in savat
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
    # print("Savatingiz bo'sh")     # Xato    

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
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
    print("Savatingiz bo'sh")     # True       


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: '))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahslot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")     # Xato  

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))
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
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")     # True  


# users = ['alisher1983','aziza','yasina' 'umar']
# login = input("Yangi login tanlang:' )
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")     # Xato  

users = ['alisher1983','aziza','yasina' 'umar']
login = input("Yangi login tanlang: ")
if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")


# son = int(input("Istalgan butun son kiriting: "))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")     # True  

son = int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")     # Xato  