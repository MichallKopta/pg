def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"].lower()
    pozice = figurka["pozice"]
    r, s = pozice
    cil_r, cil_s = cilova_pozice

    if not (1 <= cil_r <= 8 and 1 <= cil_s <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    dr = cil_r - r
    ds = cil_s - s

    def cesta_volna():
        step_r = 0 if dr == 0 else dr // abs(dr)
        step_s = 0 if ds == 0 else ds // abs(ds)
        for k in range(1, max(abs(dr), abs(ds))):
            mezi = (r + step_r * k, s + step_s * k)
            if mezi in obsazene_pozice:
                return False
        return True
    if typ == "pěšec":
        if ds == 0:
            if dr == 1 and (r + 1, s) not in obsazene_pozice:
                return True
            if r == 2 and dr == 2 and (r + 1, s) not in obsazene_pozice and (r + 2, s) not in obsazene_pozice:
                return True
        return False

    elif typ == "jezdec":
        return (abs(dr), abs(ds)) in [(2, 1), (1, 2)]

    elif typ == "věž":
        if dr == 0 or ds == 0:
            return cesta_volna()
        return False

    elif typ == "střelec":
        if abs(dr) == abs(ds):
            return cesta_volna()
        return False

    elif typ == "dáma":
        if dr == 0 or ds == 0 or abs(dr) == abs(ds):
            return cesta_volna()
        return False

    elif typ == "král":
        return max(abs(dr), abs(ds)) == 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice)) 
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  