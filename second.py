def cislo_text(cislo):
    n = int(cislo)

    jednotky = [
        "nula", "jedna", "dva", "tři", "čtyři",
        "pět", "šest", "sedm", "osm", "devět"
    ]
    jedinecne = [
        "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct",
        "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"
    ]
    desitky = [
        "", "", "dvacet", "třicet", "čtyřicet",
        "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]

    if n < 10:
        return jednotky[n]
    elif n < 20:
        return jedinecne[n - 10]
    elif n < 100:
        d = n // 10
        j = n % 10
        if j == 0:
            return desitky[d]
        else:
            return desitky[d] + " " + jednotky[j]
    elif n == 100:
        return "sto"
    else:
        return "číslo mimo rozsah"


if __name__ == "__main__":
    print(cislo_text("0"))    
    print(cislo_text("1"))     
    print(cislo_text("15"))   
    print(cislo_text("25"))   
    print(cislo_text("100"))  
