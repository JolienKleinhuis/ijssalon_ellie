from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting=prijs*(1-korting)
    uitvoer=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
    return uitvoer

print(aanbieding_1("aardbei",4,0.1))

def inkomsten_totaal(inkomsten,h):
    totaal=0
    for i in inkomsten:
        totaal += i
    btw=h*totaal
    uitvoer=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden."
    return uitvoer
inkomsten = [220,430,125,160,205,90,345]
print(inkomsten_totaal(inkomsten,0.09))

def laag_en_hoog(mijn_lijst):
    uitvoer=[max(mijn_lijst),min(mijn_lijst)]
    return uitvoer
print(laag_en_hoog(inkomsten))

def gemiddelde(mijn_lijst):
    totaal = 0
    for i in mijn_lijst:
        totaal += i
    bedrag = totaal/7
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer
print(gemiddelde(inkomsten))
    
def meervoudig(invoer_lijst):
    uitvoer=laag_en_hoog(invoer_lijst)
    return uitvoer
print(meervoudig(inkomsten))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
