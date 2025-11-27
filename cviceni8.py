class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"Osoba {self.jmeno}, {self.telefon}, {self.email}"

    @property
    def jmeno(self):
        return self.__jmeno
    
    @property
    def telefon(self):
        return self.__telefon
    
    @jmeno.setter
    def jmeno(self, hodnota:str):
        for c in hodnota:    
            if not c.isalpha() and not c.isspace():
                raise InvalidData(f"Chybne zadane jmeno '{hodnota}'")
        self.__jmeno = hodnota

    @telefon.setter
    def telefon(self, hodnota:str):
        if hodnota.len() == 13:
            if hodnota.startswith("+"):
                for c in hodnota:    
                    if not c.isalpha() and not c.isspace():
                        raise InvalidData(f"Chybne zadany telefon '{hodnota}'")
        self.__telefon = hodnota
        


if __name__ == "__main__":
    o1 = Osoba("Vašek", "+420111222333", "ahoj@email.com")
    print(o1)
