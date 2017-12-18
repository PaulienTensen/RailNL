# Rail NL 

De map heuristieken bevat 3 mappen:
- Psuedocodes: In deze map staan de pseudocodes voor de gebruikte algoritmes.
- RailNL: In deze map staat een nieuwe map met code, verschillende manieren van
het data inladen is hierin te vinden en de resulaten van de algoritmes.
- Visualisaties: In deze map staan de visualisaties van RAIL NL. 

De map heuristieken bevat ook het document: achtergrond informatie. 
Dit document bevat:
- Aangepaste score functie
- Upper/lowerbound
- Toetsingsgrootheid

- requirements.txt: Hierin staan de requirements voor deze case.

De case Rail NL gaat over het maken van de lijnvoering van intercity treinen in 
Nederland. De case is opgesplitst in twee delen. Allereerst wordt gekeken naar 
de lijnvoering voor Holland, om dit vervolgens uit te breiden naar de 
lijnvoering voor heel Nederland. 
Onder trajecten wordt een route van sporen en stations waarover treinen heen en 
weer rijden, verstaan.

Aantal treinstations in Holland: 22, 
aantal treinstations in Nederland: 61. 

Verder moet er in deze case rekening worden gehouden met 'kritieke stations', 
met bijbehorende 'kritieke sporen'. Wanneer deze stations niet regelmatig worden 
bereden, treden er logistieke problemen op. 

De volgende score functie werd meegegeven bij de case voor de kwaliteit van de 
lijnvoering: 
s = p*10000 - (t*20 + min/100000).
Waarbij:
s = score voor de lijnvoering. 
p = percentage van de bereden kritieke verbindingen. 
t= aantal treinen. 
min = totaal door alle treinen samen gereden minuten in de lijnvoering.

Constrains deel 1 - Lijnvoering voor Holland:
1. Tijdsframe van trajecten: maximaal 2 uur. 
2. Alle stations moeten bereden worden binnen de 2 uur. 
3. Maximaal aantal trajecten: 7. 
4. (Alle sporen moeten bereden worden binnen 2 uur met het maximal aantal 
toegestane trajecten).

Constrains deel 2 - Lijnvoering voor Nederland:
1. Tijdsframe van trajecten: maximaal 3 uur. 
2. Alle stations moeten bereden worden binnen 3 uur. 
3. Maximaal aantal trajecten: 20. 
4. (Alle sporen moeten bereden worden binnen 3 uur met het maximaal aantal 
toegestane trajecten).

### Voorwaarden

Zorg dat de bijbehorende csv bestanden: ConnectiesHolland.csv, 
StationsHolland.csv voor Holland in dezelfde map staan als het bijbehorende 
python bestand. 
Wanneer wordt gekeken naar heel Nederland moeten de csv bestanden: 
StationsNationaal.csv en ConnextiesNationaal.csv in dezelfde map staan 
als de bijbehorende python bestanden. 

### Installeren

Deze case is gemaakt met behulp van Python 3.6.

#### Runnen:
Om naar de code te gaan: -> RailNL -> Code -> Lees de readme. 

### Probleem type
Constrained optimalization problem (COP). Hierbij moet een zo goed mogelijke 
oplossing worden gevonden. 

### Resultaten tot nu toe
#### Loop nearest neighbour 11 trajecten.
Upperbound Holland = 9919,9619 Onze score = 9919,9604
Upperbound Nederland = 9819, 8449 Onze score = 9779, 8088

#### Loop verderzoeken in nearest neighbour algoritme (main3.py)
Nederland score: 9462,7487 (10 trajecten). 

#### 


## Auteurs
Paulien Tensen, Matia Caso & Thomas van Dooren. 







