''' This is an automated simulation of the classic Monty Hall Problem. It is modified
with settings to show that switching will always provide a 2/3 favor over staying with
the same choice and this can be shown numerically as the number of iterations increases.
Other settings, like the chance that a contestant will switch to a door is taken into account
and can be modified.'''

__author__ = "Adithya Iyengar"

import random
import numpy as np
import matplotlib.pyplot as plt

_iterations = 10000 #This controls the number of iterations, the more iterations the more accurate
#Used for wins/losses calculations and plots at the end
winCount = 0
winArray = []
lossCount = 0
lossArray = []

for i in range(_iterations):
    #Initialize doors and randomize one door to be the car
    doors = [0,0,0]
    doors[random.randrange(3)] = 1
    print(doors)

    #Choose first door (contestant) at random
    firstDoor = random.randrange(3)
    print("Contestant has chosen Door", firstDoor+1)

    #Choose door from other two possiblities that has a goat and also know the door that contains the car.
    goatDoor = 0
    carDoor = 0
    for i in range(len(doors)):
        if doors[i] == 0 and i != firstDoor:
            goatDoor = i
        if doors[i] == 1:
            carDoor = i
    #Door that contestant has the chance to switch to.
    switchDoor = 5-(firstDoor+1)-(goatDoor+1)
    print("Door", goatDoor+1, "has a goat behind it! Would you like to switch to Door", switchDoor+1)
    #Probability to see if contestant switches and check if correct
    #Assumes humans will decide to switch half the time
    #switch = random.randrange(2)
    #Assumes humans will switch all the time when presented with the opportunity
    switch = True
    #Function to check if contestant won car.
    def checkwin(choice):
        if doors[choice] == doors[carDoor]:
            print("You won")
            global winCount
            winCount += 1
        else:
            print("You lost")
            global lossCount
            lossCount += 1
    #Set to see that contestant always switches, modify conditional along with switch variable above to get different results.
    if not switch:
        print("You chose to stay")
        checkwin(firstDoor)
    else:
        print("You chose to switch")
        checkwin(switchDoor)
    winArray.append(winCount)
    lossArray.append(lossCount)

#Wins/Losses

#Plot out wins/losses
plt.plot(winArray)
plt.plot(lossArray)
plt.xlim(1000)
plt.ylabel("Wins/Losses")
plt.xlabel("Iterations")
plt.show()
#Print out game statistics
totalCount = winCount + lossCount
print("Games Played:", totalCount)
print("Win Count:", winCount)
print("Loss Count:", lossCount)
print("Winning Probability:", winCount/totalCount*100)
print("Losing Probability:", lossCount/totalCount*100)
