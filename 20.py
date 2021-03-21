#Dosya ve Klasör Modülleri 

import os #os modülü ile dosya islemleri yapilir
print(os.getcwd()) #bulunduğun dizini bastirir
print(os.listdir()) #mevcut dizindeki dosya klasorleri bastirir


dosyalar = os.listdir() #mevcut dizindeki dosya isimlerini ekrana yazdir
for eleman in dosyalar:
    print(eleman)
 
os.mkdir('deneme') #(make directory) klasor olusturma

os.rmdir('deneme') #(remove directory) klasor silme
#---Dosya Olusturma---
"""
os.O_RDONLY - Sadece Oku
os.O_WRONLY - Sadece Yaz
os.O_RDWR   - Oku ve Yaz
os.O_CREAT  - Olustur
"""

yeni_dosya = os.open('yeni_dosya.txt',os.O_RDWR | os.O_CREAT)
os.write(yeni_dosya,"Hello World".encode()) #yeni_dosya.txt içine yazi yazma
os.close(yeni_dosya)

yeni_dosya = os.open('yeni_dosya.txt',os.O_RDONLY)
uzunluk = os.stat(yeni_dosya).st_size
icerik = os.read(yeni_dosya,uzunluk) #dosya icerigini okuma
print(icerik.decode()) #decode türkçe karakterleri okur encode byte tipinde veri yazar
os.close(yeni_dosya)

os.unlink('yeni_dosya.txt') #dosya silmek

os.mkdir("deneme_eski")
os.rename("deneme_eski","deneme_yeni") #klsor ismi degistirme

os.rename("1.py","bir.py") #dosya ismi degistirmek icin de kullanilir
