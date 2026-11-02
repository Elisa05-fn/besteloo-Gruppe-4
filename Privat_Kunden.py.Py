from datetime import date


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
