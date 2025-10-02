def main():
    
    if sudy_nebo_lichy(cislo):
        print("Číslo je dělitelné beze zbytku")
    else:
        print("Číslo není dělitelné beze zbytku")

def sudy_nebo_lichy(cislo):
    cislo = cislo % 2
    if cislo == 1:
        return f"Číslo {cislo} je lichý"
    else:
        return f"Číslo {cislo} je sudé"




if __name__ == "__main__":
    main()