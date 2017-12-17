# Course: Huristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL
#
#Berekenen van totaal aantal minuten van de lijnvoering.
#

def minuten(alle_tijdsduur):
    """Deze functie returned de totale tijdsduur van de lijnvoering."""
    
    totale_tijdsduur = 0
    
    # Tel de tijdsduur van iedere verbinding op bij totale tijdsduur. 
    for i in range(len(alle_tijdsduur)):
        totale_tijdsduur += alle_tijdsduur[i]
    
    return totale_tijdsduur