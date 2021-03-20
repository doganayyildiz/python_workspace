#OOP -- NESNE TABANLI PROGRAMLAMA
 
class Ucus():
    havayolu = "THY"
    
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
    
    def __repr__(self):
        return "{} sefer sayili ucus, sistemde olusturulmustur".format(self.kod)

    
    def anons_yap(self):
        return "{} sefer sayili {} - {} ucusumuz {} dakika surecektir.".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure)
    
    def koltuk_sayisi_guncelle(self):
        return self.kapasite - self.yolcu 
        
    def bilet_satis(self,bilet_adedi = 1):
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi 
            self.koltuk_sayisi_guncelle()
            print('{} adet bilet satilmistir. Kalan koltuk sayisi {}'.format(
            bilet_adedi,self.koltuk_sayisi_guncelle()))
        else:
            print("Yetersiz koltuk sayisi")
    
    def bilet_iptal(self,bilet_adedi=1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            print('{} adet bilet iptal edilmistir. guncel koltuk sayisi {}'.format(
                bilet_adedi,
                self.koltuk_sayisi_guncelle()))
        else:
            print('islme gerceklestirilemedi. Iptal edilecek yolcu yok')
             
                 
"""ucus1 = Ucus()
print(ucus1.havayolu)"""

ucus2 = Ucus('TK123','IST','ANK',60,300,50)
print(ucus2.kalkis)
print(ucus2.kod)
print(ucus2.havayolu)

ucus3 = Ucus('TK223','BOD','ANT',40,250,200)
print(ucus3.anons_yap())

print(ucus3.koltuk_sayisi_guncelle())
ucus3.bilet_satis(5)

ucus3.bilet_satis(50)
print(ucus3.koltuk_sayisi_guncelle())

ucus3.bilet_iptal(300)

#---DUNDER METHOD (Double Under Score)---
print(ucus3.__dir__()) #class oluşturulduğunda ona tanımlanan methodlar

print(ucus3) #objenin bellekteki yerini gosterir

class Seyehat():
    def __init__(self,kalkis,varis):
        self.kalkis = kalkis
        self.varis = varis
    
    def anons(self):
        return "{} - {} seyahatine hoşgeldiniz".format(self.kalkis,self.varis)

class Otobus(Seyehat):
    def __init__(self, mola_duraklari,kalkis,varis):
        Seyehat.__init__(self,kalkis,varis)
        self.mola_duraklari = mola_duraklari

seyehat1 = Seyehat('ANK','BOD')
print(seyehat1.anons())

oto1 = Otobus(['FET','ALAN'],'ANT','BOD')
print(oto1.mola_duraklari)
        