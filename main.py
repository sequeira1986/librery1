'''Cieľ: Správca knižnice je zameraná na vytvorenie jednoduchého systému pre správu knižničných
zdrojov.
Základná štruktúra:
Trieda Kniha:
• Atribúty: názov, autor, ISBN, dostupna (boolean), rok vydania.
• Metódy: konštruktor na nastavenie atribútov,
• konštruktor na nastavenie atribútov
• vypozicat - ak je kniha dostupna zmeni jeho stav na False
• vratit - nastavi hodnotu dostupna na True
Trieda Kniznica:
• Atribúty: zoznam všetkých kníh (môže byť zoznam objektov triedy Kniha)
• Metódy: pridanie knihy do knižnice, vyhľadávanie kníh podľa názvu, vypožičanie knihy(podla ISBN),
vrátenie knihy(podla ISBN), zobrazenie dostupných kníh'''
class Kniha:
    def __init__(self, nazov, autor, isbn, dostupna=True, rok_vydania=None):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.dostupna = dostupna
        self.rok_vydania = rok_vydania

    def vypozicat(self):
        if self.dostupna:
            self.dostupna = False

    def vratit(self):
        self.dostupna = True

    def __str__(self):
        return f"Názov: {self.nazov}, Autor: {self.autor}, ISBN: {self.isbn},  Rok vydania: {self.rok_vydania}"

    def vytvor(self):
        print("Vytváram knihu s názvom", self.nazov, "od autora", self.autor)

class Kniznica:
    def __init__(self):
        self.knihy = []

    def pridaj_knihu(self, kniha):
        self.knihy.append(kniha)

    def vyhladaj_knihu_podla_nazoru(self, nazov):
        for kniha in self.knihy:
            if kniha.nazov.lower() == nazov.lower():
                return kniha
        return None

    def vypozicaj_knihu(self, isbn):
        kniha = self.vyhladaj_knihu_podla_isbn(isbn)
        if kniha is not None:
            kniha.vypozicat()
            return True
        return None

    def vrati_knihu(self, isbn):
        kniha = self.vyhladaj_knihu_podla_isbn(isbn)
        if kniha is not None:
            kniha.vratit()
            return kniha
        return None

    def zobrazi_dostupne_knihy(self):
        for kniha in self.knihy:
            if kniha.dostupna:
                print(kniha.nazov)

    def vytvor_knihu(self, nazov, autor, isbn, dostupna=True, rok_vydania=None):
        kniha = Kniha(nazov, autor, isbn, dostupna, rok_vydania)
        self.knihy.append(kniha)
        kniha.vytvor()
        return kniha

    def vyhladaj_knihy_podla_autora(self, autor):
        knihy = []
        for kniha in self.knihy:
            if kniha.autor == autor:
                knihy.append(kniha)
        return knihy

    def vyhladaj_knihu_podla_isbn(self, isbn):
        for kniha in self.knihy:
            if kniha.isbn == isbn:
                return kniha
        return None

    def vyhladaj_knihy_podla_roku_vydania(self, rok_vydania):
        knihy = []
        for kniha in self.knihy:
            if kniha.rok_vydania == rok_vydania:
                knihy.append(kniha)
        return knihy

    def zaznamena_vypozicu(self, isbn, datum_vypozicu):
        kniha = self.vyhladaj_knihu_podla_isbn(isbn)
        if kniha is not None:
            kniha.datum_vypozicu = datum_vypozicu
        return kniha

    def zaznamena_vratenie(self, isbn, datum_vratenia):
        kniha = self.vyhladaj_knihu_podla_isbn(isbn)
        if kniha is not None:
            kniha.datum_vratenia = datum_vratenia
        return kniha

    def vygeneruj_spravu_o_knizni(self):
        sprava = ""
        sprava += "Zoznam dostupných kníh:"
        for kniha in self.knihy:
            if kniha.dostupna:
                sprava += "\n" + kniha.__str__()
        sprava += "\n\nZoznam všetkých kníh:"
        for kniha in self.knihy:
            sprava += "\n" + kniha.__str__()
        return sprava
kniha = Kniha("Don QUijote", "Miguel de Cervantes", "1245", 1, "1854")
kniha2  = Kniha("Pán prsteňov - Spoločenstvo prsteňa", "J.R.R. Tolkien", "9788", 0, "1555")
kniha3  = Kniha("Trilógia Hry o tróny", "George R.R. Martin", "2837", 1, "1998")

knihovna = Kniznica()
knihovna.pridaj_knihu(kniha)
knihovna.pridaj_knihu(kniha2)
knihovna.pridaj_knihu(kniha3)
knihovna.vypozicaj_knihu("9788")
knihovna.vypozicaj_knihu("1245")
print(kniha)
print(kniha2)
print(kniha3)
knihovna.zobrazi_dostupne_knihy()

kniznica = Kniznica()
kniznica.pridaj_knihu(kniha)
kniznica.pridaj_knihu(kniha2)
kniznica.pridaj_knihu(kniha3)
kniznica.vypozicaj_knihu(kniha)
kniznica.zobrazi_dostupne_knihy()
kniznica.zaznamena_vratenie("1245", "02/12/2023")
print(kniznica.vygeneruj_spravu_o_knizni())

