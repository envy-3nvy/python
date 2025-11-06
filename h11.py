#Harjutus 11 

def sarnased_esitahed(s):
    s1, s2 = s.split(" ")
    if s1[0]==s2[0]:
        return True
    else:
        return False

print(sarnased_esitahed('Vapper Vares'))
print(sarnased_esitahed("Lahe Känguru"))



# def tervita(m, k="maailm"):
#     print("Tere!",k,m)

# def tervita2():
#     return("Hello cosmos!")

# tervita("karin")
# tervita()
# print (tervita2())