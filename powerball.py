import random
import math
import timeit

def getPowerball():
    return int(math.ceil(random.random() * 26))

def getNumber():
    return int(math.ceil(random.random() * 69))

def generateRandomTickets(numberOfTickets):
    AllTickets = []
    for i in range(0,numberOfTickets):
        ticket = []
        for j in range(0,5):
            number = getNumber()
            while ticket.count(number) > 0:
                number = getNumber()
            ticket.append(number)
        ticket.append(getPowerball())
        AllTickets.append(ticket)
    return AllTickets

def generateDistributedRandomTickets(numberOfTickets):
    AllTickets = []
    for i in range(0,numberOfTickets):
        ticket = []
        for j in range(0,5):
            number = getNumber()
            while ticket.count(number) > 0:
                number = getNumber()
            ticket.append(number)
        ticket.append((i % 26) + 1)
        AllTickets.append(ticket)
    return AllTickets

def generateSemirandomTickets(numberOfTickets):
    AllTickets = []
    tony = [9, 11, 23, 32, 64, 21]
    crispy = [3, 4, 13, 23, 43, 7]
    tony2 = [43, 44, 45, 46, 47, 1]
    edward = [22, 41, 45, 60, 69, 4]
    francis = [2, 10, 13, 22, 23, 7]
    AllTickets.append(tony)
    AllTickets.append(crispy)
    AllTickets.append(tony2)
    AllTickets.append(edward)
    AllTickets.append(francis)
    for i in range(0,numberOfTickets-5):
        ticket = []
        for j in range(0,5):
            number = getNumber()
            while ticket.count(number) > 0:
                number = getNumber()
            ticket.append(number)
        ticket.append(getPowerball())
        AllTickets.append(ticket)
    return AllTickets

def generateWinningNumbers():
    WinningNumbers = []
    for i in range(0,5):
        number = getNumber()
        while WinningNumbers.count(number) > 0:
            number = getNumber()
        WinningNumbers.append(number)
    WinningNumbers.append(getPowerball())
    return WinningNumbers

def checkWinner(ticket, winningNumbers):
    match = 0
    powerball = ticket.pop()
    for i in range(0,5):
        match = match + ticket.count(winningNumbers[i])
    ticket.append(powerball)
    powerball = 0
    if ticket[5] == winningNumbers[5]:
        powerball = 1
    return [match, powerball]

def calculateProfit(result):
    if result[1] == 0:
        if result[0] == 3:
            return 7
        elif result[0] == 4:
            return 100
        elif result[0] == 5:
            return 1000000
        else:
            return 0
    elif result[1] == 1:
        if result[0] == 2:
            return 7
        elif result[0] == 3:
            return 100
        elif result[0] == 4:
            return 50000
        elif result[0] == 5:
            return 1400000000
        else:
            return 4

start = timeit.default_timer()

numberOfTickets = 126

simulations = 1000000

outputFile = open("powerball.txt", "w")

outputFile.write("Powerball simulation\n\n")
outputFile.write("Number of tickets bought: " + str(numberOfTickets) + "\n")
outputFile.write("Number of simulations: " + str(simulations) + "\n\n")

randomJackpot = 0
semirandomJackpot = 0
distributedJackpot = 0
randomTotal = 0
semirandomTotal = 0
distributedTotal = 0
for i in range(0,simulations):
    if (i % 100000) == 0 and i > 0:
        print str(i / simulations) + "% complete"
    randomTickets = generateRandomTickets(numberOfTickets)
    semirandomTickets = generateSemirandomTickets(numberOfTickets)
    distributedTickets = generateDistributedRandomTickets(numberOfTickets)
    winningNumbers = generateWinningNumbers()
    for j in range(0, numberOfTickets):
        result = checkWinner(randomTickets[j],winningNumbers)
        if result[0] == 5 and result[1] == 1:
            randomJackpot += 1
            print "jackpot!"
            print "ticket: " + str(randomTickets[j])
            print "winning number: " + str(winningNumbers)
        randomTotal = randomTotal + calculateProfit(result)
        result = checkWinner(semirandomTickets[j],winningNumbers)
        if result[0] == 5 and result[1] == 1:
            semirandomJackpot += 1
            print "jackpot!"
            print "ticket: " + str(semirandomTickets[j])
            print "winning number: " + str(winningNumbers)
        semirandomTotal = semirandomTotal + calculateProfit(result)
        result = checkWinner(distributedTickets[j],winningNumbers)
        if result[0] == 5 and result[1] == 1:
            distributedJackpot += 1
            print "jackpot!"
            print "ticket: " + str(distributedTickets[j])
            print "winning number: " + str(winningNumbers)
        distributedTotal = distributedTotal + calculateProfit(result)

randomAverage = randomTotal / simulations
semirandomAverage = semirandomTotal / simulations
distributedAverage = distributedTotal / simulations

outputFile.write("Random Tickets:\n")
outputFile.write("-------------------------------------\n")
outputFile.write("Average winnings: ")
outputFile.write(str(randomAverage) + "\n")
outputFile.write("Jackpots hit: ")
outputFile.write(str(randomJackpot) + "\n\n")

outputFile.write("Non-random Tickets:\n")
outputFile.write("-------------------------------------\n")
outputFile.write("Average winnings: ")
outputFile.write(str(semirandomAverage) + "\n")
outputFile.write("Jackpots hit: ")
outputFile.write(str(semirandomJackpot) + "\n\n")

outputFile.write("Distributed Random Tickets:\n")
outputFile.write("-------------------------------------\n")
outputFile.write("Average winnings: ")
outputFile.write(str(distributedAverage) + "\n")
outputFile.write("Jackpots hit: ")
outputFile.write(str(distributedJackpot) + "\n\n")

stop = timeit.default_timer()
outputFile.write("total elapsed time: ")
outputFile.write(str(stop-start) + " seconds")
