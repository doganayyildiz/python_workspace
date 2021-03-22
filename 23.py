#COLLECTIONS MODULE
# import collections yazarak collections modülğü çağrılabilir
from collections import Counter  #bu şekilde sadece collections modülünden counter kısmını çağırmış oluyoruz
import random
list1 = random.sample(range(10),k=4)
list2 = random.sample(range(10),k=4)
list3 = random.sample(range(10),k=4)
list4 = random.sample(range(10),k=4)

liste_listesi = [list1,list2,list3,list4]
liste_toplam = list1 + list2 + list3 + list4

print(liste_listesi) #liste içindeki listeler de birer liste
print(liste_toplam) #listelerin hepsi tek bir liste

for index, liste in enumerate(liste_listesi):
    print('{}. liste \t {}'.format(index+1,liste))

print(Counter("abcdefhartyuıkha")) #hangi harften kaç tane olduğunu gösterir

sarki = """
        yine bana gel
        yana yana yine beni sev
        yine bana gel
        yana yana yine beni sev
        """
print(sarki)
sarki.split()
print(Counter(sarki.split()))