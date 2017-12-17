# Course: Huristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL
#
# In dit bestand worden de trajecten bepaald die worden gereden.  
#

import classes.classes
import functies.start



# Deze functie bepaald het traject. 

def traject_maker(RANGE, MAX, stations, verbindingen, uithoeken, graph, TOTAAL_SPOREN, TOTAAL_STATIONS):
    """
    Deze functie bepaalt welk traject er wordt gereden. 
    
    De functie returned de totale tijdsduur, de trajecten, de sporen waar is 
    gereden en de trajecten. 
    
    """
     
    alle_trajecten = []
    trajecten_algemeen =[] 
    sporen = [] 
    alle_tijdsduur = []
    
    for i in range (RANGE):
        
        # Kies het start station. 

        START = functies.start.kies_start3(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)

        z = START
        
        trein = classes.classes.Trein([START], [START], [z], 0)    

        # Loop door tot traject < 120 minuten. 
        while (trein.tijdsduur < MAX):
            
            # Break als alle sporen zijn bereden en alle stations zijn bereden.
            if len(sporen) == TOTAAL_SPOREN and len(trajecten_algemeen) == TOTAAL_STATIONS:
                break

            else:
                # Beste optie kiezen aan de hand van de mogelijkheden.
                beste_optie = trein.opties_randomconstr(sporen, graph, trajecten_algemeen, trein.eindstation[0])
                
                # Spoor toevoegen.
                trein.spoor_toevoegen(sporen, trein.eindstation[0], beste_optie)
                
                # Trein verplaatsen naar volgend spoor.
                trein.volgend_spoor(beste_optie[0])
                
                # Huiding station updaten.
                trein.actuele_station(beste_optie[0])
                
                # Tijd updaten.
                trein.tijd(beste_optie[1])

        # Indien de tijd hoger is dan 120 minuten, haal laatste verbinding weg.
        if trein.tijdsduur > MAX:
            trein.verminderen(beste_optie)
            trein.pop(trajecten_algemeen, sporen)
            lengte = len(trein.traject) - 1
            trein.actuele_station(trein.traject[lengte])
        
        # Voeg de trajecten en tijdsduur toe aan de lijsten. 
        alle_trajecten.append(trein.traject)
        alle_tijdsduur.append(trein.tijdsduur)

    return alle_tijdsduur, alle_trajecten, sporen, trajecten_algemeen

    