clafrom datetime import date


class Kunde:
    def __init__(self, kundennummer: int, name: str, email: str):
        if kundennummer < 1000:
            raise ValueError("Kundennummer muss mindestens 1000 sein.")

        self.kundennummer = kundennummer
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, wert):
        if wert is None:
            raise ValueError("Der Name darf nicht leer sein.")
        sauberer_name = wert.strip()
        if not sauberer_name:
            raise ValueError("Der Name darf nicht leer sein.")
        self._name = sauberer_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, wert):
        if not self.ist_gueltige_email(wert):
            raise ValueError("Ungültige E-Mail-Adresse.")
        self._email = wert.strip()

    @staticmethod
    def ist_gueltige_email(email):
        if not isinstance(email, str):
            return False
        email = email.strip()
        if "@" not in email:
            return False
        lokalteil, domain = email.split("@", 1)
        if not lokalteil or not domain or "." not in domain:
            return False
        return True

    ist_gültige_email = ist_gueltige_email

    def begruessung(self):
        return f"Hallo {self.name}!"

    def rabattsatz(self):
        return 0.0


class Privatkunde(Kunde):
    def __init__(self, kundennummer: int, name: str, email: str, geburtsjahr: int, stammkunde: bool = False):
        super().__init__(kundennummer, name, email)
        if geburtsjahr < 1900 or geburtsjahr > date.today().year:
            raise ValueError("Das Geburtsjahr muss zwischen 1900 und dem aktuellen Jahr liegen.")
        self.geburtsjahr = geburtsjahr
        self.stammkunde = stammkunde

    def rabattsatz(self):
        return 0.02
        
    
class Geschäftskunde(Kunde):
     def__init__(self, kundennummer:int, name:str, email:str, firmenname:str,ust_id:str,zahlungsziel_tage : int =14):
        super().__init__(kundennummer, name, email)
        self.firmenname = firmenname
        self.ust_id = ust_id
        self.zahlungsziel_tage = zahlungsziel_tage

    def begruessung(self) -> str:
        return f"Sehr geehrte Damen und Herren der Firma {self.firmenname},\n\nVielen Dank für Ihre Bestellung."

    def rabattsatz(self) -> float:
        # Berechnet den Rabattsatz für Geschäftskunden
        if self.zahlungsziel_tage <= 14:
            return 0.03
        else:
            raise ValueError("Zahlungsziel muss zwischen 1 und 14 Tagen liegen.")

    def __str__(self) -> str:
        return f"Geschäftskunde: {self.firmenname}, UST-ID: { {self.ust_id}.lstrip().title().isdigit().startswith("DE")}, (Ansprechpartner: {self.name}.title()))"


class Vereinskunde(Kunde):
    def__init__(self,kundennummer:int, name:str, email:str,vereinsname:str, registernummer:str, gemeinnuetzig:bool = True):
        super().__init__(kundennummer, name, email)
        self.vereinsname = vereinsname
        self.registernummer = registernummer
        self.gemeinnuetzig = gemeinnuetzig

    def begruessung(self) -> str:
        return f"An den Vorstand des Vereins {self.vereinsname}"

    def rabattsatz(self) -> float:
        # Berechnet den Rabattstz für Vereinskunden.
        if self.gemeinnuetzig:
            return 0.05
        else:
            return 0.02   


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
         

    
