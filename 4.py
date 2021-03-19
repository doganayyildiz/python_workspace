strvar = "python" #string dizi tipinde veri tutar.
print (strvar)

# P | Y | T | H | O | N |
#------------------------
# 0 | 1 | 2 | 3 | 4 | 5 |
# 0 |-5 |-4 |-3 |-2 |-1 |

print (strvar[2]) # 2.indeks
print (strvar[-1]) # son indeks

print (strvar[2:]) #2. indeksten itibaren
print (strvar[:3]) #3. indekse kadar

print (strvar[2:5]) #2.indekseten 5. indekse kadar

print (strvar[1:5:3]) #1.indeksten 5. indekse kadar 3.indeksi atla

len(strvar) #dizi uzunluğu
print (len(strvar)) 

#strvar + " ogren" #diziye ekleme yapar.
print (strvar + " ogren")

#strvar * 5 diziyi 5 kez çoğaltır
print (strvar * 5)

#strvar.upper() büyük harfe çevirir
print(strvar.upper())

#strvar.lower() küçük harfe çevirir
print(strvar.lower())

#strvar.split() belirli bir karakteri atlama
print(strvar.split('o'))



