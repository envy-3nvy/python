#Harjutus 9.13

ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

lugeja = 0
r_kokku = 0
p_kokku = 0

for i in ev_data:
   
    print(f"{i[0]:30} {i[1]:10} {i[2]:10}") #vrominda tulpadena :30 on laius
    if (i[1]).isnumeric()==True:
        r_kokku+=int(i[1])
        p_kokku+=int(i[2])    
        lugeja+=1

print("Autod mis sõidavad 300+")
for i in ev_data:
    if (i[1]).isnumeric()==True:
        if int(i[1]) >= 300:
            print (i[0])

Parim_hinnasuhe = 10000000
Parim_auto = ""

for i in ev_data:
    if (i[1]).isnumeric()==True:
        km_tasu = int(i[2]) / int(i[1])
        if km_tasu<Parim_hinnasuhe:
            Parim_hinnasuhe = km_tasu
            Parim_auto = i[0]

print(f"Parim elektriauto: {Parim_auto}")





print(f"sõidu ulatus keskmine: {r_kokku/lugeja}")
print(f"hind kesmine: {p_kokku/lugeja}")