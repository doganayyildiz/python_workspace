#If Sorguları

hava_durumu = "gunesli"

if hava_durumu == "yagisli":
    print("semsisyeni al")
else:
    print("semsiye almana gerek yok")
    
    
if hava_durumu == "gunesli":
    print("Semsiyeni alma")
elif hava_durumu == "yagisli":
    print("semsiyeni al")
else:
    print("sorun yok") 
    
yas = 16

if yas > 18:
    print("Merhaba")
else:
    print("Sen buraya ait degilsin")
    
liste = ['a','b','c','d']

hedef_harf = 'a'

if hedef_harf in liste:
    print("buldum")
else:
    liste.append(hedef_harf)
    
    print("liste eklendin")
    print('Guncel Liste {}'.format(liste))

if (hedef_harf in liste) and hedef_harf == liste[0]:
    print("buldum ve ilk harf konumunda")
elif (hedef_harf in liste):
    print("buldum fakat ilk konumda degil")
else:
    liste.append(hedef_harf)
    
    print("liste eklendin")
    print('Guncel Liste {}'.format(liste))
    