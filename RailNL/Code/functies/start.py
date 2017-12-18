# Vak: Heuristieken
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

    lengte_stations = len(stations)

    # Start vanuit de uithoeken.
    for plek in uithoeken:

        if not plek in trajecten_algemeen:
            trajecten_algemeen.append(plek)

            return plek

    # Ga alle stations af.
    for i in range(lengte_stations):
    
        # Als station nog niet in trajecten zit, voeg dit station toe en gebruik als start.
        plek = stations[i]['Station']
        if not plek in trajecten_algemeen:
            trajecten_algemeen.append(plek)

            return plek

    # Kies vervolgens voor station die nog onbereden verbindingen heeft.
    for i in range(len(verbindingen)):
        station1 = verbindingen[i]['Station1']
        station2 = verbindingen[i]['Station2']
        verbinding1 = {station1: station2}
        verbinding2 = {station2: station1}

        # Als verbindingen nog niet in sporen zit.
        if not verbinding1 in sporen and not verbinding2 in sporen:

            return station1

    # Als alles al is geweest kies eerste station.
    willekeurig_station = stations[0]['Station']
    return willekeurig_station


def kies_start2(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    """
    Deze functie begint op de uithoeken en begint vervolgens als de uithoeken
    zijn geweest op een random station.

    De functie returned station waar op wordt begonnnen (z).
    """

    # Kies eerst de uithoeken wanneer indien die nog niet bereden is.
    for plek in uithoeken:

        # Als uithoek nog niet bereden is, voeg toe aan trajecten_algemeen.
        if not plek in trajecten_algemeen:
            trajecten_algemeen.append(plek)

            return plek

    # Wanneer op alle uithoeken bereden zijn, begin dan random.
    willekeurig = randint(0, len(stations) -1)
    plek = stations[willekeurig]['Station']

    if not plek in trajecten_algemeen:
        trajecten_algemeen.append(plek)

    return plek


def kies_start3(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    """
    Deze functie begint altijd op een random station en returned station waar
    op wordt begonnen.
    """

    # Kies random station.
    willekeurig = randint(0, len(stations) -1)
    plek = stations[willekeurig]['Station']

    # Als station nog niet bereden, voeg toe aan trajecten algemeen.
    if not plek in trajecten_algemeen:
        trajecten_algemeen.append(plek)

    return plek
