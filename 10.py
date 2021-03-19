#Listede For Dongusu

isimler = ['Randal Schowalter','Lucinda Lehner','Jedidiah Harvey','Karelle Dooley','Guido Gaylord','Carmela Goldner']

for kullanici in isimler:
    print(kullanici)
    
kullanici_sayisi = 0
for kullanici in isimler:
    kullanici_sayisi = kullanici_sayisi + 1
    print(kullanici_sayisi, kullanici)

print(isimler[0])

kullanici_sayisi = 0
for kullanici in isimler:
    kullanici_sayisi = kullanici_sayisi + 1
    ad, soyad = kullanici.split()[0], kullanici.split()[1]
    print('{0}. Kullanicinin adi {1} ve Soyadi {2}'.format(kullanici_sayisi,ad,soyad))

moderator = "Lucinda Lehner"
kullanici_sayisi = 0
moderator_sayisi = 0
for kullanici in isimler:
    
    ad, soyad = kullanici.split()[0], kullanici.split()[1]
    
    if(kullanici == moderator):
        moderator_sayisi +=1
        print('{0}. Moderatorun adi {1} ve Soyadi {2}'.format(moderator_sayisi,ad,soyad))
    else:
        kullanici_sayisi = kullanici_sayisi + 1
        print('{0}. Kullanicinin adi {1} ve Soyadi {2}'.format(kullanici_sayisi,ad,soyad))
    