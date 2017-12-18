# Vak: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen.
# Case: Rail NL
#
# Dubbele verbindingen aan het einde van een traject 
# verwijderen.
#


def opschonen(alle_trajecten, alle_tijdsduur, verbindingen):
    """
    Deze functie verwijdert de overbodige verbindingen in een traject.
    """

    trajecten = alle_trajecten
    tijdsduren = alle_tijdsduur
    alle_sporen = []
    nieuwe_tijd = []

    # Slaat alle sporen 2x op in de map alle_sporen.
    for traject in trajecten:
        for i in range(len(traject) - 1):

            traject_1 = traject[i]
            traject_2 = traject[i+1]
            verbinding1 = {traject_1: traject_2}
            verbinding2 = {traject_2: traject_1}
            alle_sporen.append(verbinding1)
            alle_sporen.append(verbinding2)

    #Checkt alle trajecten van achter naar voren en als 
    #de verbinding dubbel is wordt verbinding verwijdert.
    #Dit gaat door totdat een verbinding niet dubbel is.
    counter = -1
    for traject in trajecten:
        counter = counter + 1
        tijd = int(tijdsduren[counter])

        for i in reversed(range(len(traject))):
            traject_1 = traject[i-1]
            traject_2 = traject[i]
            verbinding1 = {traject_1: traject_2}
            verbinding2 = {traject_2: traject_1}

            aantal_keer = alle_sporen.count(verbinding1)

            if aantal_keer > 1:

                for i in range(len(verbindingen)):  

                    if (verbindingen[i]["Station1"] == traject_1 and \
                            verbindingen[i]["Station2"] == traject_2) or \
                            (verbindingen[i]["Station1"] == traject_2 and \
                            verbindingen[i]["Station2"] == traject_1):

                        tijd = tijd - int(verbindingen[i]["Tijd"])

                traject.pop()
                alle_sporen.remove(verbinding1)
                alle_sporen.remove(verbinding2)

            else:
                break

        nieuwe_tijd.append(tijd)

    return trajecten, nieuwe_tijd
