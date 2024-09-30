# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:19:13 2024

@author: Alumno
"""

archivo = open("archivo_de_prueba.txt", "wt")
contenido = "Saludos cordiales\nAtentamente\nDaniel"
archivo.write(contenido)
archivo.close()