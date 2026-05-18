#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 03:30:19 2026

@author: khalievmarufjon
"""

# Quyidagi mashqlarni bajaring:

# Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini 
# foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha = input("Ko'cha nomini kiriting ")
mahalla = input("Mahalla nomini kiriting ")
tuman = input("Tuman nomini kiriting ")
viloyat = input("Viloyat nomini kiriting ")
# print(f"{kocha.capitalize()} ko'chasi, {mahalla.capitalize()} mahallasi, {tuman.capitalize()} tumani, {viloyat.capitalize()} viloyati")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan 
# yozing
print(f"{kocha.capitalize()} ko'chasi, \n{mahalla.capitalize()} mahallasi, \n{tuman.capitalize()} tumani, \n{viloyat.capitalize()} viloyati")

# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan
#  o'zgaruvchiga yuklang manzilga biz yuqorida o'rgangan title(), upper(), 
#  lower() , capitalize() metodlarini qo'llab ko'ring.