import functies.hill2
import functies.scorefunctie
import functies.minuten
import copy

def hillclimber2(alle_trajecten1, alle_tijdsduur1, totale_tijdsduur1, trajecten_algemeen1, graph, sporen1, MAX, TOTAAL_SPOREN, score1, HILL2, verbindingen):

    aantal_trajecten = len(alle_trajecten1)
    totaal_tijd1 = functies.minuten.minuten(alle_tijdsduur1)
    
    alle_tijdsduur_def = copy.deepcopy(alle_tijdsduur1)
    alle_trajecten_def = copy.deepcopy(alle_trajecten1)
    trajecten_algemeen_def = copy.deepcopy(trajecten_algemeen1)
    sporen_def = copy.deepcopy(sporen1)
    totaal_tijd_def = copy.deepcopy(totale_tijdsduur1)

    for j in range (HILL2):
    

        
        alle_trajecten2 = copy.deepcopy(alle_trajecten1)
        sporen = copy.deepcopy(sporen1)
        trajecten_algemeen = copy.deepcopy(trajecten_algemeen1)
        alle_tijdsduur = copy.deepcopy(alle_tijdsduur1)
        
        nieuw_alle_trajecten = []
        nieuw_alle_tijden = []
        
        
        for i in range(aantal_trajecten):
            

            begin_station = alle_trajecten2[i][-1]
            eigen_traject = alle_trajecten2[i]
            nieuwe_tijdsduur = alle_tijdsduur[i]
            
            while (nieuwe_tijdsduur < MAX):
            
                beste_optie = functies.hill2.opties_randomconstr(sporen, graph, trajecten_algemeen, begin_station, eigen_traject)
                
                nieuwe_tijdsduur = nieuwe_tijdsduur + beste_optie[1]
                
                
                sporen = functies.hill2.spoor_toevoegen(sporen, begin_station, beste_optie[0], nieuwe_tijdsduur)
                
                begin_station = functies.hill2.actuele_station(beste_optie[0])
                
                functies.hill2.volgend_spoor(beste_optie[0], eigen_traject)

            if nieuwe_tijdsduur > MAX:
                functies.hill2.pop(trajecten_algemeen, trajecten_algemeen1, sporen, eigen_traject)
                nieuwe_tijdsduur = nieuwe_tijdsduur - beste_optie[1]
            

            nieuw_alle_trajecten.append(eigen_traject)
            nieuw_alle_tijden.append(nieuwe_tijdsduur)
            
            
        trajecten = functies.opschonen.opschonen(nieuw_alle_trajecten, nieuw_alle_tijden, verbindingen)
        
        
        nieuw_alle_trajecten = trajecten[0] 
        nieuw_alle_tijden = trajecten[1] 
        
        
        totaal_tijd = functies.minuten.minuten(nieuw_alle_tijden)
        score = functies.scorefunctie.score(nieuw_alle_trajecten, totaal_tijd, sporen, TOTAAL_SPOREN)
        
        
            
        if score > score1:

            score1 = score
            alle_tijdsduur_def = nieuw_alle_tijden
            alle_trajecten_def = nieuw_alle_trajecten
            trajecten_algemeen_def = trajecten_algemeen
            sporen_def = sporen
            totaal_tijd_def = totaal_tijd

    
    return alle_trajecten_def, alle_tijdsduur_def, score1, sporen_def, trajecten_algemeen_def, totaal_tijd_def






