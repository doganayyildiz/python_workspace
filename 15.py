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

print(bes_dondur())

#Fonksiyonlarda Argumanlar
def sayi_dondur(sayi):
    return sayi
print(sayi_dondur(7))

def dondur(sayi1=100):
    return sayi1
print(dondur(10))

def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b
print(buyuk_sayi_dondur(3,7))

def metin_yazdir(a,b):
    buyuk_sayi = buyuk_sayi_dondur(a,b)
    sablon_metin = "{} daha buyuk sayidir.".format(buyuk_sayi)
    print(sablon_metin)
print(metin_yazdir(2,8))

def isim_soyisim_ayir(isim_soyisim):
    isim = isim_soyisim.split()[0]
    soyisim = isim_soyisim.split()[1]
    return isim,soyisim 
a,b = isim_soyisim_ayir("Doganay YILDIZ")
print(a)
print(b)

def isim_birlestir(isim,soyisim):
    return " ".join(["Doganay","YILDIZ"]) #Liste elemanlarını birleştirir

print(isim_birlestir("Doganay","YILDIZ")) #birden fazla isimli durumda hata verecek
                                          #çünkü bu fonksiyonda 2 tane değişken var

#---ARGS---
def isim_birlestirme(*args): # sayısız parametre eklenirken args kullanılır
    return " ".join(args) 
print(isim_birlestirme("Mustafa","Kemal","ATATURK"))

#---kwargs(Key_Words_Arguman)---
def gobek_adi_yazdir(**kwargs):
    if 'gobekadi' in kwargs:
        print(kwargs['gobekadi'])
    else:
        print('Gobek Adi Yok')
        
print (gobek_adi_yazdir(adi="Doganay", gobekadi="robot", soyadi="YILDIZ"))
print (gobek_adi_yazdir(adi="Nikola", soyadi="TESLA"))

#------------