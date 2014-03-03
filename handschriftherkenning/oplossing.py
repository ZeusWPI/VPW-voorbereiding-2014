def multistrip(l):
    while l[0] and all([s[0]==' ' for s in l]):
        for i in range(len(l)):
            l[i] = l[i][1:]

def popLetter(l):
    multistrip(l)
    if not l[0]: return
    i = 0
    while i<len(l[0]) and any([s[i]!=' ' for s in l]):
        i+=1
    letter = '\n'.join([s[:i] for s in l])
    for j in range(len(l)):
        l[j] = l[j][i:]
    return letter

def segmentatie(naam):
    lines = [l.strip('\n') for l in open(naam).readlines()]
    
    l = [popLetter(lines)]

    while l[-1]:
        l.append(popLetter(lines))
        
    return l[:-1]
    

def OCR(naam):
    l = segmentatie(naam)
    
    naam = naam[:naam.find('.')]
    
    d = {teken: letter for letter,teken in zip(naam, l[:len(naam)])}
    
    return ''.join([d[teken] for teken in l[len(naam):-1]])
