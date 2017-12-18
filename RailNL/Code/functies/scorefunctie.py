# Vak: Heuristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen.
# Case: Rail NL
#
# Berekenen van de kwaliteit van de lijnvoering d.m.v. scorefunctie.
#


def score(alle_trajecten, totale_tijdsduur, sporen, totaal_sporen, trajecten_algemeen, stations):
    """
    Deze functie berekend een score van de kwaliteit van de lijnvoering.

    De argumenten die worden mee gegeven zijn alle trajecten,
    totaal aantal minuten gereden, sporen en totaal aantal sporen.

    score p*1000 - (t * 20 + min / 10000)
    p) percentage bereden sporen. t) aantal treinen. min) totale tijdsduur. 

    De functie returned de berekende score.
    """

    # Als de oplossing niet alle stations heeft bereden is het geen geldige oplossing,
    # dus 0 punten.
    if not len(trajecten_algemeen) == len(stations):
        score = 0
        return score

    # Als de oplossing wel geldig is, reken de score uit.
    else:
        aantal_treinen = len(alle_trajecten)
        t = aantal_treinen

        # Als de lengte van alle trajecten 1 is, dus trein is nergens heen gegaan. 
        # Tel dit trjaect niet mee.
        for i in range(aantal_treinen):
            if len(alle_trajecten[i]) == 1:
                t = t - 1
        gebruikte_sporen = len(sporen)
        min = totale_tijdsduur

        # Bereken percentage gebruikte sporen.
        p = gebruikte_sporen / totaal_sporen
        score = p*10000 - (t*20 + min/10000)

        return score
