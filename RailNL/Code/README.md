# Code

Deze map bevat:
- Data: Hierin staan de csv bestanden die worden ingeladen in (inladen map).
- classes: Hierin staan alle classes.
- algo: Hier staan de gebruikte algoritmes die worden gebruikt.
- functies: Hier staan alle functies die in het bestand aangeroepen worden.
- inladen: Hiermee worden de csv bestanden ingeladen. 
- visualisatie: Hiermee wordt alles gevisualiseerd.
- test.png: Autmatisch gegenereerde afbeelding (door main.py en test.py) van de lijnvoering.
- test.py: Testbestand identiek aan main.py
- main.py: Hillclimber aan de hand van nearest neighbour, met random begin stations.
- main2.py: De beste oplossing uit nearest neighbour 'hillclimber' met random begin stations, wordt in een verderzoek algoritme gestopt. 
- main3.py: Tijdens het hillclimben van de nearest neighbour wordt elke oplossing in het verderzoek algoritme gestopt, en vergeleken. 

verderzoek algoritme: Per traject, na het opschonen, wordt aan de hand van random constrains(zie algoritme folder) gekeken of er meer verbindingen behaald kunnen worden bij het traject. Dit wordt per traject bekeken.

Runnen:
- python main.py
- python main2.py
- python main3.py

Hoe pas je de code aan?
- in de 3 mains staan de volgende 3 globale variabelen: 
* HILL) staat voor aantal keer dat het nearest neighbour algoritme wordt gerund. 
* MAX) dit staat voor het aantal maximale minuten per traject. 
* TRAJECTEN) Dit staat voor het aantal trajecten dat je je lijnvoering wilt hebben. 
