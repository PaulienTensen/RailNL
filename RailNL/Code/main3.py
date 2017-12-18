# Vak: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL 
#
# Dit is het main bestand. Run dit bestand door middel van main3.py.
#

import functies.minuten
import algo.hillclimber2
import inladen.inladen
import time
import visualisatie.visualisatie


# Houd de tijd bij. 
start_time = time.clock()

# Aantal iteraties Nearest neighbor loop.
HILL = 10

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

# Run het Nearest Neighbor algoritme met de ingebouwde verderzoek algoritme.
resultaat = algo.hillclimber2.hillclimber2(SCORE, HILL, HILL2, TRAJECTEN, MAX, MAX2, stations, verbindingen, uithoeken, graaf, TOTAAL_SPOREN, TOTAAL_STATIONS)

# Hill climber returnd 5 gegevens, deze worden opgeslagen.
score = resultaat[0]
alle_tijdsduur = resultaat[1]
alle_trajecten = resultaat[2]
sporen = resultaat[3]
trajecten_algemeen = resultaat[4]

#Totaal aantal minuten van alle trajecten.
totale_tijdsduur = (functies.minuten.minuten(alle_tijdsduur))

# Deze print ststatement print alle uitkomsten.
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

# Visualisatie oplossing.
visualisatie.visualisatie.visualisatie(alle_trajecten, STATIONS, VERBINDINGEN)
