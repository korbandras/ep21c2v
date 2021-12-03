import bolt
import kosar
termekek={
    "elso":1000,
    'masodik':900,
    'harmadik':800,
    'kesobb':800
}
kosarak=[]
kosar=[]
fbe=open("kosar.txt",'r')
for sor in fbe:
    if sor.strip()!="F":
        kosar.append(sor.strip())
    else:
        kosarak.append(kosar)
        kosar=[]
print(kosarak)
bolt.feladat_1()
bolt.feladat_2()
bolt.feladat_3()
kosar.kosar_tartalmanak_kiirasa()
kosar.arucikk_mennyisegenek_vizsgalata()
bolt.feladat_4()
kosar.termekek_lekerdezese()