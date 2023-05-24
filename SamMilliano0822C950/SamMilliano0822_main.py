# Samantha Millhart 004640948
import sys
import os
import hashMap
from hashMap import HashMap
from datetime import datetime
from datetime import timedelta
from doctest import master
from gettext import install
from xmlrpc.client import DateTime

import pip

#creates array for the package delivery time for each truck for tracking and checks
truckOneTimeArray = []
truckTwoTimeArray = []
truckThreeTimeArray = []

#setting start time for when each truck leaves thu Hub
truckOneTime = '8:00:00'
truckTwoTime = '9:10:00'
truckThreeTime = '11:10:00'

#converting start times from string into datetime
(shT1, smT1, ssT1) = truckOneTime.split(':')
convertTruckOneTimeStart = timedelta(hours=int(shT1), minutes=int(smT1), seconds=int(ssT1))
(shT2, smT2, ssT2) = truckTwoTime.split(':')
convertTruckTwoTimeStart = timedelta(hours=int(shT2), minutes=int(smT2), seconds=int(ssT2))
(shT3, smT3, ssT3) = truckThreeTime.split(':')
convertTruckThreeTimeStart = timedelta(hours=int(shT3), minutes=int(smT3), seconds=int(ssT3))

#converting each truck time from string into datetime to add time to
(hT1, mT1, sT1) = truckOneTime.split(':')
convertTruckOneTime = timedelta(hours=int(hT1), minutes=int(mT1), seconds=int(sT1))
(hT2, mT2, sT2) = truckTwoTime.split(':')
convertTruckTwoTime = timedelta(hours=int(hT2), minutes=int(mT2), seconds=int(sT2))
(hT3, mT3, sT3) = truckThreeTime.split(':')
convertTruckThreeTime = timedelta(hours=int(hT3), minutes=int(mT3), seconds=int(sT3))

# Function to take the distances traveled and MPH of the truck to find the delivery time for each truck.
# Space-Time Complexity is O(1)
def checkTimeFirstTruck(truckOneMiles, convertTruckOneTime):
    newTime = truckOneMiles / 18
    distanceInMinutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(newTime * 60, 60))
    finalTime = distanceInMinutes + ':00'
    sum = timedelta(hours=int(hT1), minutes=int(mT1), seconds=int(sT1))
    finalTimeHours = int(finalTime.split(':')[0])
    finaltimeMinutes = int(finalTime.split(':')[1])
    finalTimeDelta = timedelta(hours=finalTimeHours, minutes=finaltimeMinutes)
    allTogetherNow = finalTimeDelta + sum
    convertAllTogetherNow = str(allTogetherNow)
    truckOneTimeArray.append(convertAllTogetherNow)
    return allTogetherNow

# Space-Time Complexity is O(1)
def checkTimeSecondTruck(truckTwoMiles, convertTruckTwoTime):
    newTime = truckTwoMiles / 18
    distanceInMinutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(newTime * 60, 60))
    finalTime = distanceInMinutes + ':00'
    sum = timedelta(hours=int(hT2), minutes=int(mT2), seconds=int(sT2))
    finalTimeHours = int(finalTime.split(':')[0])
    finaltimeMinutes = int(finalTime.split(':')[1])
    finalTimeDelta = timedelta(hours=finalTimeHours, minutes=finaltimeMinutes)
    allTogetherNow = finalTimeDelta + sum
    convertAllTogetherNow = str(allTogetherNow)
    truckTwoTimeArray.append(convertAllTogetherNow)
    return allTogetherNow

# Space-Time Complexity is O(1)
def checkTimeThirdTruck(truckThreeMiles, convertTruckThreeTime):
    newTime = truckThreeMiles / 18
    distanceInMinutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(newTime * 60, 60))
    finalTime = distanceInMinutes + ':00'
    sum = timedelta(hours=int(hT3), minutes=int(mT3), seconds=int(sT3))
    finalTimeHours = int(finalTime.split(':')[0])
    finaltimeMinutes = int(finalTime.split(':')[1])
    finalTimeDelta = timedelta(hours=finalTimeHours, minutes=finaltimeMinutes)
    allTogetherNow = finalTimeDelta + sum
    convertAllTogetherNow = str(allTogetherNow)
    truckThreeTimeArray.append(convertAllTogetherNow)
    return allTogetherNow

