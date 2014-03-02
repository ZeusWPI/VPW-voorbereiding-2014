def categorie(karakter):
    """
    >>> categorie('f')
    0
    >>> categorie('M')
    1
    >>> categorie(' ')
    2
    """
    if 'a' <= karakter.lower() <= 'i':
        return 0
    elif 'j' <= karakter.lower() <= 'r':
        return 1
    else:
        return 2

def codeer(zin, k1, k2, k3):
    """
    >>> codeer('Nobody expects the Spanish Inquisition!', 2, 3, 1)
    'ppene xctnhes t aiSsqhoI iuinNsitb!dooy'
    """
    
    # deelstrings opbouwen
    deelstrings = ['', '', '']
    for karakter in zin:
        deelstrings[categorie(karakter)] += karakter
        
    # afzonderlijke rotaties doorvoeren op deelstrings
    resultaat = ''
    posities = [0, 0, 0]
    rotaties = [k1, k2, k3]
    for p in range(len(zin)):
        karakter = zin[p]
        cat = categorie(karakter)
        deelstring = deelstrings[cat]
        positie = (posities[cat] + rotaties[cat]) % len(deelstring)
        resultaat += deelstring[positie]
        posities[cat] += 1
    return resultaat

def decodeer(zin, k1, k2, k3):
    """
    >>> decodeer('ppene xctnhes t aiSsqhoI iuinNsitb!dooy', 2, 3, 1)
    'Nobody expects the Spanish Inquisition!'
    """
    return codeer(zin, -k1, -k2, -k3)

if __name__ == '__main__':
    import doctest
    doctest.testmod()