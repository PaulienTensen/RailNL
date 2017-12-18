# Vak: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen.
# Case: Rail NL
#
# In dit bestand openen we de csv bestanden van de station en verbindingen en 
# laden deze csv bestanden in.
#

import csv


def stations(x):
    """"
    Deze functie returned een lijst met alle stations, x/y coördinaten en of 
    een station kritiek is.
    """

    stations = []
    with open (x) as csvfile:
        bestand_lezer = csv.DictReader(csvfile)
        for rij in bestand_lezer:
            stations.append(rij)

    return stations


def verbindingen(y):
    """"
    Deze functie returned een lijst met mogelijke verbindingen tussen stations, 
    en de tijd hoelang de verbinding er over doet.
    """

    verbindingen = []
    with open(y) as csvfile:
        bestand_lezer = csv.DictReader(csvfile)
        for rij in bestand_lezer:
            verbindingen.append(rij)
    
    return verbindingen


def alle_sporen(stations, verbindingen):
    """ 
    Deze functie returned een lijst (alle_sporen) met alle stations, 
    bijbehorende verbindingen en hoelang de verbindigen er over doen.
    """

    lengte_stations = len(stations)
    lengte_verbindingen = len(verbindingen)
    alle_sporen = []

    for i in range (lengte_stations):        
        sporen = [] 

        for z in range (lengte_verbindingen):
            stat = []
            tijd = []

            # Als je de verbinding van een station hebt gevonden voeg deze toe
            # aan lijst stat. 
            if stations[i]['Station'] == verbindingen[z]['Station1']: 
                stat.append(verbindingen[z]['Station2'])
   
                # Voeg de duur van de verbinding toe aan tijd, en voeg station 
                # met tijd toe aan sporen.
                tijd.append(verbindingen[z]['Tijd'])
                stat_tijd = stat, tijd 
                sporen.append(stat_tijd)

            if stations[i]['Station'] == verbindingen[z]['Station2']:

                stat.append(verbindingen[z]['Station1'])
                tijd.append(verbindingen[z]['Tijd'])
                stat_tijd = stat, tijd            
                sporen.append(stat_tijd)

        alle_sporen.append(sporen)

    return alle_sporen 


def graaf(stations, alle_sporen):
    """ 
    Deze functie returned een dict (graaf) met daarin alle stations en 
    sporen.
    """

    graaf = {}
    lengte_stations = len(stations)

    # Vul de dict met stations en alle sporen. 
    for i in range (lengte_stations):
        dict = {}
        station = stations[i]['Station']
        spoor = alle_sporen[i]
        dict = {station: spoor}
        graaf.update(dict)

    return graaf


def uithoeken(graaf, stations):
    """
    Deze functie returned een lijst (uithoeken) met alle uithoeken van 
    Nederland en Holland. Deze kunnen worden gebruikt als start station. 
    """

    uithoeken = [] 

    # Stel uithoek gelijk aan 2.
    geen_uithoek = 2   
    lengte_stations = len(stations)

    for i in range (lengte_stations):
        station = stations[i]['Station']
        connecties = len(graaf[station])

        # Als de stations een uithoek is, append aan uithoeken. 
        if connecties < geen_uithoek:
            uithoeken.append(station)

    return uithoeken
