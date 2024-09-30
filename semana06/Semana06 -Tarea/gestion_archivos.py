# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:31:20 2024

@author: Alumno
"""

def crear_archivo(nombre_archivo, contenido):
    if not nombre_archivo.endswith('.txt'):
        nombre_archivo += '.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

def eliminar_archivo(nombre_archivo):
    import os
    os.remove(nombre_archivo)

def agregar_contenido_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'at') as archivo:
        archivo.write(contenido)

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'rt') as archivo:
        return archivo.read()

