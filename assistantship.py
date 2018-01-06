def findTime(jobsDistribution, inputTable):
    returnValue = 0
    for i in range(0, len(jobsDistribution)):
        returnValue += 6 if jobsDistribution[i] == -1 else inputTable[i][jobsDistribution[i]]
    return returnValue

def findAllJobsDistributions(distribution, jobs, allDistributions):
    jobsLeft = len(jobs)
    if jobsLeft == 0:
        allDistributions.append(distribution)
    else:
        for next in jobs:
            distributionCpy = list(distribution)
            jobsCpy = list(jobs)
            distributionCpy.append(next)
            jobsCpy.remove(next)
            findAllJobsDistributions(distributionCpy, jobsCpy, allDistributions)

def findOptimalAssistantship(inputTable):
    numberOfJobs = len(inputTable[0])
    numberOfRA = len(inputTable)
    jobs = list(range(numberOfJobs))
    for i in range(numberOfJobs,numberOfRA):
        jobs.append(-1)

    allDistributions = []
    findAllJobsDistributions([], jobs, allDistributions)

    asst = []
    time = 99999999999
    for nextDistribution in allDistributions:
        nextTime = findTime(nextDistribution, inputTable)
        if nextTime < time:
            time = nextTime
            asst = nextDistribution

    return asst, time



asst, time = findOptimalAssistantship([[5,8,7],
                                [8,12,7],
                                [4,8,5]])
print(asst, time)