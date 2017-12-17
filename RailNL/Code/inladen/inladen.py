# Course: Huristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL
#
# In dit bestand openen we de csv bestanden van de station en verbindingen en 
# laden deze csv bestanden in.
#

import csv

def stations(x):
    """"
    Deze functie returned een lijst met alle stations, x/y coördinaten en of een 
    station kritiek is.
    """

    stations = []
    with open (x) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations.append(row)
    
    return stations
     
     
def verbindingen(y):
    """"
    Deze functie returned een lijst met mogelijke verbindingen tussen stations, 
    en de tijd hoelang de verbinding er over doet.
    """

    verbindingen = []
    with open(y) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            verbindingen.append(row)
    
    return verbindingen


def alle_sporen(stations, verbindingen):
    """ 
    Deze functie returned een lijst (alle_sporen) met alle stations, bijbehorende 
    verbindingen en hoelang de verbindigen er over doen.
    """
    
    b = len(stations)
    a = len(verbindingen)
    alle_sporen = []
     
    for i in range (b):        
        sporen = [] 
        
        for z in range (a):
            stat = []
            tijd = []
            
            # Als je de verbinding van een station hebt gevonden voeg deze toe
            # aan lijst stat. 
            if stations[i]['Station'] == verbindingen[z]['Station1']: 
                stat.append(verbindingen[z]['Station2'])
                
                # Voeg de duur van de verbinding toe aan tijd, en station met 
                # tijd toe aan sporen.
                tijd.append(verbindingen[z]['Tijd'])
                u = stat, tijd 
                sporen.append(u)
            
            if stations[i]['Station'] == verbindingen[z]['Station2']:
                
                stat.append(verbindingen[z]['Station1'])
                tijd.append(verbindingen[z]['Tijd'])
                u = stat, tijd            
                sporen.append(u)
       
        alle_sporen.append(sporen)
     
    return alle_sporen 
      
      
def graph(stations, alle_sporen):
    """ 
    Deze functie returned een dict (graph) met daarin alle stations en 
    sporen.
    """
    
    graph = {}
    b = len(stations)
    
    # Vul de dict met stations en alle sporen. 
    for i in range (b):
        y = {}
        x= stations[i]['Station']
        g=alle_sporen[i]
        y = {x:g}
        graph.update(y)
    
    return graph
    
    
def uithoeken(graph, stations):
    """
    Deze functie returned een lijst (uithoeken) met alle uithoeken van Nederland 
    en Holland. Deze kunnen worden gebruikt als start station. 
    """
   
    uithoeken =[] 
    
    # Stel uithoek gelijk aan 2.
    geen_uithoek = 2   
    b = len(stations)
    
    for i in range (b):
        x = stations[i]['Station']
        connecties = len(graph[x])

        # Als de stations een uithoek is, append aan uithoeken. 
        if connecties < geen_uithoek:
            uithoeken.append(x)
           
    return uithoeken
    
    

