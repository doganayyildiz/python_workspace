#Break Continue ve Pass

#---BREAK---
harfler = ['a','b','c','d','e'] * 100
for index, harf in enumerate(harfler):
    if harf == 'c':
        print ('{} harfi {}. indexte!' .format(harf,index))
        break 

#---CONTINUE---
for sayi in range(1,6):
    if sayi%2==0:
        continue
    print(sayi)
    
#---PASS---
for sayi in range(1,6):
    if sayi%2==0:
        pass
    else:
        print(sayi)
    
