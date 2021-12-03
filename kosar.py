import bolt

class Kosar:
    """
    Egyetlen vásárlás adatait kezelő osztály.

    Az osztály attribútumai:
        - a kosárban lévő árucikkek (név-mennyiség párok)
        - a vásárlás összege
    """

    def __init__(self, termekek: dict[str, int]) -> None:
        """
        A kosár létrehozásakor beállítja az osztály attribútumait.
        """
        self.termekek=termekek


    def osszeg_lekerdezese(self) -> int:
        """
        A vásárlás összegének lekérdezése.

        :return: A vásárlás összege Ft-ban.
        """
        for i in self.termekek:
            print('ok')

    def termekek_lekerdezese(self) -> dict[str, int]:
        """
        Az árucikk-mennyiség párok lekérdezése.

        :return: Az árucikkek nevei és mennyiségei.
        """
        pass

    def termekek_szamanak_lekerdezese(self) -> int:
        """
        A kosárban lévő termékek számának lekérdezése.

        :return: Hány darab termék van a kosárban.
        """
        pass

    def arucikk_mennyisegenek_lekerdezese(self, arucikk: str) -> int:
        """
        Egy árucikknek a kosárban megtalálható mennyiségének lekérdezése.

        :param arucikk: A vizsgált árucikk neve.
        :return: A vizsgált árucikk mennyisége a kosárban.
        """
        for i in range(len(kosarak)):
            if kosarak[i]==sorszam:
                print("%d árúcikk volt a kosárban" %len(kosarak[i]))
                colostok=0
                toll=0
                HB_ceruza=0
                szatyor=0
                csavarkulcs=0
                doboz=0
                filctoll=0
                kefe=0
                ceruzaelem=0
                for elem in kosarak[i]:
                    if elem=="colostok":
                        colostok+=1
                    elif elem=="toll":
                        toll+=1
                    elif elem=="filctoll":
                        filctoll+=1
                    elif elem=="HB ceruza":
                        HB_ceruza+=1
                    elif elem=="szatyor":
                        szatyor+=1
                    elif elem=="csavarkulcs":
                        csavarkulcs+=1
                    elif elem=="doboz":
                        doboz+=1
                    elif elem=="kefe":
                        kefe+=1
                    elif elem=="ceruzaelem":
                        ceruzaelem+=1
        print("%d colostok, %d toll, %d HB ceruza, %d szatyor, %d csavarkulcs, %d doboz, %d filctoll,"
              "%d kefe és %d ceruzaelem van a megadott kosárban" % (
              colostok, toll, HB_ceruza, szatyor, csavarkulcs, doboz, filctoll, kefe, ceruzaelem))

    def kosar_tartalmanak_kiiratasa(self) -> None:
        """
        Kiírja a kosár tartalmát a konzolra.
        """
        for i in kosarak:
            if kosarak[i]==sorszam:
                print(kosarak[i])

