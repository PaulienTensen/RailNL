import functies.verderzoekfuncties
import functies.scorefunctie
import functies.minuten
import copy


def verderzoeken(alle_trajecten1, alle_tijdsduur1, totale_tijdsduur1, trajecten_algemeen1, graph, sporen1, MAX, TOTAAL_SPOREN, score1, HILL2, verbindingen):

    aantal_trajecten = len(alle_trajecten1)
    totaal_tijd1 = functies.minuten.minuten(alle_tijdsduur1)
    
    alle_tijdsduur_def = copy.deepcopy(alle_tijdsduur1)
    alle_trajecten_def = copy.deepcopy(alle_trajecten1)
    trajecten_algemeen_def = copy.deepcopy(trajecten_algemeen1)

    totaal_tijd_def = copy.deepcopy(totale_tijdsduur1)

    alle_trajecten2 = copy.deepcopy(alle_trajecten1)
    
    sporen = copy.deepcopy(sporen1)
    
    trajecten_algemeen = copy.deepcopy(trajecten_algemeen1)
    alle_tijdsduur = copy.deepcopy(alle_tijdsduur1)
    
    nieuw_alle_trajecten = []
    nieuw_alle_tijden = []
    
    
    for i in range(aantal_trajecten):
        
        eigen_traject = copy.deepcopy(alle_trajecten2[i])
            
        nieuwe_tijdsduur = copy.deepcopy(alle_tijdsduur[i])
        
        score_oud = functies.scorefunctie.score(eigen_traject, nieuwe_tijdsduur, sporen, TOTAAL_SPOREN)
        
        sporen1 = copy.deepcopy(sporen)

        for _ in range(HILL2):
        

            begin_station = alle_trajecten2[i][-1]
            nieuw_eigen_traject = copy.deepcopy(alle_trajecten2[i])
            nieuw_nieuw_tijdsduur = copy.deepcopy(alle_tijdsduur[i])
            eind_sporen = copy.deepcopy(sporen1)

            
            while (nieuw_nieuw_tijdsduur < MAX):
            
                beste_optie = functies.verderzoekfuncties.opties_randomconstr(eind_sporen, graph, trajecten_algemeen, begin_station, nieuw_eigen_traject)
                
                nieuw_nieuw_tijdsduur = nieuw_nieuw_tijdsduur + beste_optie[1]
                
                eind_sporen = functies.verderzoekfuncties.spoor_toevoegen(eind_sporen, begin_station, beste_optie[0], nieuw_nieuw_tijdsduur)    
                
                begin_station = functies.verderzoekfuncties.actuele_station(beste_optie[0])
                
                functies.verderzoekfuncties.volgend_spoor(beste_optie[0], nieuw_eigen_traject)

                
            if nieuw_nieuw_tijdsduur > MAX:
                

                functies.verderzoekfuncties.pop(trajecten_algemeen, trajecten_algemeen1, eind_sporen, nieuw_eigen_traject)

                nieuw_nieuw_tijdsduur = nieuw_nieuw_tijdsduur - beste_optie[1]

        
        
        
        
            score_nieuw = functies.scorefunctie.score(nieuw_eigen_traject, nieuw_nieuw_tijdsduur, eind_sporen, TOTAAL_SPOREN)
        
        
            if score_nieuw > score_oud :

                score_oud = score_nieuw
                eigen_traject = nieuw_eigen_traject
                
                sporen = eind_sporen
                
                nieuwe_tijdsduur = nieuw_nieuw_tijdsduur
        
        
        
        nieuw_alle_trajecten.append(eigen_traject)
        nieuw_alle_tijden.append(nieuwe_tijdsduur)

              
              
    trajecten = functies.opschonen.opschonen(nieuw_alle_trajecten, nieuw_alle_tijden, verbindingen)

    nieuw_alle_trajecten = trajecten[0] 
    nieuw_alle_tijden = trajecten[1] 
     
    totaal_tijd = functies.minuten.minuten(nieuw_alle_tijden)
    score = functies.scorefunctie.score(nieuw_alle_trajecten, totaal_tijd, sporen, TOTAAL_SPOREN)

    
    return nieuw_alle_trajecten, nieuw_alle_tijden, score, sporen, trajecten_algemeen, totaal_tijd 
    
    






