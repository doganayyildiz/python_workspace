#REGEX MODULE

import re
cumle = "Mustafa Kemal Atatürk, Türk asker, devlet adamı ve Türkiye Cumhuriyeti'nin kurucusudur."

patern = "Türk"
print(re.search(patern,cumle)) #cumle icindeki kelimeyi bulma

durum = re.search(patern,cumle)
print(durum.span())
print(durum.start()) #nerde baslıyor
print(durum.end()) #nerde bitiyor

for eslesme in re.finditer(patern, cumle): # findiet --> herbir eslesmeyi bir objede tutuar
    print(eslesme.span(),eslesme.group())

cumle2 = "Selam, benim telefon numaram 0555-1112233"
#Yukaridaki ornekteki gibi sadece kelime degil de 
#telefon numarasi gibi sıfır ve 3 rakam - 7 rakam seklinde kalıpları bulma

patern = r"\d\d\d\d-\d\d\d\d\d\d\d"
print(re.search(patern,cumle2))