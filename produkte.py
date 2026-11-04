import pytest 
from bestelo.produkte import Produkt
class Produkt: 
    """Ein Produkt hat Artikelnummer, Bezeichnung, Nettopreis und Kategorie."""
    def __init__(self,artikelnummer: str, bezeichnung: str, nettepreis: float, kategorie: str) ->None:
       self._artikelnummer = artikelnummer
       self.bezeichnung = bezeichnung
       self.nettopreis = nettopreis
       self.kategorie = kategorie


    @property
    def artikelnummer(self) -> str:
        return self._artikelnummer
    

    @property
    def bezeichnung(self) -> str :
        return self._bezeichnung

    @bezeichnung.setter
    def bezeichnung(self, value: str) -> None:
        value = value.strip()
        if value == "":
            raise ValueError("leer")
        self._bezeichnung = value


    
    @property
    def nettopreis(self) -> float :
        return self._nettopreis

    @nettopreis.setter
    def nettopreis(self, value: float) -> None:
         value = value.float()
         if value <= 0:
             raise ValueError("Der Nettopreis muss größer als 0 sein")
         self._nettopreis = round(value, 2)
        
       
        
    
    
    @property
    def kategorie(self) -> str :
        return self._kategorie

    @kategorie.setter
    def kategorie(self, value: str) -> None:
        value = value.strip()
        if value not in Produkt.KATEGORIEN:
            raise ValueError("kategorie ist nicht in der Produkt.KATEGORIEN")
        self._kategorie = value
        
        
    @property
    def mwst_satz(self) -> float:
        if self.kategorie in produkt.ERMAESSIGTE_KATEGORIEN:
            return Produkt.MWST_ERMAESSIGT
        else:
            return Produkt.MWST_REGULAER


    @property
    def bruttopreis(self) -> float:
        return round(self.nettopreis * (1 +self.mwst_satz), 2)

    def __str__(self) -> str:
        return f"{self.artikelnummer}, {self.bezeichnung} - {self.nettopreis:.2f} € netto"

    def __repr__(self) -> str:
         return f"Produkt({self.artikelnummer}, {self.bezeichnung}, {self.nettopreis:.2f}, 'Lebensmittel')"

    def __eq__(self, other) -> bool:
        if not isinstance(other, "Produkt"):
         return NotImplemented

    def __lt__(self, other) -> bool:
         return (self.preis < other.preis)

    