import csv
class Lambda:
    pass

# opens CSV distances file in program.
with open('C:\\Users\\smill\\OneDrive\\Desktop\\C950\\WGUPS Distance Table Edited.csv') as csvDistanceFile:

# Taking values from CSV file and inserting them in keys (location) and values (distance in miles)
# Space-Time Complexity is O(N)
    spamreader = csv.reader(csvDistanceFile)
    distanceRowDict = {}
    for distanceInRow in spamreader:


        startingLocationRow = distanceInRow[0].replace('\n','')
        westernGovernorsUniversity = distanceInRow[1].replace('\n','')
        internationalPeaceGardens = distanceInRow[2].replace('\n','')
        sugarHousePark = distanceInRow[3].replace('\n','')
        taylorsvilleBennion = distanceInRow[4].replace('\n','')
        saltLakeCityHealthService = distanceInRow[5].replace('\n','')
        southSLCPublicWorks = distanceInRow[6].replace('\n','')
        slcStreetsAndSanitation = distanceInRow[7].replace('\n','')
        dekerLake = distanceInRow[8].replace('\n','')
        slcCityOttingerHall = distanceInRow[9].replace('\n','')
        columbusLibrary = distanceInRow[10].replace('\n','')
        taylorsvilleCityHall = distanceInRow[11].replace('\n','')
        southSLCPolice = distanceInRow[12].replace('\n','')
        councilHall = distanceInRow[13].replace('\n','')
        redwoodPark = distanceInRow[14].replace('\n','')
        slcMentalHealth = distanceInRow[15].replace('\n','')
        slcUnitedPoliceDept = distanceInRow[16].replace('\n','')
        westValleyProsecutor = distanceInRow[17].replace('\n','')
        housingAuthOfSLC = distanceInRow[18].replace('\n','')
        utahDMVAdminOffice = distanceInRow[19].replace('\n','')
        thirdDistJuvenileCourt = distanceInRow[20].replace('\n','')
        cottonwoodRegionalSoftballComplex = distanceInRow[21].replace('\n','')
        holidayCityOffice = distanceInRow[22].replace('\n','')
        murrayCityOffice = distanceInRow[23].replace('\n','')
        valleyRegionalSoftballComplex = distanceInRow[24].replace('\n','')
        cityCenterOfRockSprings = distanceInRow[25].replace('\n','')
        riceTerracePavilionPark = distanceInRow[26].replace('\n','')
        wheelerHistoricalFarm = distanceInRow[27].replace('\n','')

        #grabs rest of the row
        distanceRowDict[startingLocationRow] = distanceInRow[0:]

# with a starting location checks every other location distance to find the closest.
# Space-Time Complexity is O(N)
# sets starting point as hub
pointFrom = '4001 South 700 East'
def distanceLookUp(pointFrom, pointTo, distanceRowDict):
    locationArray = distanceRowDict['DISTANCE BETWEEN HUBS IN MILES']
    columnNumber = locationArray.index(pointTo)
    columnNumberTwo = locationArray.index(pointFrom)
    # switching column and row to avoid blanks where necessary
    if columnNumber > columnNumberTwo:
        tempVarColumn = columnNumber
        columnNumber = columnNumberTwo
        columnNumberTwo = tempVarColumn
        tempVarPoint = pointTo
        pointTo = pointFrom
        pointFrom = tempVarPoint
    rowArray = distanceRowDict[pointFrom]
    distanceBetweenToAndFrom = rowArray[columnNumber]
    return distanceBetweenToAndFrom

