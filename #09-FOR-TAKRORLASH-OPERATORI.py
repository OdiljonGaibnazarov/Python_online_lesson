                     # Dasrda o'tilgan narsalar.

mehmonlar = ["Ali", 'Vali', 'Hasan', 'Husan', 'Olim']
print('Salom, ', mehmonlar[0])
print('Salom, ', mehmonlar[1])
print('Salom, ', mehmonlar[2])
for mehmon in mehmonlar:
    print('Salom, ', mehmon)  
    print(f"Hurmatli {mehmon}, sizni 20 dekabr kuni nahorga oshga taklif qiamiz. \nHurmat bilan palonchayevlar oilasi!")

sonlar = list(range(1, 11))
for son in sonlar:
    print(f"{son} ning kvadrati {son **2} ga teng.")

sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)

dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting \n>>>").title())
print(dostlar)
                     # Mustaqil bajarilgan narsalar

ismlar = ['Jamshid', 'Sarvar', 'Hislat', 'Shohruh', 'Xondamir']
for ism in ismlar:
    print('Salom, ', ism)
print('Kod ', len(ismlar), 'marta takrorlandi')

toq_sonlar = list(range(11, 100, 2))
for element in toq_sonlar:
    print(element**3)

kinolar = []
print('Eng yoqtirgan 5 ta kinongizni kiriting.')
for n in range(5):
    kinolar.append(input(f"{n+1}-kinongizni nomini kiriting \n>>>").title())
print('Siz yoqtirgan kinolar bular: ', kinolar)

nechtaligi = int(input('Bugun nechta kishi bilan suhbat qilldingiz \n>>>'))
odamlar = []
for n in range(nechtaligi):
    odamlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi :  ").title())
print(odamlar)

                     # Javoblar 

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Ali','Vali','Hasan','Husan','Olim']
for ism in ismlar:
    print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

# Yuoqirdagi tsikl tugaganidan so'ng, 
# ekranga "Kod n marta takrorlandi" degan xabar chiqaring 
# (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)
