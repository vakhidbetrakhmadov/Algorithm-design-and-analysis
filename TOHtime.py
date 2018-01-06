def simulateTOH(SRC, AUX, DST, diskNum, elapsedTimes):
    if(diskNum == 1):
        print('disk {0}: {1} to {2}'.format(diskNum,SRC[0],DST[0]))
        elapsedTimes[diskNum - 1] = elapsedTimes[diskNum - 1] + abs(diskNum * (DST[1] - SRC[1]))
    else:
        simulateTOH(SRC,DST,AUX,diskNum - 1,elapsedTimes)
        print('disk {0}: {1} to {2}'.format(diskNum, SRC[0], DST[0]))
        elapsedTimes[diskNum - 1] = elapsedTimes[diskNum - 1] + abs(diskNum * (DST[1] - SRC[1]))
        simulateTOH(AUX, SRC, DST, diskNum - 1,elapsedTimes)


def calculateTOHtimes(diskNum):
    elapsedTimes = [0] * diskNum

    simulateTOH(('SRC', 0), ('AUX', 1), ('DST', 2), 3, elapsedTimes)

    for i in range(0, diskNum):
        print('Elapsed time for disk {0}: {1}'.format(i+1, elapsedTimes[i]))


calculateTOHtimes(3)