#importing the package file
#elimateInLines are packages
import csv
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'WGUPS Package File Edited.csv')
# with open('C:\\Users\\smill\\OneDrive\\Desktop\\C950\\WGUPS Package File Edited.csv ')as csvfile:
with open(filename)as csvfile:
    spamreader = csv.reader(csvfile)

    packageHashMap = HashMap()

# Taking values from CSV file and inserting them in keys (package ID) and values (package info)
# Space-Time Complexity is O(N^2)
    packageDict = {}
    next(csvfile)
    for elementsInLine in spamreader:
        packageId = elementsInLine[0]
        address = elementsInLine[1]
        city = elementsInLine[2]
        state = elementsInLine[3]
        zip = elementsInLine[4]
        deadlineDelivery = elementsInLine[5]
        massKilo = elementsInLine[6]
        specialNotes = elementsInLine[7]
        deliveryStatus = 'at the hub'
        deliveryTime = convertTruckOneTimeStart
        truckNum = ''
        leaveHubTime = ''

        packageDict[packageId] = elementsInLine[1:]

        packageDict[packageId] = [address, city, state, zip, deadlineDelivery, massKilo, specialNotes, deliveryStatus, deliveryTime, truckNum, leaveHubTime]

        value = [packageId, address, city, state, zip, deadlineDelivery, massKilo, specialNotes, deliveryStatus, deliveryTime, truckNum, leaveHubTime]

# Insert value into the hash table

        packageHashMap.insert(packageId, value)

# creates array for the packages

        packageArray = []
        for packageId in packageDict:
            valRow = packageDict[packageId]
            packageArray.append(valRow[0])

# creates array for packages that have special notes not 'must be delivered together'

        truckTwoNotesArray = []
        for packageId in packageDict:
            truckTwoNotesRow = packageDict[packageId]
            if truckTwoNotesRow[6] == 'Must be delivered together':
                pass
            elif truckTwoNotesRow[6].strip():
                truckTwoNotesArray.append(truckTwoNotesRow[0])

# creates array for the packages that have to be delivered together or have to be delivered before EOD with no other special notes

        truckOneNotesArray = []
        for packageId in packageDict:
            truckOneNotesRow = packageDict[packageId]
            if truckOneNotesRow[6] == 'Must be delivered together':
                truckOneNotesArray.append(truckOneNotesRow[0])
            elif truckOneNotesRow[0] in truckTwoNotesArray:
                pass
            elif truckOneNotesRow[4] != 'EOD':
                truckOneNotesArray.append(truckOneNotesRow[0])

# creates a way to look up by row

    distanceArray = []
    for pointFrom in distanceRowDict:
        valRow = distanceRowDict[pointFrom]
        distanceArray.append(valRow[0])

#finding number of packages that fit truck special requirements

    truckOneAddressPackNumArray = []
    for packageId in packageDict:
        addressPackNumRow = packageDict[packageId]
        if packageId in truckOneAddressPackNumArray:
            pass
        elif addressPackNumRow[0] in truckOneNotesArray:
            truckOneAddressPackNumArray.append(packageId)

    truckTwoAddressPackNumArray = []
    for packageId in packageDict:
        addressPackNumRow = packageDict[packageId]
        if packageId in truckTwoAddressPackNumArray:
            pass
        elif addressPackNumRow[0] in truckTwoNotesArray:
            truckTwoAddressPackNumArray.append(packageId)

    #setting starting values
    truckOne = 0
    truckTwo = 0
    truckThree = 0
    truckOneMiles = 0.0
    truckTwoMiles = 0.0
    truckThreeMiles = 0.0
    truckOneCount = len(truckOneAddressPackNumArray)
    truckTwoCount = len(truckTwoAddressPackNumArray)
    totalMiles = 0.0
    numPackages = 0
    totalLocations = 0
    milesReturn = 0
    startingPointFrom = '4001 South 700 East'
    lowestDistance = 100.0
    closestPoint = '4001 South 700 East'
    #creating list of visited places to avoid repeats
    alreadyVisited = ['4001 South 700 East']
    truckOneRoute = ['4001 South 700 East']
    truckOneMilesRoute = []

