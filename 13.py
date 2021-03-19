# enumerate zip ve range

#---RANGE---
print(list(range(10))) #range i bir liste olarak yazdırma

print([*range(10)]) #yukarıdaki kullanım ile aynı

print([*range(2,10,2)]) #2 den başla 10 a kadar 2 şer yaz

for sayi in range(10):
    if sayi == 5:
        print("5 burda")
    elif sayi == 7:
        print("7 burda")
    else:
        print(sayi)

#---ENUMERATE
harfler = ['a','b','c','d','e']
for  harf in enumerate(harfler):
    print(harf)
    
harfler = ['a','b','c','d','e']
for  index,harf in enumerate(harfler): #indeks numaraları ve liste değerlerini birleştirebilir
    print(index, harf)
    
#ZIP
ulkeler = ['TR','FR','DE'] 
siralamalar = range(1,4)
for ulke in zip(ulkeler,siralamalar): 
    print(ulke)
