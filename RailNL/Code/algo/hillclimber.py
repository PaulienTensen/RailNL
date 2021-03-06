# Vak: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen.
# Case: Rail NL
#
# In dit bestand staan de functies van main.py
#

import functies.start
import classes.classes
import functies.scorefunctie
import functies.minuten
import functies.opschonen


def hillclimber(score1, HILL, RANGE, MAX,\
        stations, verbindingen, uithoeken, graph, \
        TOTAAL_SPOREN, TOTAAL_STATIONS):
    """
    Deze functie implementeert het hill climber algoritme.

    De functie returned de beste score van de hill climber, de tijdsduur,
    en de trajecten.
    """

    for j in range(HILL):

        alle_trajecten = []
        trajecten_algemeen = []
        sporen = []
        alle_tijdsduur = []

        for i in range(RANGE):

            # Kies de beginpunten van het traject.
            START = functies.start.kies_start3(sporen, verbindingen, uithoeken,
                    trajecten_algemeen, stations)
            trein = classes.classes.Trein([START], [START], [START], 0)

            # While loop gaat door tot traject kleiner of gelijk is dan 180.
            while(trein.tijdsduur < MAX):

                if len(sporen) == TOTAAL_SPOREN and \
                        len(trajecten_algemeen) == TOTAAL_STATIONS:
                    break

                else:
                
                    # Beste optie kiezen aan de hand van de mogelijkheden.
                    beste_optie = trein.opties_nearest(sporen, graph,\
                                    trajecten_algemeen, trein.eindstation[0])

                    # Spoor toevoegen.
                    trein.spoor_toevoegen(sporen, trein.eindstation[0],
                            beste_optie)
 
                    # Trein verplaatsen naar volgend spoor.
                    trein.volgend_spoor(beste_optie[0])

                    # Huiding station updaten.
                    trein.actuele_station(beste_optie[0])

                    # Tijd updaten.
                    trein.tijd(beste_optie[1])

            # Als tijdsduur langer is dan de MAX, moet het laatste spoor
            # verwijderd worden.
            if trein.tijdsduur > MAX:
                trein.verminderen(beste_optie)
                trein.pop(trajecten_algemeen, sporen)
                lengte = len(trein.traject) - 1
                trein.actuele_station(trein.traject[lengte])

            alle_trajecten.append(trein.traject)
            alle_tijdsduur.append(trein.tijdsduur)

        # Schoon de trajecten op.
        trajecten = functies.opschonen.opschonen(alle_trajecten,
                alle_tijdsduur, verbindingen)

        alle_trajecten = trajecten[0]
        alle_tijdsduur = trajecten[1]

        # Bekijk de tijdsduur.
        totale_tijdsduur = functies.minuten.minuten(alle_tijdsduur)

        # Bekijk de nieuwe score.
        score2 = functies.scorefunctie.score(alle_trajecten, totale_tijdsduur,\
                sporen, TOTAAL_SPOREN, trajecten_algemeen, stations)

        # Vergelijk de score van de vorige oplossing met de huidige
        # oplossing. Bewaar de beste oplossing.
        if score2 >= score1:
            score1 = score2
            alle_tijdsduur1 = alle_tijdsduur
            alle_trajecten1 = alle_trajecten
            trajecten_algemeen1 = trajecten_algemeen
            sporen1 = sporen

    return score1, alle_tijdsduur1, alle_trajecten1, sporen1, \
            trajecten_algemeen1
