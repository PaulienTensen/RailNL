import matplotlib.pyplot as plt
import numpy as np
import csv
from tabulate import tabulate

stations = []
xcoordinates = []
ycoordinates = []
lengte = [] 
with open('C:\Users\Gebruiker\Desktop\Programmeer minor\Heuristieken\StationsHolland.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        
        stations.append(row[0])
        xcoordinates.append(row[1])
        ycoordinates.append(row[2])
        
verbinding1 = []
verbinding2 = []


connectiesholland = []
with open('C:\Users\Gebruiker\Desktop\Programmeer minor\Heuristieken\ConnectiesHolland.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        verbinding1.append(row[0])
        verbinding2.append(row[1])
        lengte.append(row[2])
        connectiesholland.append(row)
    
        
        
for j in range(0,len(verbinding1)):
        counter1 = stations.index(verbinding1[j])
        verbinding1x = float(xcoordinates[counter1])
        verbinding1y = float(ycoordinates[counter1])
        counter2 = stations.index(verbinding2[j])
        verbinding2x = float(xcoordinates[counter2])
        verbinding2y = float(ycoordinates[counter2])

        
        plt.text((verbinding1y + verbinding2y) /2, (verbinding1x + verbinding2x) / 2, lengte[j])
        plt.plot([verbinding1y,verbinding2y],[verbinding1x,verbinding2x], marker = 'o')
        plt.xticks([])
        plt.yticks([])

plt.title('Lijnvoering MPT')
plt.savefig("test.png")



graaf = {'Dordrecht': [(['Rotterdam Centraal'], ['17'])], 'Delft': [(['Den Haag Centraal'], ['13']), (['Schiedam Centrum'], ['7'])], 'Alkmaar': [(['Hoorn'], ['24']), (['Den Helder'], ['36']), (['Castricum'], ['9'])], 'Den Haag Centraal': [(['Delft'], ['13']), (['Gouda'], ['18']), (['Leiden Centraal'], ['12'])], 'Schiphol Airport': [(['Amsterdam Zuid'], ['6']), (['Leiden Centraal'], ['15'])], 'Schiedam Centrum': [(['Rotterdam Centraal'], ['5']), (['Delft'], ['7'])], 'Den Helder': [(['Alkmaar'], ['36'])], 'Rotterdam Centraal': [(['Dordrecht'], ['17']), (['Schiedam Centrum'], ['5']), (['Rotterdam Alexander'], ['8'])], 'Heemstede-Aerdenhout': [(['Haarlem'], ['6']), (['Leiden Centraal'], ['13'])], 'Leiden Centraal': [(['Den Haag Centraal'], ['12']), (['Heemstede-Aerdenhout'], ['13']), (['Alphen a/d Rijn'], ['14']), (['Schiphol Airport'], ['15'])], 'Amsterdam Amstel': [(['Amsterdam Zuid'], ['10']), (['Amsterdam Centraal'], ['8'])], 'Alphen a/d Rijn': [(['Gouda'], ['19']), (['Leiden Centraal'], ['14'])], 'Amsterdam Centraal': [(['Amsterdam Amstel'], ['8']), (['Amsterdam Sloterdijk'], ['6'])], 'Beverwijk': [(['Castricum'], ['13']), (['Haarlem'], ['16']), (['Zaandam'], ['25'])], 'Zaandam': [(['Amsterdam Sloterdijk'], ['6']), (['Castricum'], ['12']), (['Beverwijk'], ['25']), (['Hoorn'], ['26'])], 'Amsterdam Sloterdijk': [(['Amsterdam Centraal'], ['6']), (['Haarlem'], ['11']), (['Zaandam'], ['6']), (['Amsterdam Zuid'], ['16'])], 'Castricum': [(['Beverwijk'], ['13']), (['Alkmaar'], ['9']), (['Zaandam'], ['12'])], 'Hoorn': [(['Alkmaar'], ['24']), (['Zaandam'], ['26'])], 'Rotterdam Alexander': [(['Gouda'], ['10']), (['Rotterdam Centraal'], ['8'])], 'Amsterdam Zuid': [(['Amsterdam Amstel'], ['10']), (['Amsterdam Sloterdijk'], ['16']), (['Schiphol Airport'], ['6'])], 'Gouda': [(['Den Haag Centraal'], ['18']), (['Alphen a/d Rijn'], ['19']), (['Rotterdam Alexander'], ['10'])], 'Haarlem': [(['Amsterdam Sloterdijk'], ['11']), (['Beverwijk'], ['16']), (['Heemstede-Aerdenhout'], ['6'])]}

matrix = [["x" for x in range(len(stations) + 1)] for y in range(len(stations) + 1)] 

# Make the matrix
for i in range(0,len(stations)):
    matrix[i][i] = "x"
    matrix[0][0] == "x"
    matrix[0][i+1] = stations[i][:6]
    matrix[i+1][0] = stations[i][:6]
    
#print matrix
#print np.matrix(matrix)



for i in range(0, len(stations)):
    for index, elem in enumerate(graaf[stations[i]]):
        for idex2, elem2 in enumerate(stations):
            if elem2 == elem[0][0]:
                matrix[i + 1][idex2 + 1] = elem[1][0]
                matrix[idex2 + 1][i + 1] = elem[1][0]
    
print tabulate(matrix)
#    print graaf[matrix[0][i]]

#    for j in range(len(matrix[0][i])):
#        print stations.index("graaf[matrix[0][i][j]") 
#print graaf["Delft"]
arraymatrix = np.array(matrix)     
#print arraymatrix[:,0]


def function(beginstation):
    for i in range(0, len(arraymatrix[:,0])):
        if arraymatrix[:,0][i] == beginstation:
            print arraymatrix[i,:]
            listOfNumbers = []
            listOfIndexes = []
            index = -1
            for el in arraymatrix[i,:]:
                index += 1
                try:
                    listOfNumbers.append(int(el))
                    listOfIndexes.append(index)

                except ValueError:
                    pass
    
    # Verwerk de lijst met indexen naar een ijst met stations.
    listOfStations = []
    for i in range(0, len(listOfIndexes)):
        listOfStations.append(stations[listOfIndexes[i] - 1])
    print listOfStations
    print listOfNumbers


    # Vind de kortste route en het bijbehorende station.
    shortestRoute = min(listOfNumbers)
    correspondingStation = listOfStations[listOfNumbers.index(shortestRoute)]
    
    print "Het is maar " ,shortestRoute, "minuutjes reizen TJOEK TJOEK"


    return correspondingStation

   



        





    
    
    

