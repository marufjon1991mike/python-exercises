#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 03:43:28 2026

@author: khalievmarufjon
"""

# Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
user = int(input("Son kiriting "))
print(user**2)
print(user**3)

# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga 
# chiqaruvchi dastur 
foydalanuvchi = int(input("Yoshingizni kiriting "))
print(f"{2026-foydalanuvchi}")


# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, 
# ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
son1 = int(input("Birinchi sonni kiriting "))
son2 = int(input("Ikkinchi sonni kiriting "))
print(f"{son1+son2}")
print(f"{son1-son2}")
print(f"{son1*son2}")
print(f"{son1/son2}")