if __name__ == '__main__':
    elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
    note = [9, 7, 10, 4, 8]
    elev_nou = "Felix"
    nota_elev_nou = 6
    elev_de_sters = "Darius"
    interogari_nume = ["Ana", "Mara", "Elena", "stop"]
    absente = [1, 0, 2, 3, 0]
    for i in range(len(elevi)):
        nume_elev=elevi[i]
        nota_elev=note[i]
        print(nume_elev+" are nota "+str (nota_elev))
    nota_maxima=max(note)
    nota_minima=min(note)
    for i in range(len(note)):
        if note[i]==nota_maxima:
           print("Nota maxima este "+ str(nota_maxima) +" si a fost obtinuta de "+ elevi[i])
    for i in range(len(note)):
        if note[i]==nota_minima:
            print("Nota minima este "+str(nota_minima) +" si a fost obtinuta de "+ elevi[i])
    from decimal import Decimal, ROUND_HALF_UP
    suma_notelor=sum(note)
    nr_elevi=len(elevi)
    media_clasei=suma_notelor/nr_elevi
    medie_decimal=Decimal(media_clasei)
    medie_doua_zecimale=medie_decimal.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    print("Media clasei este "+str(medie_doua_zecimale))
    for i in range (len(elevi)):
        nume_elev = elevi[i]
        nota_elev = note[i]
        if nota_elev>=5 :
            print(nume_elev+" are nota "+str (nota_elev))
    for i in range(len(note)):
        if note[i]<10:
            note[i]=note[i]+1
    print("Notele marite sunt: "+str(note))
    elevi.append(elev_nou)
    print("Lista noua elevi dupa adaugare : "+str(elevi))
    note.append(nota_elev_nou)
    print("Lista noua note dupa adaugare : "+str(note))
    pozitie_sters=elevi.index("Darius")
    elevi.pop(pozitie_sters)
    note.pop(pozitie_sters)
    print("Lista noua elevi dupa stergere : " + str(elevi))
    print("Lista noua note dupa stregere : " + str(note))
    for i in range(len(elevi)):
        nume_elev=elevi[i]
        nota_elev=note[i]
        print(nume_elev+"- "+str (nota_elev))
    i=0
    lungime_interogari=len(interogari_nume)
    while i < lungime_interogari and interogari_nume[i] != "stop":
        nume_cautat = interogari_nume[i]
        if nume_cautat in elevi:
            pozitie = elevi.index(nume_cautat)
            nota_elev = note[pozitie]
            print("Elevul "+str(nume_cautat)+ " are nota:"+str(nota_elev))
        else:
            print("Elevul "+str(nume_cautat)+" NU există în clasa actuală.")
        i += 1
    trecuti=0
    corigenti=0
    for nota in note:
        if nota >= 5:
            trecuti += 1
        else:
            corigenti += 1
    print("Numarul de elevi trecuti este: "+str(trecuti))
    print("Numarul de elevi corigite este: "+str(corigenti))
    note_de_trecere = []
    for nota in note:
        if nota >= 5 :
            note_de_trecere.append(nota)
    print("Lista cu note de trecere:"+str(note_de_trecere))
    if len(note_de_trecere) > 0:
        suma_note_trecere = sum(note_de_trecere)
        nr_note_trecere = len(note_de_trecere)
        media_trecuti = suma_note_trecere / nr_note_trecere
        print("Media notelor de trecere este: "+str(media_trecuti))
    else:
        print("Nu există note de trecere (toți elevii sunt sub 5 sau clasa este goală). Media nu poate fi calculată.")
        media_trecuti = 0