#creates array of package IDs for each truck for checking purposes
    truckOnePackagesArray = []
    truckTwoPackagesArray = []
    truckThreePackagesArray = []

#running distancelookup to find truck one first location from the hub
# Space-Time Complexity is O(N)
    while truckOne < 1:
        startingPointFrom = '4001 South 700 East'
        lowestDistance = 100
        closestPoint = '4001 South 700 East'
        for nextLocation in distanceArray:
            if nextLocation == 'DISTANCE BETWEEN HUBS IN MILES':
                pass
            elif nextLocation in alreadyVisited:
                pass
            elif nextLocation in truckTwoNotesArray:
                pass
            elif nextLocation not in truckOneNotesArray:
                pass
            else:
                milesDistance = distanceLookUp(startingPointFrom, nextLocation, distanceRowDict)
                convertedMilesDistance = float(milesDistance)
                if convertedMilesDistance > 0.0 and convertedMilesDistance < lowestDistance:
                   lowestDistance = convertedMilesDistance
                   closestPoint = nextLocation
                   # totalMiles = lowestDistance
        alreadyVisited.append(closestPoint)
        truckOneRoute.append(closestPoint)
        truckOneMiles = truckOneMiles + lowestDistance
        truckOneMilesRoute.append(convertedMilesDistance)
        convertTruckOneTime = checkTimeFirstTruck(truckOneMiles, truckOneTime)
        for currentPackageId, currentPackageValue in packageDict.items():
            if currentPackageValue[0] == closestPoint:
                currentPackageValue[7] = 'On Route'
                currentPackageValue[8] = convertTruckOneTime
                currentPackageValue[9] = 'Truck One'
                currentPackageValue[10] = truckOneTime
                truckOnePackagesArray.append(currentPackageId)
                truckOne = truckOne + 1

#running distancelookup to find truck one locations with deadlines and to be delivered together
# Space-Time Complexity is O(N)
    startingPointFrom = closestPoint
    while truckOne < truckOneCount:
        lowestDistance = 100
        for nextLocation in distanceArray:
            if nextLocation == 'DISTANCE BETWEEN HUBS IN MILES':
                pass
            elif nextLocation in truckTwoNotesArray:
                pass
            elif nextLocation not in truckOneNotesArray:
                pass
            elif nextLocation in alreadyVisited:
                pass
            else:
                milesDistance = distanceLookUp(startingPointFrom, nextLocation, distanceRowDict)
                convertedMilesDistance = float(milesDistance)
                if convertedMilesDistance > 0.0 and convertedMilesDistance < lowestDistance:
                    lowestDistance = convertedMilesDistance
                    closestPoint = nextLocation
        if lowestDistance == 100:
            pass
        else:
            truckOneMiles = truckOneMiles + lowestDistance
        alreadyVisited.append(closestPoint)
        truckOneMilesRoute.append(convertedMilesDistance)
        truckOneRoute.append(closestPoint)
        startingPointFrom = closestPoint
        convertTruckOneTime = checkTimeFirstTruck(truckOneMiles, convertTruckOneTime)
        for currentPackageId, currentPackageValue in packageDict.items():
            if currentPackageValue[0] == closestPoint:
                currentPackageValue[7] = 'On Route'
                currentPackageValue[8] = convertTruckOneTime
                currentPackageValue[9] = 'Truck One'
                currentPackageValue[10] = truckOneTime
                truckOne = truckOne + 1
                truckOnePackagesArray.append(currentPackageId)

