'''
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!
'''
def ketto():
    if szam > num:
        return f"A nagyobb szám: {szam}"
    elif szam < num:
        return f"A nagyobb szám: {num}"
    else:
        return "A két szám ugyan akkora!"

szam = int(input("Kérem adjon meg egy számot!"))
num = int(input("Kérem adjon meg egy számot!")) 
print(ketto())