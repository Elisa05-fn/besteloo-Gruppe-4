from kunden import Kunde

class Geschäftskunde(Kunde):
    def __init__(self, firmenname:str,ust_id:str,zahlungsziel_tage : int =14):
        super().__init__(kundennummer, name, email)
        self.firmenname = firmenname
        self.ust_id = ust_id
        self.zahlungsziel_tage = zahlungsziel_tage

    def ist_gultige_email(email:str) -> bool:
        # Überprüfen, ob die email adresse gültig ist
        if "@" in email and "." in email:
            return True
        else:
            return False

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
    def __init__(self,vereinsname:str, registernummer:str, gemeinnuetzig:bool = True):
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