#running until truck one has 16 packages
# Space-Time Complexity is O(N)
    startingPointFrom = closestPoint
    while truckOne < 16:
        lowestDistance = 100
        for nextLocation in distanceArray:
            if nextLocation == 'DISTANCE BETWEEN HUBS IN MILES':
                pass
            elif nextLocation in truckTwoNotesArray:
                pass
            elif nextLocation in alreadyVisited:
                pass
            else:
                milesDistance = distanceLookUp(startingPointFrom, nextLocation, distanceRowDict)
                convertedMilesDistance = float(milesDistance)
                if convertedMilesDistance > 0.0 and convertedMilesDistance < lowestDistance:
                    lowestDistance = convertedMilesDistance
                    closestPoint = nextLocation
        if lowestDistance == 100:
            pass
        else:
            truckOneMiles = truckOneMiles + lowestDistance
        alreadyVisited.append(closestPoint)
        truckOneMilesRoute.append(convertedMilesDistance)
        truckOneRoute.append(closestPoint)
        startingPointFrom = closestPoint
        convertTruckOneTime = checkTimeFirstTruck(truckOneMiles, convertTruckOneTime)
        for currentPackageId, currentPackageValue in packageDict.items():
            if currentPackageValue[0] == closestPoint:
                currentPackageValue[7] = 'On Route'
                currentPackageValue[8] = convertTruckOneTime
                currentPackageValue[9] = 'Truck One'
                currentPackageValue[10] = truckOneTime
                truckOne = truckOne + 1
                truckOnePackagesArray.append(currentPackageId)

# Returning Driver to Hub to take out Truck Three

    truckOneLastPoint = closestPoint
    truckOneReturnMiles = distanceLookUp(truckOneLastPoint, '4001 South 700 East', distanceRowDict)
    convertedTOneReturnMiles = float(truckOneReturnMiles)
    truckOneTotalMiles = truckOneMiles + convertedTOneReturnMiles
    numPackages = truckOne + truckTwo + truckThree
    returnTruckOneTime = checkTimeFirstTruck(truckOneTotalMiles, convertTruckOneTime)


# running distancelookup to find truck two first location from the hub
# Space-Time Complexity is O(N)
    truckTwoRoute = ['4001 South 700 East']
    truckTwoMilesArray = []
    while truckTwo < 1:
        startingPointFrom = '4001 South 700 East'
        lowestDistance = 100.0
        closestPoint = '4001 South 700 East'
        for nextLocation in distanceArray:
            if nextLocation == 'DISTANCE BETWEEN HUBS IN MILES':
                pass
            elif nextLocation in alreadyVisited:
                pass
            elif nextLocation not in truckTwoNotesArray:
                pass
            else:
                milesDistance = distanceLookUp(startingPointFrom, nextLocation, distanceRowDict)
                convertedMilesDistance = float(milesDistance)
                if convertedMilesDistance > 0.0 and convertedMilesDistance < lowestDistance:
                    lowestDistance = convertedMilesDistance
                    closestPoint = nextLocation
                    # totalMiles = lowestDistance
        alreadyVisited.append(closestPoint)
        truckTwoRoute.append(closestPoint)
        truckTwoMilesArray.append(convertedMilesDistance)
        truckTwoMiles = truckTwoMiles + convertedMilesDistance
        convertTruckTwoTime = checkTimeSecondTruck(truckTwoMiles, convertTruckTwoTime)
        for currentPackageId, currentPackageValue in packageDict.items():
            if currentPackageValue[0] == closestPoint:
                currentPackageValue[7] = 'On Route'
                currentPackageValue[8] = convertTruckTwoTime
                currentPackageValue[9] = 'Truck Two'
                currentPackageValue[10] = truckTwoTime
                truckTwo = truckTwo + 1
                truckTwoPackagesArray.append(currentPackageId)

