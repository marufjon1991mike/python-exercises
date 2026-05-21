#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 03:29:57 2026

@author: khalievmarufjon
"""

#- ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning 
#ismini kiriting
ismlar = ["Hasan", "Husan", "Ali"]

#- Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
for ism in ismlar:
    print(f"Salom {ism}")
    
#- `sonlar` deb nomlangan ro'yxat yarating va ichiga turli sonlarni 
#yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [1, -3, 4.5, 2]

#- Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib 
#ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini 
#esa almashtiring. 
sonlar[1] = 3
print(sonlar)

#- `t_shaxslar` va `z_shaxslar` degan 2 ta ro'yxat yarating va biriga
# o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa 
#zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = ["amir temur", "charli chaplin", "bobur", "mirzo ulug'bek"]
z_shaxslar = ["jeki chan", "tom kruz", "ozodbek nazarbekov"]

#- Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib 
#(`.pop()`), quyidagi ko'rinishda chiqaring:
print(t_shaxslar.pop())
print(z_shaxslar.pop())

#- `friends` nomli bo'sh ro'yxat tuzing va unga `.append()` yordamida 5-6 
#ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends = []
friends.append("jasur")
friends.append("kamol")
friends.append("jamol")
friends.append("ali")
friends.append("vali")
print(friends)


#- Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni `.remove()` 
#metodi yordamida o'chrib tashlang. 
friends.remove("ali")
print(friends)

#- Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append("salim")
friends.insert(0, "karim")
friends.insert(len(friends)//2, "nayim") # // bo'linmani butun qismini olish 5//2=2
print(friends)

#- Yangi `mehmonlar` deb nomlangan bo'sh ro'yxat yarating.
# `.pop()` va `.append()` metodlari yordamida mehmonga kelgan 
#do'stlaringizning ismini friends ro'yxatidan sug'urib olib, 
#mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmon = friends.pop()
mehmonlar.append(mehmon)
mehmonlar.append("Anora")
print(mehmonlar)











