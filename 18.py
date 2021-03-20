#Try Except Komutları ile Hata Tedbirleri

def tam_sayi_cevir():
    girdi = input("ondalıklı sayı giriniz: ")
    #print("yuvarlama isleminin sonucu: {}".format(round(float(girdi))))
    #random() ondalıklı sayıları yuvarlar
    try:
        girdi = float(girdi)
        print("yuvarlama sonucu: {}".format(round(girdi)))
    except:
        print("{} girdisi ondalık tipe cevrilemiyor".format(girdi))
tam_sayi_cevir()

#---FINALLY---
def tam_sayi_cevir():
    girdi2 = input("ondalıklı sayı giriniz: ")
    status = ''
    try:
        girdi2 = float(girdi2)
        print("yuvarlama sonucu: {}".format(round(girdi2)))
        status = 'basarili'
    except:
        print("{} girdisi ondalık tipe cevrilemiyor".format(girdi2))
        status = 'basaririsiz'
    finally: #iki sonuçta da tetiklenecek olan kod blogu
        print("Tam sayiya cevirme islemi {} oldu".format(status))
tam_sayi_cevir()
#-----------------------------
def tam_sayi_cevir():
    while True:
        girdi3 = input("ondalıklı sayı giriniz: ")
    
        try:
            girdi3 = float(girdi3)
            print("yuvarlama sonucu: {}".format(round(girdi3)))
            break
        except:
            print("{} girdisi ondalık tipe cevrilemiyor".format(girdi3))
            pass
    
tam_sayi_cevir()

try:
    5+"a"
except TypeError: # TypeEror IndexEror gibi hata tiplerini tanımlayıp hata mesajı verebiliriz
    print("tip hatasi") 

liste = []
try:
    liste[-1]
except IndexError: #Index hatasında verilecek mesaj
    print("liste boş")

dic = {'ad':'Elta',
       'soyad':'Howe',
       'tc':'123456789'
    }
try:
    dic['pass']
except KeyError: #Key hatasında verilecek mesaj
    print("pasaport alanı yok")
    
    