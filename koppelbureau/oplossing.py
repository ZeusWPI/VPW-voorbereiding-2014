def koppelbureau(voorkeurMannen, voorkeurVrouwen):
    
    """
    >>> koppelbureau(
    ...     [  [1, 0, 2, 3], 
    ...        [3, 0, 1, 2], 
    ...        [0, 2, 1, 3], 
    ...        [1, 2, 0, 3]  ], 
    ...     [  [0, 2, 1, 3], 
    ...        [2, 3, 0, 1], 
    ...        [3, 1, 2, 0], 
    ...        [2, 1, 0, 3]  ]
    ... )
    ((0, 0), (1, 3), (2, 2), (3, 1))
    >>> koppelbureau(
    ...     [  [0, 2, 1], 
    ...        [1, 0, 2], 
    ...        [1, 2, 0]  ], 
    ...     [  [2, 1, 0], 
    ...        [2, 1, 0], 
    ...        [1, 2, 0]  ]
    ... )
    ((0, 2), (1, 0), (2, 1))
    >>> koppelbureau(
    ...     [  [0, 2, 1, 3], 
    ...        [2, 1, 3, 0], 
    ...        [0, 3, 1, 2], 
    ...        [1, 2, 0, 3]  ],
    ...     [  [1, 0, 2, 3], 
    ...        [0, 2, 3, 1], 
    ...        [3, 0, 1, 2], 
    ...        [1, 3, 2, 0]  ]
    ... )
    ((0, 0), (1, 2), (2, 3), (3, 1))
    """
    
    n = len(voorkeurMannen)
    gekoppeld = [None] * n    # vrouwen waaraan mannen gekoppeld zijn (None indien man nog niet gekoppeld is)
    volgende = [0] * n        # geeft aan hoeveelste vrouw elke man als volgende zal kiezen
    
    while None in gekoppeld:
        # zoek vrije man die moet gekoppeld worden
        man = gekoppeld.index(None)
        
        # bepaal hoogst gerangschikte vrouw aan wie man nog geen aanzoek gedaan heeft
        vrouw = voorkeurMannen[man][volgende[man]]
        volgende[man] += 1
        
        # laat man aan deze vrouw een aanzoek kan doen
        if vrouw not in gekoppeld:
            gekoppeld[man] = vrouw
        else:
            # er is een mannelijke concurrent
            concurrent = gekoppeld.index(vrouw)
            if voorkeurVrouwen[vrouw].index(man) < voorkeurVrouwen[vrouw].index(concurrent):
                gekoppeld[man] = vrouw
                gekoppeld[concurrent] = None
            
    # genereer tuple van koppels
    koppels = []
    for man in range(n):
        koppels.append((man, gekoppeld[man]))
    return tuple(koppels)

if __name__ == '__main__':
    import doctest
    doctest.testmod()