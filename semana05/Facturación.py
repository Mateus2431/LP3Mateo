# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:27:09 2024

@author: Alumno
"""

import Financieros

subtotal = 800.77

print(f"Subtotal: {subtotal}")

print(f"IGV: {Financieros.ObtenerIGVconSubtotal(subtotal):.2f}")

print(f"Total: {Financieros.ObtenerTotalconSubtotal(subtotal):.2f}")

print("##############################################################")

total = 100

print(f"total: {total}")

print(f"IGV: {Financieros.ObtenerIGVconTotal(total):.2f}")

print(f"Subtotal: {Financieros.ObtenerSubtotalconTotal(total):.2f}")

print("##############################################################")

IGV = 50

print(f"IGV: {IGV}")

print(f"Total: {Financieros.ObtenerTotalconIGV(IGV):.2f}")

print(f"Subtotal: {Financieros.ObtenerTotalconSubtotal(IGV):.2f}")