# running distancelookup to find truck two locations until it has 16 packages
# Space-Time Complexity is O(N)
        startingPointFrom = closestPoint
        while truckTwo <= truckTwoCount:
            lowestDistance = 100.0
            for nextLocation in distanceArray:
                if nextLocation == 'DISTANCE BETWEEN HUBS IN MILES':
                    pass
                elif nextLocation not in truckTwoNotesArray:
                    pass
                elif nextLocation in alreadyVisited:
                    pass
                else:
                    milesDistance = distanceLookUp(startingPointFrom, nextLocation, distanceRowDict)
                    convertedMilesDistance = float(milesDistance)
                    if convertedMilesDistance > 0.0 and convertedMilesDistance < lowestDistance:
                        lowestDistance = convertedMilesDistance
                        closestPoint = nextLocation
            if lowestDistance == 100:
                pass
            else:
                truckTwoMiles = truckTwoMiles + lowestDistance
            alreadyVisited.append(closestPoint)
            truckTwoRoute.append(closestPoint)
            truckTwoMilesArray.append(convertedMilesDistance)
            startingPointFrom = closestPoint
            totalMiles = totalMiles + lowestDistance
            convertTruckTwoTime = checkTimeSecondTruck(truckTwoMiles, convertTruckTwoTime)
            for currentPackageId, currentPackageValue in packageDict.items():
                if currentPackageValue[0] == closestPoint:
                    currentPackageValue[7] = 'On Route'
                    currentPackageValue[8] = convertTruckTwoTime
                    currentPackageValue[9] = 'Truck Two'
                    currentPackageValue[10] = truckTwoTime
                    truckTwo = truckTwo + 1
                    truckTwoPackagesArray.append(currentPackageId)
        numPackages = truckOne + truckTwo + truckThree

# running distancelookup to find truck three first location from the hub
# Space-Time Complexity is O(N)
    truckThreeRoute = ['4001 South 700 East']
    while truckThree < 1:
        startingPointFrom = '4001 South 700 East'
        lowestDistance = 100.0
        closestPoint = '4001 South 700 East'
        for nextLocation in distanceArray:
            if nextLocation == 'DISTANCE BETWEEN HUBS IN MILES':
                pass
            elif nextLocation in alreadyVisited:
                pass
            else:
                milesDistance = distanceLookUp(startingPointFrom, nextLocation, distanceRowDict)
                convertedMilesDistance = float(milesDistance)
                if convertedMilesDistance > 0.0 and convertedMilesDistance < lowestDistance:
                    lowestDistance = convertedMilesDistance
                    closestPoint = nextLocation
                    # totalMiles = lowestDistance
        if lowestDistance == 100:
            pass
        else: truckThreeMiles = truckThreeMiles + lowestDistance
        convertTruckThreeTime = checkTimeThirdTruck(truckThreeMiles, convertTruckThreeTime)
        alreadyVisited.append(closestPoint)
        truckThreeRoute.append(closestPoint)
        for currentPackageId, currentPackageValue in packageDict.items():
            if currentPackageValue[0] == closestPoint:
                currentPackageValue[7] = 'On Route'
                currentPackageValue[8] = convertTruckThreeTime
                currentPackageValue[9] = 'Truck Three'
                currentPackageValue[10] = truckThreeTime
                truckThree = truckThree + 1
                truckThreePackagesArray.append(currentPackageId)

# running distancelookup to find truck three locations until it has 16 packages
# Space-Time Complexity is O(N)
        startingPointFrom = closestPoint
        closestPoint = closestPoint
        # totalMiles = totalMiles
        while truckThree >= 1 and truckThree <= 12:
            lowestDistance = 100.0
            for nextLocation in distanceArray:
                if nextLocation == 'DISTANCE BETWEEN HUBS IN MILES':
                    pass
                elif nextLocation in alreadyVisited:
                    pass
                else:
                    milesDistance = distanceLookUp(startingPointFrom, nextLocation, distanceRowDict)
                    convertedMilesDistance = float(milesDistance)
                    if convertedMilesDistance > 0.0 and convertedMilesDistance < lowestDistance:
                        lowestDistance = convertedMilesDistance
                        closestPoint = nextLocation
            if lowestDistance == 100:
                pass
            else:
                truckThreeMiles = truckThreeMiles + lowestDistance
            startingPointFrom = closestPoint
            convertTruckThreeTime = checkTimeThirdTruck(truckThreeMiles, convertTruckThreeTime)
            alreadyVisited.append(closestPoint)
            truckThreeRoute.append(closestPoint)
            # totalMiles = truckOneMiles + truckTwoMiles + truckThreeMiles
            for currentPackageId, currentPackageValue in packageDict.items():
                if currentPackageValue[0] == closestPoint:
                    currentPackageValue[7] = 'On Route'
                    currentPackageValue[8] = convertTruckThreeTime
                    currentPackageValue[9] = 'Truck Three'
                    currentPackageValue[10] = truckThreeTime
                    truckThree = truckThree + 1
                    truckThreePackagesArray.append(currentPackageId)
            numPackages = truckOne + truckTwo + truckThree

        totalTruckMiles = truckOneMiles + truckTwoMiles + truckThreeMiles + convertedTOneReturnMiles


