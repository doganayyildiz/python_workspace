#Map Fılter Lambda

def karesini_al(x):
    return x**2 #karesini alır
print(karesini_al(5))

sayilar = [*range(1,6)]
print(sayilar)
for index in range(len(sayilar)):
    sayilar[index] = karesini_al(sayilar[index])
print(sayilar)

#---MAP---
sayilar1 = [*range(1,6)]
map(karesini_al,sayilar1)

def cift_sayilari_filtrele(x):
    if x%2==0:
        return x
    else:
        return None
print(cift_sayilari_filtrele(9))

#-------------
sayilar2 = [*range(1,7)]
print([*filter(cift_sayilari_filtrele,sayilar2)])

#---LAMBDA---
sayilar3 = [*range(1,6)]
print(list(map(lambda a: a**2,sayilar3)))