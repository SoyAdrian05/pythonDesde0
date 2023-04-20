# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:26:38 2023

@author: Adrian
"""

#Listas y sus métodos

miPrimerLista = [0, 1, 2, 3, 4, 5]

miPrimerLista.append(7)

miPrimerLista.insert(3, 2.5)

len(miPrimerLista)


miSegundaLista = [2, 3, 5, 2, 8, 14, 2, 221]

miSegundaLista.count(2)

miSegundaLista.index(8)

miSegundaLista.sort(reverse = False)


miTerceraLista = ["UPIITA", "Telemática", "Biónica", 21, "Mecatrónica", "3.1416"]

miTerceraLista.pop(1)

miTerceraLista.remove("UPIITA")


#Llenas una lista vacia 

lista_vacia = []

num1 = 1
num2 = 35
num3 = 133412

lista_vacia.append(num1)
lista_vacia.append(num3)
lista_vacia.append(num2)
