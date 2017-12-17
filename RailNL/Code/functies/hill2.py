from random import randint


def actuele_station(beste_optie):
    """Deze functie vervangt het oude station voor het huidige station."""
    
    huidig_station = beste_optie
    return huidig_station


def volgend_spoor(nieuw_station, traject):
    """Deze functie voegt het volgende spoor toe aan traject"""

    
    traject.append(nieuw_station)


def pop(trajecten_algemeen, sporen, traject):
      
        a = traject[-1]
        b = traject[-2]
        laatste_verbinding = {b:a}
        
        pop = traject.pop() 
         
        pop2 = trajecten_algemeen.pop()
        
        # Als er maar 1 station in traject is, kun je niet deze niet verwijderen. 
        if not pop == pop2:
            trajecten_algemeen.append(pop2)
        
        # Verwijder laatste verbinding uit sporen. 
        if laatste_verbinding == sporen[-1]:
            pop3 = sporen.pop()

def spoor_toevoegen(sporen, huidig_station, beste_optie, tijd):
    """"Deze functie voegt het spoor toe en onthoudt de verbindingen."""
    
    #print(sporen)
    
    
    h = huidig_station
    b = beste_optie
    verbinding1 = {h:b}
    verbinding2 = {b:h}
    

    # Als verbindingen nog niet in sporen zitten, voeg toe aan sporen.
    if not(verbinding1 in sporen) and not(verbinding2) in sporen:
        #print(verbinding1)
        #print(tijd)
        sporen.append(verbinding1)
    
    return sporen
        
     

     
        
def opties_randomconstr(sporen, graph, trajecten_algemeen, huidig_station, eigen_traject):
        
        
        
     
    # Lege lijsten om stations aan toe te voegen. 
    richtingen = graph[huidig_station]
    stations_niet_aangetikt = []
    stations_wel_aangetikt = []


    
    for row in richtingen:
        
        # Als de richting nog niet in trajecten zit voeg deze toe aan 
        # stations die nog niet bereden zijn. 
        if row[0][0] not in trajecten_algemeen:
          
            stations_niet_aangetikt.append(row)
        
        # Als traject wel het begin station is, voeg toe aan al bereden 
        # stations.
        else:
                stations_wel_aangetikt.append(row)
           
           
           
           
    # Als niet bereden stations leeg is. 
    if not stations_niet_aangetikt == []:
        

        i = randint(0, len(stations_niet_aangetikt) -1)
        
        beste_station = stations_niet_aangetikt[i][0][0]
        beste_tijd = int(stations_niet_aangetikt[i][1][0])
        
    
        trajecten_algemeen.append(beste_station)
        
        
        return beste_station, beste_tijd

    
    
    
    
    
    
    
    # Als alle stations zijn bereden. 
    elif not stations_wel_aangetikt == []: 
        

    
        onbereden_sporen = []
       
        for row in stations_wel_aangetikt:

            h = huidig_station
            b = row[0][0]
            verbinding1 = {h:b}
            verbinding2 = {b:h}

            
            # Als sporen bij station al zijn bereden.
            if not verbinding1 in sporen and not verbinding2 in sporen:

                onbereden_sporen.append(row)
                
        
        
        
        
        if not onbereden_sporen == []:
        


            i = randint(0, len(onbereden_sporen) -1)
            
            beste_station = onbereden_sporen[i][0][0]
            beste_tijd = int(onbereden_sporen[i][1][0])
        

            # Return beste station en kortste tijd.
            return beste_station, beste_tijd
      

        else:

            i = randint(0, len(stations_wel_aangetikt) -1)

            beste_station = stations_wel_aangetikt[i][0][0]
            beste_tijd = int(stations_wel_aangetikt[i][1][0])

            
            # Return beste station en kortste tijd.
            return beste_station, beste_tijd
         
         

      




    
    
    