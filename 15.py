#Fonksiyonlar

def bes_bastir(): 
    """
    define kelimesinin kısltılmışı "def"
    def fonksiyon_ismi():
    """
    print(5)
    
bes_bastir()

#---RETURN---
def bes_dondur():
    return 5

bes_dondur()

#Fonksiyonlarda Argumanlar
def sayi_dondur(sayi):
    return sayi
sayi_dondur(7)

def dondur(sayi1=100):
    return sayi1
dondur(10)

def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b
buyuk_sayi_dondur(3,7)
