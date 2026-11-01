class Bestellposition: #ertellt eine Klasse für eine Bestellposition, die ein Produkt und eine Menge enthält
    def __init__(self, produkt, menge=1):
        self.produkt = produkt
        self.menge = menge

    @property
    def netto(self): #berechnet den Nettopreis der Bestellposition, indem der Nettopreis des Produkts mit der Menge multipliziert wird und auf zwei Dezimalstellen gerundet wird
        return round(self.produkt.nettopreis * self.menge, 2)

    @property
    def mwst(self): #berechnet den MwSt.-Betrag der Bestellposition, indem der Nettopreis mit dem MwSt.-Satz multipliziert wird und auf zwei Dezimalstellen gerundet wird
        return round(self.netto * self.produkt.mwst_satz, 2)

    @property
    def brutto(self): #berechnet den Bruttobetrag der Bestellposition, indem der Nettopreis und der MwSt.-Betrag addiert werden und auf zwei Dezimalstellen gerundet werden
        return round(self.netto + self.mwst, 2)

    def __str__(self): #gibt eine lesbare Darstellung der Bestellposition zurück, die die Menge, den Namen des Produkts, den Preis pro Einheit, den Bruttobetrag und den MwSt.-Betrag enthält
        return f"{self.menge} x {self.produkt.name} a {self.produkt.preis}€ = {self.brutto}€ (inkl. {self.mwst}€ MwSt.)"


class Bestellung: #erstellt eine Klasse für eine Bestellung, die eine Bestellnummer, einen Kunden, einen Status und eine Liste von Bestellpositionen enthält
    def __init__(self, bestellnummer, kunde, status="offen", positionen=[]):
        self.bestellnummer = bestellnummer
        self.kunde = kunde
        self.status = status
        self.positionen = positionen

    @property
    def netto_summe(self): #berechnet die Gesamtnetto-Summe der Bestellung, indem die Nettopreise aller Bestellpositionen addiert werden und auf zwei Dezimalstellen gerundet werden
        return round(sum(positionen.netto for positionen in self.positionen), 2)

    @property
    def rabatt_betrag(self): #berechnet den Rabatt-Betrag der Bestellung, indem die Gesamtnetto-Summe mit dem Rabattsatz des Kunden multipliziert wird und auf zwei Dezimalstellen gerundet wird
        return round(self.netto_summe * self.kunde.rabattsatz, 2)

    @property
    def netto_nach_rabatt(self): #berechnet den Nettopreis der Bestellung nach Abzug des Rabatts, indem der Rabatt-Betrag vom Gesamtnetto abgezogen wird und auf zwei Dezimalstellen gerundet wird
        return round(self.netto_summe - self.rabatt_betrag, 2)

    @property
    def mwst_betrag(self): #berechnet den MwSt.-Betrag der Bestellung, indem die MwSt.-Beträge aller Bestellpositionen addiert werden und auf zwei Dezimalstellen gerundet werden
        return round(sum(positionen.mwst for positionen in self.positionen), 2)

    @property
    def brutto_summe(self): #berechnet den Gesamtbetrag der Bestellung, indem der Nettopreis nach Rabatt und der MwSt.-Betrag addiert werden und auf zwei Dezimalstellen gerundet werden
        return round(self.netto_nach_rabatt + self.mwst_betrag, 2)

    def hinzufuegen(self, produkt, menge=1): #fügt eine neue Bestellposition zur Bestellung hinzu, indem überprüft wird, ob das Produkt bereits in der Liste der Bestellpositionen vorhanden ist. Wenn ja, wird die Menge erhöht, andernfalls wird eine neue Bestellposition erstellt und zur Liste hinzugefügt.
        for positionen in self.positionen:
            if positionen.produkt == produkt:
                positionen.menge += menge
                return
        position = Bestellposition(produkt, menge)
        self.positionen.append(position)

    def abschliessen(self): #schließt die Bestellung ab, indem überprüft wird, ob mindestens eine Bestellposition vorhanden ist. Wenn nicht, wird eine ValueError-Ausnahme ausgelöst. Andernfalls wird der Status der Bestellung auf "abgeschlossen" gesetzt.
        if len(self.positionen) == 0:
            raise ValueError("Eine Bestellung muss mindestens eine Position haben.")
        self.status = "abgeschlossen"

    def __len__(self): #gibt die Anzahl der Bestellpositionen in der Bestellung zurück, indem die Länge der Liste der Bestellpositionen zurückgegeben wird
        return len(self.positionen)

    def __str__(self): #gibt eine lesbare Darstellung der Bestellung zurück, die die Bestellnummer, den Status, den Namen des Kunden, die Anzahl der Bestellpositionen und die Bruttosumme enthält
        return f"Bestellung {self.bestellnummer} {self.status} für {self.kunde.name}: {len(self)} Position(en), {self.brutto_summe} € brutto"
