# Vak: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen.
# Case: Rail NL
#
# Functies die aangeroepen worden in het verderzoekalgoritme.
#

from random import randint


def actuele_station(beste_optie):
    """Deze functie vervangt het oude station voor het huidige station."""

    huidig_station = beste_optie
    return huidig_station


def volgend_spoor(nieuw_station, traject):
    """Deze functie voegt het volgende spoor toe aan traject."""

    traject.append(nieuw_station)


def pop(trajecten_algemeen, oud_trajecten_algemeen, sporen, traject):
    """
    Deze functie verwijdert de overbodige toevoegingen die na de 180
    minuten worden toegevoegd.
    """

    traject_min1 = traject[-1]
    traject_min2 = traject[-2]
    laatste_verbinding = {traject_min2: traject_min1}
    laatste_verbinding2 = {traject_min1: traject_min2}
    pop = traject.pop()

    # Voorkomt dat staions verwijdert worden, waarbij dat niet moet.
    if len(trajecten_algemeen) == len(oud_trajecten_algemeen):
        trajecten_algemeen = trajecten_algemeen
    else:
        pop2 = trajecten_algemeen.pop()

        # Als laatste station in het traject niet overeenkomt met het
        # gepopte station, moet hij niet verwijdert worden.
        if not pop == pop2:
            trajecten_algemeen.append(pop2)

    # Verwijder laatste verbinding uit sporen indien de laatst toegevoegde
    # verbinding boven de 180 mins zit.
    if laatste_verbinding == sporen[-1] or laatste_verbinding2 == \
                sporen[-1]:
        pop3 = sporen.pop()


def spoor_toevoegen(sporen, huidig_station, beste_optie, tijd):
    """"Deze functie voegt het spoor toe en onthoudt de verbindingen."""

    h = huidig_station
    b = beste_optie
    verbinding1 = {h: b}
    verbinding2 = {b: h}

    # Als verbindingen nog niet in sporen zitten, voeg toe aan sporen.
    if not(verbinding1 in sporen) and not(verbinding2) in sporen:

        sporen.append(verbinding1)

    return sporen


def opties_randomconstr(sporen, graph, trajecten_algemeen, huidig_station,
        eigen_traject):
    """Maakt de keuze voor het volgend station."""

    # Lege lijsten om stations aan toe te voegen.
    richtingen = graph[huidig_station]
    stations_niet_aangetikt = []
    stations_wel_aangetikt = []

    for rij in richtingen:

        # Als het staion nog niet in trajecten_algemeen zit voeg deze toe aan
        # stations die nog niet bereden zijn.
        if rij[0][0] not in trajecten_algemeen:

            stations_niet_aangetikt.append(rij)

        # Als station wel bereden is, voeg toe aan al bereden
        # stations.
        else:
                stations_wel_aangetikt.append(rij)

    # Als niet bereden stations niet leeg is.
    if not stations_niet_aangetikt == []:

        # Kies random een station uit.
        random = randint(0, len(stations_niet_aangetikt) - 1)
        beste_station = stations_niet_aangetikt[random][0][0]
        beste_tijd = int(stations_niet_aangetikt[random][1][0])
        trajecten_algemeen.append(beste_station)

        return beste_station, beste_tijd

    # Als alle stations zijn bereden.
    elif not stations_wel_aangetikt == []:

        # Maak lijst die onbereden sporen opslaat.
        onbereden_sporen = []

        for rij in stations_wel_aangetikt:
            verbinding1 = {huidig_station: rij[0][0]}
            verbinding2 = {rij[0][0]: huidig_station}

            # Als sporen bij station niet zijn bereden.
            if not verbinding1 in sporen and not verbinding2 in sporen:
                onbereden_sporen.append(rij)

        # Als lijst onbereden sporen vol zit.
        if not onbereden_sporen == []:
            random = randint(0, len(onbereden_sporen) -1)
            beste_station = onbereden_sporen[random][0][0]
            beste_tijd = int(onbereden_sporen[random][1][0])

            return beste_station, beste_tijd

        # Als alle sporen bereden zijn:
        else:
            random = randint(0, len(stations_wel_aangetikt) -1)
            beste_station = stations_wel_aangetikt[random][0][0]
            beste_tijd = int(stations_wel_aangetikt[random][1][0])

            return beste_station, beste_tijd
