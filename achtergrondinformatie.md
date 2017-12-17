# Achtergrond informatie Rail NL.

Deze file bevat:

- vernieuwde score functie
- toetsingsgrootheid
- upperbound
- lowerbound

### Vernieuwde score functie 
De gegeven score functie bij deze case = s = p*10000 - (t*20 + min/100000).
(uitleg te vinden in README). 

Aangezien 'min' door een heel groot getal gedeeld wordt, is er nauwelijks een 
verandering in de score functie wanneer 'min' veranderd. Vandaar dat we de keuze 
hebben gemaakt 'min' door een kleiner getal te delen, zodat het aantal minuten 
een relevantere rol speelt, in de score functie wanneer 'min' veranderd. Wij 
denken dat dit belangrijk is omdat de trajecttijd ook indiceert of het een goed
traject is of niet. 
Naar aanleiding van onze tweede presentatie is er dan ook een verandering in de
case beschrijving gekomen:

1) Zit er een typfout in de scorefunctie?

Ja. De waarde 100000 moet 10000 zijn. Voor deze versie mag je de waarde kizen 
die je het beste uitkomt. De gecorrigeerde case is waarschijnlijk leuker 

Vandaar onze aangepaste score functie: 
s = p*10000 - (t*20 + min/10000)
Waarbij:
s = score voor de lijnvoering. 
p = percentage van de bereden kritieke verbindingen. 
t= aantal treinen.

### Toetsingsgrootheid

De toetsingsgrootheid= gemiddelde aantal sporen per station ^(aantal stations), 
in dit geval: 

voor Holland:
2,54 ^ 22 = 806012478.

voor heel Nederland:
2,92 ^ 61 = 1,98 *(10 ^ 28). 


#### upperbound: 
Uitkomsten van ons nearest neigbour algoritme. De upperbound hebben we berekend
aan de hand van de aangepaste score functie en de orginele score functie. 

Holland:
aangepaste score functie:
S-Min = 1 * 10000 - ((6*20) + 672/10000) = 9879,9328

orginele score functie:
S-Min = 1 * 10000 - ((6*20) + 672/100000) = 9879,99382

Heel Nederland:
aangepaste score functie: 
S-Min = 1 * 10000 - ((14*20) + (2398/10000)) = 9719.7602.

orginele score functie:
S-Min = 1 * 10000 - ((14*20) + (2398/100000)) = 9719.97602.


#### Lowerbound:
Hoogst mogelijke score berekend met de score-functie waarbij 
alle trajecten en stations worden bereden. De lowerbound hebben we berekend 
aan de hand van de aangepaste score functie en de orginele score functie. 

Holland: 
381) Aantal minuten samen gereden verbindingen in Holland.
120) Max duur van traject. 
381/120 = 3,175
Theoretische lowerbouwnd) 4 treinen die totaal 381 minuten rijden. 

Aangepaste score functie:
s-Max = 1*10000 -(4*20 + 381/10000) = 9919.9619

Orginele formule: 
s-Max = 1*10000 - (4*20 + (381/100000)) = 9919.99619 

Heel Nederland:
1551) Aantal minuten samen gereden verbindingen in heel Nederland.
180) Max duur van traject.

1551/180 = 8.6.
Theoretische lowerbound) 9 treinen die in totaal 1551 minuten rijden.

Aangepaste formule:
s-Max = 1*10000 - ((9*20) + (1551/10000)) = 9819.8449. 

Orginele formule: 
s-Max = 1*10000 - ((9*20) + (1551/100000)) = 9819.98449.

bron: http://www.thechalkface.net/resources/Travelling_Salesman_England.pdf 
