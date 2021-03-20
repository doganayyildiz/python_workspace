#Kullanıcı Girdisi INPUT

def uygulama():
    girdi = input("bir sayi giriniz: ")
    islem = input("tek mi cift mi:")
    if islem == 'cift':
        if int(girdi)%2==0:
            return '{} cift sayi'.format(girdi)
        else:
            return '{} cift sayi degil'.format(girdi)
    elif islem == 'tek':
        if int(girdi)%2==1:
            return '{} tek sayi'.format(girdi)
        else:
            return '{} tek sayi degil'.format(girdi)

print(uygulama())

#Kullanici Girdisini Onaylamak 

def sayi_girdisi_kontrol():
    girdi2 = input("bir sayi giriniz: ")
    if girdi2.isdigit():
        print("bu bir sayi tipi değişken")
    else:
        print("bu bir sayi tipi değişken değil")
sayi_girdisi_kontrol()

def sayi_girdisi_kontrol_dongu():
    girdi3 = input("bir sayi giriniz: ")
    
    while not girdi3.isdigit():
        print("Bu bir sayi değil.")
        girdi3 = input("bir sayi giriniz: ")
    else: 
        print("bu bir sayi")
sayi_girdisi_kontrol_dongu()

def eposta_kontrol():
    girdi4 = input("gecerli bir eposta giriniz: ")
    
    while not (('.' in girdi4) and ('@' in girdi4)):
        print("gecerli eposta adresi degil.")
        girdi4 = input("gecerli bir eposta adresi giriniz: ")
    else: 
        print("Eposta adresi dogru")
eposta_kontrol()