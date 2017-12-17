import matplotlib.pyplot as plt
import numpy as np
import csv



	# Lijsten


	# Dit is een visualisatie aanvraag voor 4 trajecten:


	# Dit is een visualisatie aanvraag voor 0 trajecten, dit levert een lege lijnvoering op:
	#alleTrajecten = [[]]

def visualisatie(x, STATIONS, VERBINDINGEN):
    
    stations = []
    xcoordinates = []
    ycoordinates = []
    lengte = [] 
    
    with open(STATIONS) as f:
        reader = csv.reader(f)
        for row in reader:
            
            stations.append(row[0])
            xcoordinates.append(row[1])
            ycoordinates.append(row[2])
            
    verbinding1 = []
    verbinding2 = []
    somTotaal = 0
    connectiesholland = []

    # 16 kleuren, voor 16 verschillende trajecten.
    colors = ["olive","orange", "green", "blue", "black", "red", "pink","yellow","purple","cyan","brown","magenta","aqua","teal","maroon","fuchsia" ]
    counter = 0
    with open(VERBINDINGEN) as f:
        reader = csv.reader(f)
        
        for row in reader:
            if counter != 0:
                
                
                verbinding1.append(row[0])
                verbinding2.append(row[1])
                lengte.append(row[2])

                connectiesholland.append(row)
                
                somTotaal = somTotaal + float(row[2])
            counter +=1
            
            
    for j in range(0,len(verbinding1)):
            counter1 = stations.index(verbinding1[j])
            verbinding1x = float(xcoordinates[counter1])
            verbinding1y = float(ycoordinates[counter1])
            counter2 = stations.index(verbinding2[j])
            verbinding2x = float(xcoordinates[counter2])
            verbinding2y = float(ycoordinates[counter2])

            plt.plot([verbinding1y,verbinding2y],[verbinding1x,verbinding2x], marker = 'o', color = '0.9')

            plt.xticks([])
            plt.yticks([])
            # Ga door de lijst met alle trajecten.
            for i in range(0, len(x)):
                
                    # Ga alle stations af per traject.
                for k in range(0,len(x[i])-1):

                    counterinput1 = stations.index(x[i][k])
                    verbinding1xinput = float(xcoordinates[counterinput1])
                    verbinding1yinput = float(ycoordinates[counterinput1]) 

                    counterinput2 = stations.index(x[i][k+1])
                    verbinding2xinput = float(xcoordinates[counterinput2])
                    verbinding2yinput = float(ycoordinates[counterinput2]) 

                    plt.plot([verbinding1yinput,verbinding2yinput],[verbinding1xinput,verbinding2xinput], marker = 'o', color = colors[i])


                

                
                #plt.text((verbinding1y + verbinding2y) /2, (verbinding1x + verbinding2x) / 2, lengte[j])
                


            

    # Weergeef een aantal plaatsnamen om overzicht te krijgen.			
    plt.text(4.5,53, "Den Helder")
    plt.text(3.6,51.3, "Vlissingen")
    plt.text(5.5,51, "Maastricht")
    plt.text(6.7,52, "Enschede")
    plt.text(6.15,53.05, "Groningen")
    plt.text(4.87,51.97, "Utrecht")
    plt.text(5.4,52.57, "Lelystad")
    plt.text(6.23,51.35, "Venlo")
    plt.text(5.29,51.37, "Eindhoven")
    plt.text(4.74,51.53, "Breda")
    plt.text(4.11,52.18, "Den Haag")
    plt.text(6.55,52.47, "Almelo")
    plt.text(6.12, 51.99, "Nijmegen")
    plt.title('Lijnvoering Nederland')
    plt.savefig("test.png")

    plt.show()







    





	
	
	





