#Harjutus04

#Kingtuste pakkimine

try:
    kingitused = int(input("Lisa kingituste arv: "))
    maht = 5 

    kingitusi_kokku = kingitused // maht #täisarvuline jagamine
    ylejaak = kingitused % maht #jääk

    print(f"Saad teha {kingitusi_kokku} täis kinkekasti. Üle jääb {ylejaak} kingitust.")
except:
    print("Kontrolli sisestust")







#Raamatute allahindlus
ale = 0.3
hind = 12.53
kogus = int(input("sisesta raamatute kogus: "))
summa = (hind-hind*ale)*kogus
print(f"{kogus} raamatu hind soodustusega on {summa:0.2f}€.") #0.2f ümarab 2 kohta





#Aia pikkus 
#kasutaja sisetus ja muudan täisarvuks
a = int(input("Lisa külg 1: "))
b = int(input("Lisa külg 2: "))
p = (a+b)*2
print(f"Aia kogupikkus külgedega {a} ja {b} on {p} meetrit.")

