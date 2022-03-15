import matplotlib.pyplot as plt
import numpy as np
from drawSimulator import *

graphToggle = False

def simulateMultipleDraws(deck, x, tarMana):
    totalData = []
    mulligans =0
    for i in range(x):
        newData = deadDrawSim(deck)
        if(newData[1] >=3):
            totalData.append(newData)
        else:
            mulliganData = deadDrawSim(deck)
            totalData.append(mulliganData)
            mulligans += 1



    totalTurns = []
    totalMana = []
    manaPerTurn =[]
    noLander = 0
    successfulHands = 0

    for x in range(len(totalData)):
        if (totalData[x][1] == 0):
            noLander += 1
        else:
            totalTurns.append(totalData[x][0])
            totalMana.append(totalData[x][1])
            if(totalData[x][1] >= tarMana):
                successfulHands += 1
            manaPerTurn.append((totalData[x][1])/totalData[x][0])

    totalTurns.sort()
    totalMana.sort()
    manaPerTurn.sort()
    probOfTarMana = successfulHands/(len(totalData))

    print("Number of Mulligans: " + str(mulligans))
    print("Number of No Landers: " + str(noLander))
    print("Percent of Successful Hands: " + str(probOfTarMana))
    print("Average Turn That Hit a Wall: "+str(np.average(totalTurns)))
    print("Average Generated Mana: "+str(np.average(totalMana)))

    
    if(graphToggle):
        plt.plot(totalTurns, 'b')
        plt.ylabel("Turn Limit")
        plt.show()

        plt.plot(totalMana, 'g')
        plt.ylabel("Mana Generated")
        plt.show()

        plt.plot(manaPerTurn, 'p')
        plt.ylabel("Mana Generated Per Turn Limit")
        plt.show()