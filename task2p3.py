def sort_():
    text = input('vedite slova cherez probel: ')
    l = text.split()
    q=""
    for i in sorted(l,key=lambda a: len(a)):
        q = q + " " + i
    print(q)
sort_()