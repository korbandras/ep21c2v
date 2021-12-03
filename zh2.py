kosarak=[]
def f1():
    kosar = []
    fbe = open("kosar.txt", 'r')
    for sor in fbe:
        if sor.strip() != "F":
            kosar.append(sor.strip())
        else:
            kosarak.append(kosar)
            kosar = []
def f2():
    print(f"{len(kosarak)} alkalommal fizettek a pénztárnál")
def f3():
    tartalom=[]
    sorszam=int(input("Vásárlás sorszáma: "))
    valasztott_vasarlas=[]
    for i in range(len(kosarak)):
        #print(kosarak[i],i)
        if sorszam==i+1:
           valasztott_vasarlas.append(kosarak[i])
    #print(valasztott_vasarlas)
    for i in valasztott_vasarlas:
        for j in range(len(i)):
            #print(i[j])
            if i[j] not in tartalom:
                tartalom.append(i[j])
    print("A kosár tartalma:",tartalom)
    osszeg=0
    for i in tartalom:
        osszeg+=1000
    print("%d a kosár értéke" %osszeg)
def f4():
    elso=0
    utolso=0
    osszesen=0
    kosarak2=reversed(kosarak)
    aru=input("Kérem egy árúcikk nevét: ")
    for i in range(len(kosarak)):
        print(kosarak[i], i)
        for j in range(len(kosarak[i])):
            if kosarak[i][j]==aru:
                elso+=(i+1)
                break
    print(elso)
    for i in kosarak:
        for j in range(len(i)):
            if i[j]==aru:
                osszesen+=1
    if osszesen!=0:
        print(f"{osszesen} darab {aru}-t vettek")
    else:
        print("Ilyen árút nem vettek")
def f5():
    fki=open("osszeg.txt","w")
    for i in range(len(kosarak)):
        colostok = 0
        toll = 0
        HB_ceruza = 0
        szatyor = 0
        csavarkulcs = 0
        doboz = 0
        filctoll = 0
        kefe = 0
        ceruzaelem = 0
        for elem in kosarak[i]:
            if elem == "colostok":
                colostok += 1
            elif elem == "toll":
                toll += 1
            elif elem == "filctoll":
                filctoll += 1
            elif elem == "HB ceruza":
                HB_ceruza += 1
            elif elem == "szatyor":
                szatyor += 1
            elif elem == "csavarkulcs":
                csavarkulcs += 1
            elif elem == "doboz":
                doboz += 1
            elif elem == "kefe":
                kefe += 1
            elif elem == "ceruzaelem":
                ceruzaelem += 1

        if colostok==3:
            sum_colostok=1000+800+900
        elif colostok==2:
            sum_colostok=1000+900
        elif colostok==1:
            sum_colostok=1000
        else:
            sum_colostok=0

        if toll == 3:
            sum_toll = 1000 + 800 + 900
        elif toll == 2:
            sum_toll = 1000 + 900
        elif toll == 1:
            sum_toll= 1000
        else:
            sum_toll = 0

        if filctoll == 3:
            sum_filctoll = 1000 + 800 + 900
        elif filctoll == 2:
            sum_filctoll = 1000 + 900
        elif filctoll == 1:
            sum_filctoll = 1000
        else:
            sum_filctoll = 0

        if HB_ceruza == 3:
            sum_hb = 1000 + 800 + 900
        elif HB_ceruza == 2:
            sum_hb = 1000 + 900
        elif HB_ceruza == 1:
            sum_hb = 1000
        else:
            sum_hb = 0

        if szatyor == 3:
            sum_szatyor = 1000 + 800 + 900
        elif szatyor == 2:
            sum_szatyor = 1000 + 900
        elif szatyor == 1:
            sum_szatyor = 1000
        else:
            sum_szatyor = 0

        if csavarkulcs == 3:
            sum_csavarkulcs = 1000 + 800 + 900
        elif csavarkulcs == 2:
            sum_csavarkulcs = 1000 + 900
        elif csavarkulcs == 1:
            sum_csavarkulcs = 1000
        else:
            sum_csavarkulcs = 0

        if doboz == 3:
            sum_doboz = 1000 + 800 + 900
        elif doboz == 2:
            sum_doboz = 1000 + 900
        elif doboz == 1:
            sum_doboz = 1000
        else:
            sum_doboz = 0

        if ceruzaelem == 3:
            sum_ceruzaelem = 1000 + 800 + 900
        elif ceruzaelem == 2:
            sum_ceruzaelem = 1000 + 900
        elif ceruzaelem == 1:
            sum_ceruzaelem = 1000
        else:
            sum_ceruzaelem = 0

        if kefe == 3:
            sum_kefe = 1000 + 800 + 900
        elif kefe == 2:
            sum_kefe = 1000 + 900
        elif kefe == 1:
            sum_kefe = 1000
        else:
            sum_kefe = 0

        summa=sum_kefe+sum_hb+sum_colostok+sum_ceruzaelem+sum_doboz+sum_csavarkulcs+sum_szatyor+sum_filctoll+sum_toll
        #print(i, summa)
        #print(i,kosarak[i])
        fki.write(f'{i+1}. vasarlasnal {summa} Ft-t fizettek\n')
    fki.close()

f1()
f2()
f5()
f3()
f4()
