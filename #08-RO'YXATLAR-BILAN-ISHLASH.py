                     # Dasrda o'tilgan narsalar.

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)

cars = ['Bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)
print(sorted(cars))

sonlar = [12, 32, 45, 56, 84, 2, 59, 85, 20, -5, 2.3]
print(sorted(sonlar))
sonlar.sort(reverse=True)
print(sonlar)

sonlar = [12, 32, 45, 56, 84, 2, 59, 85, 20, -5, 2.3]
sonlar.reverse()
print(sonlar)

print(len(sonlar))

raqamlar = list(range(0, 15))
print(raqamlar)

print(list(range(21, 30)))

toq_sonlar = list(range(1, 20, 2))
print(toq_sonlar)

juft_sonlar = list(range(0, 20, 2))
print(juft_sonlar)

sanash = list(range(0, 101, 10))
print(sanash)

max_qiymat = max(toq_sonlar)
print(max_qiymat)

min_qiymat = min(juft_sonlar)
print(min_qiymat)

narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
print(min(narxlar))
print(max(narxlar))
print(sum(narxlar))

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
print(cars[0])
print(cars[4])
print(cars[0:3])
print(cars[2:5])
print(cars[:4])     # print(cars[:4]) = print(cars[0:4])
print(cars[2:])     # print(casr[2:]) = print(cars[2:oxirigacha])

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars     # Hammasini bir xil buladi faqat 2 ta nom bilan
my_cars.remove('volvo')
my_cars[0] = 'Lacetti'

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[:]     # cars[:] = hammasi
my_cars.remove('bmw')
print(cars)
print(my_cars)
# Endi cars bilan my_cars bir xil emas birini o'zgartirsa ikkinchisi o'zgarmaydi.

# TUPLE = o'zgarmas ro'yxat
# TUPLEda [] emas () qo'yiladi

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys)
print(toys[0])
print(toys[-1])
print(toys[2:5])
# toys[0] = 'teddy' 
# print(toys[0])     # Xato berdi chunki TUPLEda o'zgartirib bo'lmaydi
            # Majbur bo'lsak
toys = list(toys) # Endi o'zgartirishimiz mumkin
toys.append('teddy')
print(toys)     # Endi TUPLEga qaytarish kerak
toys = tuple(toys)
print(type(toys))

                    # Mustaqil bajarilgan narsalar

davlatlar = ["O'zbekiston", 'AQSh', 'Angliya', 'Shvetsiya', 'Rossiya', 'Xitoy', 'Qoraqalpog\'iston']

print(len(davlatlar))

print(sorted(davlatlar))

print(sorted(davlatlar, reverse=True))

print(davlatlar)

davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)

davlatlar.sort(reverse=True)
print(davlatlar)

juft_sonlar = list(range(120, 1201, 2))

print(sum(juft_sonlar))

print(max(juft_sonlar) - min(juft_sonlar))

print(len(juft_sonlar))

print(juft_sonlar[:20])
print(juft_sonlar[-20:])
print(juft_sonlar[260:280])

taomlar = ['Osh', 'Shashlik', 'Kasha', 'Shirbirinch', 'KFC']
nonushta = taomlar[:]
nonushta.remove('Osh')
nonushta.remove('Shashlik')
nonushta.remove('KFC')

nonushta.append('Sut')
nonushta.append('Qaymoq')

print(nonushta)
print(taomlar)

nonushta = tuple
# nonushta[0] = "qaymoq va non"     # Demak TUPLEni o'zgartirib bo'lmaydi.

                    # Javoblar 

#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
print(davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

#Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200))

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar))

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(sonlar)-min(sonlar))

#Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"



