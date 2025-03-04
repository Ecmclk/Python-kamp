import math

def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b != 0:
        return a / b
    else:
        return "Bölme hatası: Sıfıra bölünemez!"

def karekok(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Hata: Negatif sayının karekökü alınamaz!"

def us_al(a, b):
    return math.pow(a, b)