# Vak: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen.
# Case: Rail NL
#
# Dit is het main bestand. Run dit bestand door middel van main2.py.
#

import functies.minuten
import algo.hillclimber
import inladen.inladen
import time
import visualisatie.visualisatie
import algo.hill_verderzoeken


# Houd de tijd bij.
start_time = time.clock()

# Aantal iteraties Nearest neighbor loop.
HILL = 100

# Aantal iteraties verderzoekalgoritme.
HILL2 = 100

# Max aantal minuten per traject voor eerste algoritme.
MAX = 180

# Def. max aantal minuten per traject.
MAX2 = 180
SCORE = 0

# Aantal trajecten.
TRAJECTEN = 10

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

# Pas de Nearest Neighbor hillclimber toe.
resultaat = algo.hillclimber.hillclimber(SCORE, HILL, TRAJECTEN, MAX, stations,
                                         verbindingen, uithoeken, graaf,
                                         TOTAAL_SPOREN, TOTAAL_STATIONS)

# Hill climber returnd 4 gegevens. Deze worden weer opgehaald.
score = resultaat[0]
alle_tijdsduur = resultaat[1]
alle_trajecten = resultaat[2]
sporen = resultaat[3]
trajecten_algemeen = resultaat[4]

# Totaal aantal minuten van alle trajecten.
totale_tijdsduur = (functies.minuten.minuten(alle_tijdsduur))

# Print uitkomst Nearest Neighbor loop.
for i in range(len(alle_trajecten)):
    print()
    print(alle_trajecten[i])
    print(alle_tijdsduur[i])
    print()
print()
print("Nearest Neigbor Hillclimber")
print("SCORE: ", score)
print("AANTAL SPOREN: ", len(sporen))
print("AANTAL STATIONS: ", len(trajecten_algemeen))
print("TOTAAL AANTAL MINUTEN: ", totale_tijdsduur)
print()
print(time.clock() - start_time, "seconden")


start_time1 = time.clock()

# Runt de verderzoek hillclimber algoritme aan de hand van de beste
# oplossing van de Nearest Neighbor Algoritme.
nieuw_traject = algo.hill_verderzoeken.verderzoeken(alle_trajecten,
                alle_tijdsduur, totale_tijdsduur, trajecten_algemeen, graaf,
                sporen, MAX2, TOTAAL_SPOREN, HILL2, verbindingen, stations)

# Slaat uitkomsten op.
def_score = nieuw_traject[2]
def_trajecten = nieuw_traject[0]
def_tijden = nieuw_traject[1]
def_sporen = nieuw_traject[3]
def_trajecten_algemeen = nieuw_traject[4]
def_totaal_tijd = nieuw_traject[5]

# Print de beste oplossing.
for i in range(len(def_trajecten)):
    print()
    print(def_trajecten[i])
    print(def_tijden[i])
    print()
print()
print("Nearest Neigbor Hillclimber 2.0")
print("SCORE: ", def_score)
print("AANTAL SPOREN: ", len(def_sporen))
print("AANTAL STATIONS: ", len(def_trajecten_algemeen))
print("TOTAAL AANTAL MINUTEN:", def_totaal_tijd)
print()
print(time.clock() - start_time1, "seconden")

# Visualisatie uitkomst.
visualisatie.visualisatie.visualisatie(def_trajecten, STATIONS, VERBINDINGEN)
