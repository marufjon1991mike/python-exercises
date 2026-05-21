#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 03:22:44 2026

@author: khalievmarufjon
"""

#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga 
#chiqaring
davlatlar = ['iroq', 'suriya', 'aqsh', 'xitoy', 'yaponiya']
print(davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga 
#chiqaring
print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse = -1))

# Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa 
#alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse = True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = []
# for son in range(120, 1200):
#     if son % 2 == 0:
#         juft_sonlar.append(son)
# print(juft_sonlar)
juft_sonlar = list(range(120,1201,2))
#print(juft_sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
jami = sum(juft_sonlar)
print(jami)

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang 
#va konsolga chiqaring
min = min(juft_sonlar)
max = max(juft_sonlar)
print(max - min)

# Ro'yxatdagi elementlar sonini hisoblang
uzunlik = len(juft_sonlar)
print(uzunlik)

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga 
#chiqaring
# print(juft_sonlar[: 20])
# print(juft_sonlar[-20 :])
# print((juft_sonlar[280 : 300]))

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'norin', 'shashlik', 'somsa', 'tuxum']

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta  = taomlar[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, 
#va qo'shimcha 2 ta taom qo'shing
nonushta.remove('osh')
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('somsa')
nonushta.append('issiq non')
nonushta.append('qaymoq')


# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring 
nonushta = tuple(nonushta)

#va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta[0] = 'qaymoa va non'