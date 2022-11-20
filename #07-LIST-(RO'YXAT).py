                     # Dasrda o'tilgan narsalar.

# radius = 10
# ism = "Maxmud"

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narhlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
aralash = ['bir', 'ikki', 3, 4, 5]
bush = []

print(mevalar[0])
print(narhlar[6])
print(aralash[2])
print(mevalar[-1])
print(narhlar[-2])
print(aralash[-3])
# Element O'zgartirish
mevalar[0] = 'Anor'
aralash[3] = 2654123012546153.554125
# Oxiriga Element Qo'shish     .append()
mevalar.append('Uzum')
print(mevalar)
aralash.append('6lt1')
print(aralash)
# Xohlagan joyimizga qo'shish     .insert()
mevalar.insert(0, "banan")
print(mevalar)
narhlar.insert(6, 45300)
print(narhlar)

cars = []
cars.append('Lacetti')
cars.append('Malibu')
cars.append('Tracker')
cars.append('Nexia')
print(cars)
del cars[0]
print(cars)
cars.insert(0, 'Nexia 3')
print(cars)
del cars[1]
print(cars)

# Elementlarni o'chirish nomi bilan     .remove()

hayvonlar = ('it', 'mushuk', 'sigir', 'qo\'y', 'quyuon', 'mushuk')
hayvonlar.remove('mushuk')
print(hayvonlar)
# Demak .remove() metodi eng birinchi (chapdagini) o'chiradi.

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(1)
print(mahsulot)
print(bozorlik)
mahsulot2 = bozorlik.pop()
print(mahsulot2)
# Demak biz .pop() a son kiritmasak oxirgisini oladi
# .pop() = .pop(-1)
# Darsda .append() .insert() del .remove() .pop() 

                    # Mustaqil bajarilgan narsalar

ismlari = ['Hislat', 'Jamshid', 'Sarvar']
print('Salom', ismlari[0], 'bugun futbol nechida?')
print('Salom', ismlari[1], 'bugun ham darvozabon bo\'lasanmi?')
print('Salom', ismlari[2], 'bugun futbol chiqasanmi?')

sonlar = [10, -15, 13.2, -86.3, 66.66, 595]
amal1 = sonlar[1] + sonlar[3]
amal2 = sonlar[0] + sonlar[4]
amal3 = sonlar[5] * sonlar[-2]
amal4 = sonlar[2] / sonlar[5]
print(amal1, '\n', amal2, '\n', amal3, '\n', amal4)

sonlar.append(162)
sonlar.append(-12.5)

sonlar.insert(4, 78.2)
sonlar.insert(8, -563.2)

del sonlar[-2]
del sonlar[7]

sonlar.remove(66.66)
sonlar.remove(595)

son1 = sonlar.pop(3)
son2 = sonlar.pop(0)

print(sonlar)
print(son1)
print(son2)

t_shaxslar = ['Imom al-Buxoriy', 'Aliisher Navoiy', 'Muhammad (s.a.v.)']
z_shaxslar = ['Pongfinity', 'Shavkat Miromonivich Mirziyoyev', 'Bill Gates']
print('Men tarixiy shaxs ', t_shaxslar[2], ' bilan, \nzamonaviy shaxslardan esa ', z_shaxslar[0], 'bilan \nsuhbat qilishni istar edim.')

Friends = [ ]
Friends.append('Shohruh')
Friends.append('Jamshid')
Friends.append('Hislat')
Friends.append('Sarvar')
Friends.append('Sunnat')
Friends.append('Muhammad')

Friends.remove('Shohruh')
Friends.remove('Sunnat')

Friends.append('Aziz')
Friends.append('Sardor')

Friends.insert(0, 'Shamshod')
Friends.insert(0, 'Islom')

Friends.insert(4, 'Ulug\'bek')
Friends.insert(5, 'Nurali')

print(Friends)

mehmonlar = [ ]
mehmonlar.append(Friends.pop(2))
mehmonlar.append(Friends.pop(2))
mehmonlar.append(Friends.pop(2))
mehmonlar.append(Friends.pop(2))
mehmonlar.append(Friends.pop(2))
mehmonlar.append(Friends.pop(2))

print(Friends)
print(mehmonlar)

                    # Javoblar 

#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print(sonlar)

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)

#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('John')
friends.append('Alex')
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove('John')
friends.remove('Alex')
print(friends)

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)
