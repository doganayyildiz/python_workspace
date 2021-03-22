#RANDOM ve MATH
#---RANDOM---
import random 
import math 
print(random.__dir__())

print(random.random()) #random 0 ve 1 arasinda bir sayi uretir.

print(random.uniform(5,10)) #uniform ile birlikte istediğimiz aralikta sayi uretiririz

print(random.randint(5,10)) #randint ile tamsayi uretebiliriz

print(random.choice([*range(10)])) #range ile verilen liste icinden rastgele bir sayi secer

print(random.sample(range(10),k=4)) #sample ile range listesinden kaç tane sayı rastgele secilecek gosteriyoruz

liste = [*range(10)]
random.shuffle(liste) #shuffle ile karıstırılmıs bir liste
print(liste)

#---MATH---
print(math.ceil(7.6)) #ceil ile yukarı yuvarlama yapılır
print(math.floor(7.8)) #floor ile asagı yuvarlama yapılır
print(math.factorial(7)) #faktoriyel hesaplama
print(math.pow(3,2)) #3ün karesini alır
print(round(7,1))