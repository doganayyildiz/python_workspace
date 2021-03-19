#Iterable Objelerle For Donguleri

tup1 = (1,3,5,7)

for sayi in tup1:
    print(sayi)
    
liste = [[1,2],[3,4]]

for x,y in liste:
    print(x) # 1 ve 3 
    print(y) # 2 ve 4
    print(x,y) # 1 2 ve 3 4 
    
kullanici = {
    'ad':'Noah',
    'soyad':'Zemlak'
}
print(kullanici.items())
print(kullanici.keys())
print(kullanici.values())

for k,v in kullanici.items():
    print("key:     {}\t value: {}".format(k,v))
    