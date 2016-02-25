#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nazwa pliku: ahoj.py

# print 'Ahoj, przygodo!'
# a = 'Witaj w świecie Pythona'
# print a
# print a[0:3]
# c = 1985

# print a[0:5] + repr(c)

# tupla = (0,1,2,"jurek")
# print tupla[3]

# lista = [1,2,3,4,5,6,7,"8"]
# print lista

# # bar = "Zdrabniamy literki"
# # for i in bar:
# # 	print i

# # bar = ["foo", "bar", "yaz"]
# # for i in bar:
# # 	print i

# # print "PETLA"

# # for i  in range (10,100,2):
# # 	print i

# print "SŁOWNIKI"

# bar = {"imie" : "jurek", "nazwisko" : "lepper"}
# # print bar["imie"]

# for i in bar:
# 	print i + " - " +bar[i]

# print bar["imie"]

print "Funkcje"

# def nasza_funkcja(argument1, argument2 = "Koniec"):
# 	global a
# 	argumenty = argument1+" - "+argument2
# 	a = 1
# 	return argumenty

# print nasza_funkcja("Poczatek")
# print a




# suma = 0

# def dodaj (arg1,arg2):
# 	suma = arg1 + arg2
# 	return suma

# print dodaj(3,11)

class auto:
	marka = "nn"
	def __init__ (self):
		self.auto = []
	def dodaj(self,obiekt):
		self.auto.append(obiekt)
	def rozmiar(self):
		return len(self.auto)

s = auto()
s.dodaj("pierwszy wpis")
s.dodaj("drugi wpis")
s.dodaj("trzeci")
print s.rozmiar()
s.marka = "Audi"
print s.marka
del s
	
		