#starting interface
        print('Welcome! Total Miles Traveled: ', totalTruckMiles)
# getting user input
        userInput = input("""
                                Please select an option below or type 'quit' to quit:
                                1. See all package
                                2. Search for a package""")

# Space-Time Complexity is O(N)
        while userInput != 'quit':
            if userInput == '1':
                try:
                    inputTime = input('Enter a Time as HH:MM:SS')
                    (hrs, mins, secs) = inputTime.split(':')
                    convertInputTime = timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                    for currentPackageId, currentPackageValue in packageDict.items():
                        startTime = currentPackageValue[10]
                        timeDelivered = currentPackageValue[8]
                        (sthrs, stmins, stsecs) = startTime.split(':')
                        convertStartTime = timedelta(hours=int(sthrs), minutes=int(stmins), seconds=int(stsecs))

                        if convertStartTime >= convertInputTime:
                            packageHashMap.getValue(str(currentPackageId))[8] = 'At Hub'

                        elif convertStartTime < convertInputTime and convertInputTime < timeDelivered:
                            packageHashMap.getValue(str(currentPackageId))[8] = 'On Route'

                        elif convertStartTime < convertInputTime and convertInputTime > timeDelivered:
                             packageHashMap.getValue(str(currentPackageId))[8] = 'Delivered'


                        print(
                            f'Package ID: {packageHashMap.getValue(str(currentPackageId))[0]}   '
                            f'Delivery status: {packageHashMap.getValue(str(currentPackageId))[8]}  '
                            f'Delivery Time: {timeDelivered}    '
                            f'Start Time: {convertStartTime}    '
                        )

                except IndexError:
                    print(IndexError)
                    exit()
                except ValueError:
                    print('Invalid Entry')
                    exit()

            elif userInput == '2':
                try:
                    inputSearch = input('Enter a valid package ID')
                    inputTime = input('Enter a Time as HH:MM:SS')
                    (hrs, mins, secs) = inputTime.split(':')
                    convertInputTime = timedelta(hours = int(hrs), minutes = int(mins), seconds = int(secs))

                    for currentPackageId, currentPackageValue in packageDict.items():
                        startTime = currentPackageValue[10]
                        timeDelivered = currentPackageValue[8]
                        (sthrs, stmins, stsecs) = startTime.split(':')
                        convertStartTime = timedelta(hours=int(sthrs), minutes=int(stmins), seconds=int(stsecs))

                        if convertStartTime >= convertInputTime:
                            packageHashMap.getValue(str(currentPackageId))[8] = 'At Hub'

                        elif convertStartTime < convertInputTime and convertInputTime < timeDelivered:
                            packageHashMap.getValue(str(currentPackageId))[8] = 'On Route'

                        elif convertStartTime < convertInputTime and convertInputTime > timeDelivered:
                            packageHashMap.getValue(str(currentPackageId))[8] = 'Delivered'

                        if inputSearch == currentPackageId:

                            print(
                                f'Package ID: {packageHashMap.getValue(str(currentPackageId))[0]}\n'
                                f'Delivery status: {packageHashMap.getValue(str(currentPackageId))[8]}\n'
                                f'Delivery Time: {timeDelivered}\n'
                                f'Start Time: {convertStartTime}\n'
                            )
                except IndexError:
                    print(IndexError)
                    exit()
                except ValueError:
                    print('Invalid Entry')
                    exit()

            elif userInput == 'quit':
                exit()

            else:
                print ('Invalid entry')
                exit()