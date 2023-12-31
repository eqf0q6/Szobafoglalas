from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def info(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)
        self.agyak_szama = 1

    def info(self):
        return f"Egyágyas Szoba - Szobaszám: {self.szobaszam}, Ár: {self.ar}, Ágyak száma: {self.agyak_szama}"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)
        self.agyak_szama = 2

    def info(self):
        return f"Kétágyas Szoba - Szobaszám: {self.szobaszam}, Ár: {self.ar}, Ágyak száma: {self.agyak_szama}"

class Szalloda:
    def __init__(self, nev):
        self.foglalasok = None
        self.nev = nev
        self.szobak = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    def szobak_listazasa(self):
        for szoba in self.szobak:
            print(szoba.info)

    def szoba_foglalas(self, foglalo_neve, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                return f"A szoba ({szobaszam}) már foglalt ezen a dátumon: {datum}"

        szoba = next((szoba for szoba in self.szobak if szoba.szobaszam == szobaszam), None)
        if szoba is None:
            return f"Nincs ilyen szobaszám: {szobaszam}"

        uj_foglalas = Foglalas(foglalo_neve, szoba, datum)
        self.foglalasok.append(uj_foglalas)
        return f"Foglalás megerősítve: {uj_foglalas.info()}, Ár: {szoba.ar}"

    def foglalas_lemondas(self, foglalo_neve, szobaszam, datum):
        for i, foglalas in enumerate(self.foglalasok):
            if foglalas.foglalo_neve == foglalo_neve and \
                    foglalas.szoba.szobaszam == szobaszam and \
                    foglalas.datum == datum:
                del self.foglalasok[i]
                return f"Foglalás lemondva: {foglalo_neve}, Szoba: {szobaszam}, Dátum: {datum}"

        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Jelenleg nincsenek foglalások."

        for foglalas in self.foglalasok:
            print(foglalas.info())
    

class Foglalas:
    def __init__(self, foglalo_neve, szoba, datum):
        self.foglalo_neve = foglalo_neve
        self.szoba = szoba
        self.datum = datum

    def info(self):
        return f"Foglaló neve: {self.foglalo_neve}, Szoba: {self.szoba.szobaszam}, Dátum: {self.datum}"


def main_menu(szalloda):
    while True:
        print("Üdvözöljük szállodánkban!")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Kérjük, válasszon egy opciót: ")

        if valasztas == '1':
            foglalo_neve = input("Foglaló neve: ")
            szobaszam = input("Szoba száma: ")
            datum = input("Dátum (YYYY-MM-DD formátumban): ")
            print(szalloda.szoba_foglalas(foglalo_neve, szobaszam, datum))

        elif valasztas == '2':
            foglalo_neve = input("Foglaló neve: ")
            szobaszam = input("Szoba száma: ")
            datum = input("Dátum (YYYY-MM-DD formátumban): ")
            print(szalloda.foglalas_lemondas(foglalo_neve, szobaszam, datum))

        elif valasztas == '3':
            szalloda.foglalasok_listazasa()

        elif valasztas == '4':
            print("Köszönjük, hogy minket választott")
            break
        else:
            print("Érvénytelen választás, kérjük próbálja újra!")
