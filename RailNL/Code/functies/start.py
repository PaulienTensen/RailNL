# Course: Huristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL
#
# In dit bestand wordt de start bepaald per traject. 
#

from random import randint

def kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    """
    Deze functie bepaalt de start van elk traject.
    
    Het start punt wordt bepaald door: 
    1. Start vanuit de uithoeken. 
    2. Wanneer al in de uithoeken is begonnen begin bij een onbereden station. 
    3. Wanneer de stations allemaal zijn bereden, begin bij een station met een 
    onbereden spoor. 
    
    De functie returned het station waar op wordt 'gestart' (z). 
    """
    
    b = len(stations)
    
    # Start vanuit de uithoeken. 
    for plek in uithoeken:
    
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            
            return z

    # Kies hierna stations die niet zijn aangeraakt.
    for i in range (b):
    
        # Als station nog niet in trajecten zit, voeg dit station toe. 
        plek = stations[i]['Station']
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            
            return z

    
    # Kies vervolgens voor station die nog onbereden verbindingen heeft. 
    for i in range (len(verbindingen)):
        station1 = verbindingen[i]['Station1']
        station2 = verbindingen[i]['Station2']
        verbinding1 = {station1:station2}
        verbinding2 = {station2:station1}
        
        # als verbindingen nog niet in sporen zit. 
        if not verbinding1 in sporen and not verbinding2 in sporen:
            z = station1
            
            return z
          
   # Als alles al is geweest kies willekeurig station. 
    z = stations[0]['Station']
    return z
    

def kies_start2(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    """
    Deze functie begint op de uithoeken en begint vervolgens als de uithoeken
    zijn geweest op een random station.
    
    De functie returned station waar op wordt begonnnen (z).
    """
    
    b = len(stations)
    
    # Kies eerst de uithoeken wanneer daar nog niet begonnen is.
    for plek in uithoeken:
        
        # Als uithoek nog niet bereden is, voeg toe aan trajecten_algemeen.
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)

            return z
    
    # Wanneer op alle uithoeken is begonnen, begin dan random. 
    i = randint(0, len(stations) -1)
    plek = stations[i]['Station']
    z = plek
    
    if not plek in trajecten_algemeen:
        trajecten_algemeen.append(z)
    
    return z
  

def kies_start3(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    """ 
    Deze functie begint altijd op een random station en returned station waar
    op wordt begonnen. 
    """    
        
    # Kies random station. 
    i = randint(0, len(stations) -1)
    plek = stations[i]['Station']
    z = plek
    
    # Als station nog niet bereden, voeg toe aan trajecten algemeen.
    if not plek in trajecten_algemeen:
        trajecten_algemeen.append(z)
        
   
    return z
    
    

