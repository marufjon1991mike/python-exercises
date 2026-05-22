#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 03:30:39 2026

@author: khalievmarufjon
"""

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi 
# har bir ismga takrorlanuvchi xabar yozing
ismlar = ['abror', 'asror', 'ali', 'vali', 'salim']
for ism in ismlar:
    print(f'Salom {ism.title()}')
    
# Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan 
# xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
n = len(ismlar)
print(f'Kod {n} marta takrorlandi')

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir
#  elementining kubini yangi qatordan konsolga chiqaring.
toq_sonlar = list(range(11,100,2))
for toq_son in toq_sonlar:
    print(f'{toq_son} ning kubi {toq_son**3} ga teng')

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar 
# degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print('5 ta eng sevimli kinolaringizni yozing')
for n in range(5):
    kino = input(f'{n+1}-kino ')
    kinolar.append(kino)
print('\nSevimli kinolaringiz:')
for kino in kinolar:
    print(kino)
    
# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) 
# so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga 
# yozing. Ro'yxatni konsolga chiqaring.
odamlar = []
qty = int(input(f'Bugun nechi kishi bilan suhbatlashdingiz? '))
for n in range(qty):
    odam = input(f'{n+1}-suhbatdoshingizni ismini yozing ')
    odamlar.append(odam)
print('\nSiz bugun suhbatlashgan insonlar:')
for odam in odamlar:
    print(odam.title())
