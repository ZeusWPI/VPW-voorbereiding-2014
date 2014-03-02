def crossoverpunten(chromosoom1, chromosoom2):
    
    """
    >>> chromosoom1 = [3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62]
    >>> chromosoom2 = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]
    >>> crossoverpunten(chromosoom1, chromosoom2)
    4
    >>> chromosoom1 = [-5, 100, 1000, 1005]
    >>> chromosoom2 = [-12, 1000, 1001]
    >>> crossoverpunten(chromosoom1, chromosoom2)
    1
    """
    
    return len(set(chromosoom1) & set(chromosoom2))

def maximaleSom(chromosoom1, chromosoom2):
    
    """
    >>> chromosoom1 = [3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62]
    >>> chromosoom2 = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]
    >>> maximaleSom(chromosoom1, chromosoom2)
    450
    >>> chromosoom1 = [-5, 100, 1000, 1005]
    >>> chromosoom2 = [-12, 1000, 1001]
    >>> maximaleSom(chromosoom1, chromosoom2)
    2100
    """
    
    # (deel)sommen en posities initialiseren
    som, som1, som2, p1, p2 = [0] * 5
    
    # langste pad zoeken: breid telkens som uit voor kleinste van de
    # twee elementen op beide chromosomen, tot crossoverpunt gevonden
    # wordt; in die geval wordt de grootste som behouden
    while p1 < len(chromosoom1) or p2 < len(chromosoom2):
        
        if p1 == len(chromosoom1):
            
            som2 += chromosoom2[p2]
            p2 += 1
            
        elif p2 == len(chromosoom2) or chromosoom1[p1] < chromosoom2[p2]:
            
            som1 += chromosoom1[p1]
            p1 += 1
            
        elif chromosoom1[p1] > chromosoom2[p2]:
            
            som2 += chromosoom2[p2]
            p2 += 1
            
        else:
            
            som += max(som1, som2) + chromosoom1[p1]
            som1, som2 = 0, 0
            p1 += 1
            p2 += 1

    # langste pad uischrijven: deelsommen van uiteinden van langste
    # paden moet nog uitgeschreven worden
    return som + max(som1, som2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()