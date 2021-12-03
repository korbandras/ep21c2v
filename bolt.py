import kosar
class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """


    def feladat_1(self, filepath: str) -> None:
        """
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        global kosarak
        kosarak = []
        kosar = []
        fbe = open("kosar.txt", 'r')
        for sor in fbe:
            if sor.strip() != "F":
                kosar.append(sor.strip())
            else:
                kosarak.append(kosar)
                kosar = []
        print(kosarak)

    def feladat_2(self) -> None:
        """
        Kiírja, hányan fizettek a pénztárnál.
        """
        print("%d ember fizetett" %len(kosarak))

    def feladat_3(self) -> None:
        """
        Bekéri egy vásárlás sorszámát és kiírja:
            - hány darab árucikk volt a kosárban,
            - mely árucikkekből és milyen mennyiségben vásároltak,
            - a vásárlás összegét.
        """
        sorszam=int(input("Vásárlás sorszámát kérem: "))
    def feladat_4(self) -> None:
        """
        Bekéri egy árucikk nevét és kiírja:
            - melyik vásárlásnál vettek először a termékből
            - melyik vásárlásnál vettek utoljára a termékből
            - összesen hány alkalommal vásároltak a termékből
        """
        nev=input("Kérem az egyik árúcikk nevét: ")


    def feladat_5(self, filepath: str) -> None:
        """
        Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        pass
