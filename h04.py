import turtle
#Harjutus04

# Ringi pindala ja Turtle
# Kirjuta programm, mis kasutab Turtle graafikat joonistamaks ringi ning arvutab ja kuvab konsoolis ringi pindala ja ümbermõõdu.
# Programm küsib kasutajalt ringi raadiuse.
# Kasuta ** operaatorit raadiuse ruudu arvutamiseks ja π väärtusena 3.14.
# Lisa veakontroll, et kontrollida kasutaja sisestatud raadiuse korrektsust.
# Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta
# Näide:
# Kasutaja sisestab: 5
# Programm väljastab konsoolis: Ringi pindala on 78.5 ja ümbermõõt on 31.4
# Turtle graafika joonistab vastava ringi

try:
    r = float(input("Ringi raadius r="))
    s = 3.14 * r ** 2
    p= 2 * 3.14 * r
    print(f"Ringi pindala on {s:0.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r)
except:
    print("Kontrolli sisestust!")
turtle.done()


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

