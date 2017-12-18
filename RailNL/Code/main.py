# Course: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL 
#
# Dit is het main bestand. Run dit bestand door middel van main.py.
#

import functies.scorefunctie
import functies.minuten
import algo.hillclimber
import inladen.inladen
import time
import visualisatie.visualisatie


# Houd de tijd bij. 
start_time = time.clock()

# Aantal iteraties van de hillclimber.


# AANTAL MINUTEN

HILL = 1000

# Aantal minuten.

MAX = 180


# Aantal trajecten.
RANGE = 11

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

# Laad graph in. 
graph = inladen.inladen.graph(stations, alle_sporen)

# Pak alle uithoeken. 
uithoeken = inladen.inladen.uithoeken(graph, stations)





resultaat = algo.hillclimber.hillclimber(SCORE, HILL, RANGE, MAX, stations, verbindingen, uithoeken, graph, TOTAAL_SPOREN, TOTAAL_STATIONS)

# Hill climber returnd 4 gegevens. Deze worden weer opgehaald. 
score = resultaat[0]
alle_tijdsduur = resultaat[1]
alle_trajecten = resultaat[2]
sporen = resultaat[3]
trajecten_algemeen = resultaat[4]


totale_tijdsduur = (functies.minuten.minuten(alle_tijdsduur))


# Deze print statements nog verwijderen. 
print("TRAJECTEN:")
for i in range (len(alle_trajecten)):
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


visualisatie.visualisatie.visualisatie(alle_trajecten, STATIONS, VERBINDINGEN)






