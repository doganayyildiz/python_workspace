#DATETIME ve TIME MODULE
import datetime
from datetime import date
bugun = date.today()
print(bugun)

dun = date(2021,3,21)
print(dun)
print(bugun-dun)

print(bugun.year)
print(bugun.month)
print(bugun.day)

print(date.isocalendar(bugun)) #yılın kaçıncı haftası haftanın kaçıncı gunu
print(date.weekday(bugun)) #haftanın kaçıncı gunu index numarasını verir

print(date.ctime(bugun))

#---TIME---
from datetime import time
zaman = time(21,15)
print(zaman) #21.dakika 15.saniye

print(zaman.hour)
print(zaman.minute)
print(zaman.second)

dt = datetime.datetime(2020,10,21,5,3)
print(dt)

#---TIME---
import time
print(time.time()) #anlamsız bir sayı çıkar bu sayıyı 60 a bölersek dakika cinsinden... degerler uretebiliriz
 
baslangic_zamani = time.time()
print("baslama zamani:\t{}".format(baslangic_zamani))
time.sleep(5)
bitis_zamani = time.time()
print("bitis zamani:\t{}".format(bitis_zamani))
print("Calısma zamanı: {}".format(bitis_zamani-baslangic_zamani))


 