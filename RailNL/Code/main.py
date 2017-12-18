# Vak: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen.
# Case: Rail NL
#
# Dit is het main bestand. Run dit bestand door middel van main.py.
# Dit bestand loopt een nearest neighbor algoritme met random beginstations.
#

import functies.minuten
import algo.hillclimber
import inladen.inladen
import time
import visualisatie.visualisatie


# Houd de tijd bij.
start_time = time.clock()

# Aantal iteraties van de hillclimber.
HILL = 10

# Aantal max minuten van een traject.
MAX = 180

# Aantal trajecten.
TRAJECTEN = 11

SCORE = 0

# Te gebruiken CSV's.
STATIONS = 'Data/StationsNationaal.csv'
VERBINDINGEN = 'Data/ConnectiesNationaal.csv'

# Pak de gebruikte lists.
stations = inladen.inladen.stations(STATIONS)
TOTAAL_STATIONS = len(stations)

# Laad de verbindingen in.
verbindingen = inladen.inladen.verbindingen(VERBINDINGEN)

# Pak het totaal aantal sporen.
TOTAAL_SPOREN = len(verbindingen)

# Pak alle sporen.
alle_sporen = inladen.inladen.alle_sporen(stations, verbindingen)

# Laad graaf in. 
graaf = inladen.inladen.graaf(stations, alle_sporen)

# Pak alle uithoeken. 
uithoeken = inladen.inladen.uithoeken(graaf, stations)

# Functie om de beste resultaat van de hillclimber te verkrijgen.
resultaat = algo.hillclimber.hillclimber(SCORE, HILL, TRAJECTEN, MAX, stations,
                                         verbindingen, uithoeken, graph,
                                         TOTAAL_SPOREN, TOTAAL_STATIONS)

# Hill climber returnd 4 gegevens. Deze worden weer opgehaald.
score = resultaat[0]
alle_tijdsduur = resultaat[1]
alle_trajecten = resultaat[2]
sporen = resultaat[3]
trajecten_algemeen = resultaat[4]

# Totale tijd lijnvoering berekenen.
totale_tijdsduur = (functies.minuten.minuten(alle_tijdsduur))

# Alle trajecten en de score uitprinten.
print("TRAJECTEN:")
for i in range(len(alle_trajecten)):
    print()
    print("TRAJECT", i)
    print(alle_trajecten[i])
    print("AANTAL GEBRUIKTE VERBINDINGEN::", len(alle_trajecten[i])-1)
    print(alle_tijdsduur[i])
print()
print("SCORE :::", score)
print("AANTAL SPOREN:: ", len(sporen))
print("AANTAL STATIONS:: ", len(trajecten_algemeen))
print("TOTAAL AANTAL MINUTEN::", totale_tijdsduur)
print()
print(time.clock() - start_time, "seconden")

# Visualisatie oplossing.
visualisatie.visualisatie.visualisatie(alle_trajecten, STATIONS, VERBINDINGEN)
