# Course: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen.
# Case: Rail NL
#
# In dit bestand maken we de visualisatie van onze case. Alle gemaakte
# trajecten krijgen een andere kleur. Als een spoor of station niet wordt
# bereden door een traject dan blijft de kleur van het station of spoor grijs.
#

import matplotlib.pyplot as plt
import numpy as np
import csv


def visualisatie(x, STATIONS, VERBINDINGEN):
    """"Deze functie maakt een visualisatie voor de lijnvoering."""

    stations = []
    x_coordinaten = []
    y_coordinaten = []
    lengte = []

    # Vul de bovenstaande lijsten met stations en coördinaten.
    with open(STATIONS) as stations_bestand:
        bestand_lezer = csv.reader(stations_bestand)
        for rij in bestand_lezer:

            stations.append(rij[0])
            x_coordinaten.append(rij[1])
            y_coordinaten.append(rij[2])

    verbinding1 = []
    verbinding2 = []
    som_totaal = 0
    connecties_holland = []

    # 16 kleuren, voor 16 verschillende trajecten.
    kleuren = ["olive", "orange", "green", "blue", "black", "red", "pink",\
            "yellow", "purple", "cyan", "brown", "magenta", "aqua", "teal", \
            "maroon", "fuchsia"]
    counter = 0

    with open(VERBINDINGEN) as verbinding_bestand:
        bestand_lezer = csv.reader(verbinding_bestand)

        # Vul de lijsten met verbindingen.
        for rij in bestand_lezer:

            # Skip eerste regel uit file.
            if counter ! = 0:
                verbinding1.append(rij[0])
                verbinding2.append(rij[1])
                lengte.append(rij[2])

                connecties_holland.append(rij)

                som_totaal = som_totaal + float(rij[2])

            counter + = 1

    # Plot de hele lijnvoering, maak deze grijs.
    for j in range(0, len(verbinding1)):
            counter1 = stations.index(verbinding1[j])
            verbinding1x = float(x_coordinaten[counter1])
            verbinding1y = float(y_coordinaten[counter1])
            counter2 = stations.index(verbinding2[j])
            verbinding2x = float(x_coordinaten[counter2])
            verbinding2y = float(y_coordinaten[counter2])

            plt.plot([verbinding1y, verbinding2y],
                    [verbinding1x, verbinding2x], marker='o', color='0.9')

            plt.xticks([])
            plt.yticks([])

            # Ga door de lijst met alle trajecten.
            for i in range(0, len(x)):

                # Plot alle verbindingen, geef ze verschillende kleuren.
                for k in range(0, len(x[i])-1):
                    counterinput1 = stations.index(x[i][k])
                    verbinding1xinput = float(x_coordinaten[counterinput1])
                    verbinding1yinput = float(y_coordinaten[counterinput1])

                    counterinput2 = stations.index(x[i][k+1])
                    verbinding2xinput = float(x_coordinaten[counterinput2])
                    verbinding2yinput = float(y_coordinaten[counterinput2])

                    plt.plot([verbinding1yinput, verbinding2yinput],\
                        [verbinding1xinput, verbinding2xinput], marker='o',\
                        color=kleuren[i])

    # Weergeef een aantal plaatsnamen om overzicht te krijgen.
    plt.text(4.5, 53, "Den Helder")
    plt.text(3.6, 51.3, "Vlissingen")
    plt.text(5.5, 51, "Maastricht")
    plt.text(6.7, 52, "Enschede")
    plt.text(6.15, 53.05, "Groningen")
    plt.text(4.87, 51.97, "Utrecht")
    plt.text(5.4, 52.57, "Lelystad")
    plt.text(6.23, 51.35, "Venlo")
    plt.text(5.29, 51.37, "Eindhoven")
    plt.text(4.74, 51.53, "Breda")
    plt.text(4.11, 52.18, "Den Haag")
    plt.text(6.55, 52.47, "Almelo")
    plt.text(6.12, 51.99, "Nijmegen")
    plt.title('Lijnvoering Nederland')
    plt.savefig("test.png")

    plt.show()
