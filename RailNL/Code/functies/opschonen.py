# Course: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL
#
# Deze functie NOG COMMENTEN!
#
def opschonen(alle_trajecten, alle_tijdsduur, verbindingen):
    
    trajecten = alle_trajecten
    tijdsduren = alle_tijdsduur
    alle_sporen = []
    nieuwe_tijd = []
    
    for traject in trajecten:
        for i in range (len(traject)-1):
            
            a = traject[i]
            b = traject[i+1]
            verbinding1 = {a:b}
            verbinding2 = {b:a}
            alle_sporen.append(verbinding1)
            alle_sporen.append(verbinding2)
       
    counter = -1
    
    for traject in trajecten:
        
        counter = counter + 1   
        tijd = int(tijdsduren[counter])
        
        for i in reversed (range (len(traject))):
            
            a = traject[i-1]
            b = traject[i]
            verbinding1 = {a:b}
            verbinding2 = {b:a}
            
            aantal_keer = alle_sporen.count(verbinding1)
            
            if aantal_keer > 1:
                            
                for i in range(len(verbindingen)):           
                
                    if (verbindingen[i]["Station1"] == a and verbindingen[i]["Station2"] == b) or \
                        (verbindingen[i]["Station1"] == b and verbindingen[i]["Station2"] == a):
                        
                        tijd = tijd - int(verbindingen[i]["Tijd"])
                                              
                traject.pop()
                alle_sporen.remove(verbinding1)
                alle_sporen.remove(verbinding2)
                
            else:
                break
        
        nieuwe_tijd.append(tijd)
      
    return trajecten, nieuwe_tijd
