# Course: Huristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL
#
# Dit bestand bestaat uit de class Trein. Het bepaald het traject, houdt het 
# actuele station bij, vervangt het oude station voor een nieuw station, 
# houdt de tijd bij en verwijderd het laatste station wanneer de tijd wordt 
# overschreden.
#

from random import randint

# Class Trein aanmaken.    
class Trein(object):
    """
    Deze class (Trein) bevat de publieke methodes onder init: 
    het traject, het eindstation de tijdsduur en het beginstation. 
    
    De class Trein onthoudt het actuele station, bepaalt het volgende spoor, en 
    houdt de tijd bij. Het houdt het spoor bij, en bepaalt welk spoor er wordt
    genomen. Tot slot wordt het laatste station verwijderd wanneer de tijd is 
    overschreden. 
    """

    def __init__(self, traject, eindstation, beginstation, tijdsduur):
        self.traject= traject
        self.eindstation = eindstation
        self.tijdsduur = tijdsduur
        self.beginstation = beginstation
     
    def actuele_station(self,huidig_station):
        """Deze functie vervangt het oude station voor het huidige station."""
        
        self.eindstation = []
        self.eindstation.append(huidig_station)
      
    def volgend_spoor(self, nieuw_station):
        """Deze functie voegt het volgende spoor toe aan traject"""
        
        self.traject.append(nieuw_station)
       
    def tijd(self, tijd):
        """Deze functie houdt de tijd bij."""
        
        self.tijdsduur += tijd

    def spoor_toevoegen(self, sporen, huidig_station, beste_optie):
        """"Deze functie voegt het spoor toe en onthoudt de verbindingen."""
        
        h = huidig_station
        b = beste_optie[0]
        verbinding1 = {h:b}
        verbinding2 = {b:h}
        
        # Als verbindingen nog niet in sporen zitten, voeg toe aan sporen.
        if not verbinding1 in sporen and not verbinding2 in sporen:
            sporen.append(verbinding1)
        
        

    def opties_randomconstr(self, sporen, graph, trajecten_algemeen, huidig_station):
        
        # Lege lijsten om stations aan toe te voegen. 
        richtingen = graph[huidig_station]
        stations_niet_aangetikt = []
        stations_wel_aangetikt = []
        terugweg = []

        
        for row in richtingen:
            
            # Als de richting nog niet in trajecten zit voeg deze toe aan 
            # stations die nog niet bereden zijn. 
            if row[0][0] not in trajecten_algemeen:
                stations_niet_aangetikt.append(row)
            
            # Als traject niet het begin station is, voeg toe aan terug weg.  
            elif not self.traject == self.beginstation:
                if row[0][0] == self.traject[-2]:
                    terugweg.append(row)
                
                # Anders voeg station toe die al aangetikt is. 
                else:
                    stations_wel_aangetikt.append(row)                                        
            
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
               # print(verbinding1)
                #print(sporen)
                
                # Als sporen bij station al zijn bereden.
                if verbinding1 in sporen or verbinding2 in sporen:
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
             
             
        else:

            beste_station = terugweg[0][0][0]
            beste_tijd = int(terugweg[0][1][0])

            
            # Return beste station en kortste tijd.
            return beste_station, beste_tijd  
          




        
        
        
        
        
        
        
        
        
    # Random kiezen, nog te maken!
    def opties_random(self, sporen, graph, trajecten_algemeen, huidig_station):
        
        

        richtingen = graph[huidig_station]
        
        i = randint(0, len(richtingen) -1)
        
        beste_station = richtingen[i][0][0]
        beste_tijd = int(richtingen[i][1][0])
        
        if not beste_station in trajecten_algemeen:     
            # Voeg best gekozen station toe aan trajecten.     
            trajecten_algemeen.append(beste_station)
        
        return beste_station, beste_tijd
        

        
        
    def opties_farest(self, sporen, graph, trajecten_algemeen, huidig_station):
        
        # Lege lijsten om stations aan toe te voegen. 
        richtingen = graph[huidig_station]
        stations_niet_aangetikt = []
        stations_wel_aangetikt = []
        terugweg = []
        
        for row in richtingen:
            
            # Als de richting nog niet in trajecten zit voeg deze toe aan 
            # stations die nog niet bereden zijn. 
            if row[0][0] not in trajecten_algemeen:
                stations_niet_aangetikt.append(row)
            
            # Als traject niet het begin station is, voeg toe aan terug weg.  
            elif not self.traject == self.beginstation:
                if row[0][0] == self.traject[-2]:
                    terugweg.append(row)
                
                # Anders voeg station toe die al aangetikt is. 
                else:
                    stations_wel_aangetikt.append(row)                                        
            
            # Als traject wel het begin station is, voeg toe aan al bereden 
            # stations.
            else:
                    stations_wel_aangetikt.append(row)
               
        # Als niet bereden stations leeg is. 
        if not stations_niet_aangetikt == []:
            beste_tijd = 0
            
            # Kies het station met de laagste tijd. 
            for row in stations_niet_aangetikt: 
                if int(row[1][0]) >= beste_tijd:
                    beste_tijd = int(row[1][0])
                    beste_station = row[0][0] 
    
                

            # Voeg best gekozen station toe aan trajecten.     
            trajecten_algemeen.append(beste_station)
            return beste_station, beste_tijd
        
        # Als alle stations zijn bereden. 
        elif not stations_wel_aangetikt == []: 
            
            beste_tijd = 0
            
            
            
            # Manier om sporen te checken. 
            for row in stations_wel_aangetikt:
                
                # Huidig station tegenover optie zetten. 
                h = huidig_station
                b = row[0][0]
                verbinding1 = {h:b}
                verbinding2 = {b:h}

                # Als sporen bij station al zijn bereden.
                if verbinding1 in sporen or verbinding2 in sporen:
                    
                    # Kies spoor met laagste tijd. 
                    if int(row[1][0]) >= beste_tijd:
                        beste_tijd = int(row[1][0])
                        beste_station = row[0][0] 

                # Als spoor nog niet is bereden.         
                else:
                    
                    # Kies beste tijd en station. Return deze.
                    beste_tijd = int(row[1][0])
                    beste_station = row [0][0]
                    return beste_station, beste_tijd
            
            # Return beste station en kortste tijd.
            return beste_station, beste_tijd
            
        # Als terug de enige optie is ga terug.
        else: 
            beste_station = row[0][0]
            beste_tijd =  int(row[1][0])
            return beste_station, beste_tijd
 
    
         
    # Deze functie maakt de beslissing welk spoor er wordt genomen.  
    def opties_nearest(self, sporen, graph, trajecten_algemeen, huidig_station):
        """
        Deze functie maakt de beslissing welk spoor er wordt genomen. 
        
        Allereest wordt het begin station bekeken. 
        Vervolgens wordt een keuze gemaakt waar de trein heen gaat. Kies het 
        station verbonden door de laagste tijd (nearest neighbour). Als deze al 
        bereden is kies onbereden station. Als alle stations bereden zijn kies
        station met onbereden sporen. Als alle stations bereden zijn en alle
        sporen, ga terug als dit de enige optie is. 
        
        De functie returned de beste tijd en beste station. 
        """

        richtingen = graph[huidig_station]
        stations_niet_aangetikt = []
        stations_wel_aangetikt = []
        terugweg = []
        
        for row in richtingen:
            
            # Als de richting nog niet in trajecten zit voeg deze toe aan 
            # stations die nog niet bereden zijn. 
            if row[0][0] not in trajecten_algemeen:
                stations_niet_aangetikt.append(row)
            
            # Als traject niet het begin station is, voeg toe aan terug weg.  
            elif not self.traject == self.beginstation:
                if row[0][0] == self.traject[-2]:
                    terugweg.append(row)
                
                # Anders voeg station toe die al aangetikt is. 
                else:
                    stations_wel_aangetikt.append(row)                                        
            
            # Als traject wel het begin station is, voeg toe aan al bereden 
            # stations.
            else:
                    stations_wel_aangetikt.append(row)
               
        # Als alle stations nog niet zijn bereden. 
        if not stations_niet_aangetikt == []:
            beste_tijd = 1000
            
            # Kies het station met de laagste tijd. 
            for row in stations_niet_aangetikt: 
                if int(row[1][0]) <= beste_tijd:
                    beste_tijd = int(row[1][0])
                    beste_station = row[0][0] 
    
            # Voeg best gekozen station toe aan trajecten.     
            trajecten_algemeen.append(beste_station)
            return beste_station, beste_tijd
        
        
        
        
        # Als alle stations zijn bereden. 
        elif not stations_wel_aangetikt == []: 
            
            beste_tijd = 1000
             
            for row in stations_wel_aangetikt:
                
                # Huidig station tegenover optie zetten. 
                h = huidig_station
                b = row[0][0]
                verbinding1 = {h:b}
                verbinding2 = {b:h}

                # Als sporen bij station al zijn bereden.
                if verbinding1 in sporen or verbinding2 in sporen:
                    
                    # Kies spoor met laagste tijd. 
                    if int(row[1][0]) <= beste_tijd:
                        beste_tijd = int(row[1][0])
                        beste_station = row[0][0] 

                # Als spoor nog niet is bereden, kies beste tijd en station.         
                else:
                    beste_tijd = int(row[1][0])
                    beste_station = row [0][0]
                    return beste_station, beste_tijd
            
            # Return beste station en kortste tijd.
            return beste_station, beste_tijd
            
        # Als terug de enige optie is ga terug.
        else: 
            beste_station = row[0][0]
            beste_tijd =  int(row[1][0])
            return beste_station, beste_tijd
 
 
    def pop(self, trajecten_algemeen, sporen):
      

     
        a = self.traject[-1]
        b = self.traject[-2]
        laatste_verbinding = {b:a}
        
        pop = self.traject.pop() 
         
        pop2 = trajecten_algemeen.pop()
        
        # Als er maar 1 station in traject is, kun je niet deze niet verwijderen. 
        if not pop == pop2:
            trajecten_algemeen.append(pop2)
        
        # Verwijder laatste verbinding uit sporen. 
        if laatste_verbinding == sporen[-1]:
            pop3 = sporen.pop()
             
    def verminderen(self, laatste_verbinding):
        """Deze functie verwijderd tijd van laatste verbinding uit tijdsduur."""
        
        self.tijdsduur -= laatste_verbinding[1] 
        

        
        
        
        
        