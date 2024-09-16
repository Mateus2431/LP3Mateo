# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:18:56 2024

@author: Alumno
"""
igv = 0.18

#Subtotal
def ObtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def ObtenerTotalconSubtotal(subtotal):
    return subtotal*(1 + igv)

#Total
def ObtenerSubtotalconTotal(total):
    return total/(1 + igv)

def ObtenerIGVconTotal(total):
    return total*(1 - 1/(1+igv))

#IGV
def ObtenerTotalconIGV(IGV):
    return IGV / 0.18

def ObtenerSubtotalconIGV(IGV):
    return IGV*(1 +  1 / 0.18)