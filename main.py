if __name__ == '__main__':
    elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
    note = [9, 7, 10, 4, 8]
    for i in range(len(elevi)):
        nume_elev=elevi[i]
        nota_elev=note[i]
        print(nume_elev+" are nota "+str (nota_elev))
    nota_maxima=max(note)
    nota_minima=min(note)
    elevi_maximi=[]
    for i in range(len(note)):
        if note[i]==nota_maxima:
           print("nota maxima este obtinuta de "+ elevi[i])