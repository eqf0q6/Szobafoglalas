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
