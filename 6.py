#List ve Set Veri Tipleri

liste = ['a','b','c','d','e']
print (liste)

liste = liste + ['f'] #listeler liste ile birleşirler
print (liste)

print (liste[0]) #listelerdeki indeksleri yazdırma

print (liste[3:5]) #3.indeksten başlayıp 5.indekse kadar yaz.

#liste.append('g') listenin sonuna ekleme yapma
liste.append('g')
print(liste)

#liste.pop() listeden son elemanı atma
liste.pop()
print (liste)

#liste.pop(3) listeden 3. indeksi atar
liste.pop(3)
print (liste) 

sayilar = [123,12321,312,45435,35,345,1,1]
print (sayilar)

sayilar.sort() #küçükten büyüğe sıralama
print (sayilar) 

sayilar.reverse() #büyükten küçüğe sıralama
print (sayilar) 

print(set(sayilar)) #set ile tekrar eden sayılar bir kez yazılır
