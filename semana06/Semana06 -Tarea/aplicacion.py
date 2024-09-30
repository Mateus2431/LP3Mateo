# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:38:29 2024

@author: Alumno
"""

from gestion_archivos import *

def menu():
    print("Menú")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Agregar contenido")
    print("4. Mostrar contenido de archivo")
    print("5. Salir")

def crear():
    nombre = input("Ingrese el nombre del archivo: ")
    contenido = input("Ingrese el contenido del archivo: ")
    crear_archivo(nombre, contenido)
    print("Archivo creado.")

def eliminar():
    nombre = input("Ingrese el nombre del archivo a eliminar: ")
    eliminar_archivo(nombre)
    print("Archivo eliminado.")

def agregar():
    nombre = input("Ingrese el nombre del archivo: ")
    contenido = input("Ingrese el contenido a agregar: ")
    agregar_contenido_archivo(nombre, contenido)
    print("Contenido agregado.")

def listar():
    nombre = input("Ingrese el nombre del archivo a mostrar: ")
    contenido = leer_archivo(nombre)
    print(contenido)

def salir():
    print("Saliendo del programa.")
    exit()

def error():
    print("Opción no válida.")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear()
        elif opcion == '2':
            eliminar()
        elif opcion == '3':
            agregar()
        elif opcion == '4':
            listar()
        elif opcion == '5':
            salir()
        else:
            error()
