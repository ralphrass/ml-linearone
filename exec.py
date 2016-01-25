import read as r

dataSet = r.readFile()

ALPHA = 0.026
THETA_0, THETA_1, nrIterations = 0, 0, 0
M = float(len(dataSet))
CONVERGENCE_LIMIT = 10**-4 * 1.15
ITERATIONS_LIMIT = M**2

def getValue(row, i):
    return int(row.split(',')[i])

def costFunction(THETA_0, THETA_1):
    SUM = 0
    for row in dataSet:
        X = getValue(row, 0)
        Y = getValue(row, 1)
        SUM += (THETA_0 + THETA_1 * X - Y) ** 2

    cost = 1/(2*M) * SUM
    return cost

#gradient descent iterations
while True:

    SUM_THETA_0, SUM_THETA_1 = 0, 0
    cost = costFunction(THETA_0, THETA_1)
    for row in dataSet:
        X = getValue(row, 0)
        Y = getValue(row, 1)
        H0 = THETA_0 + THETA_1 * X
        SUM_THETA_0 += H0 - Y
        SUM_THETA_1 += (H0 - Y) * X

    THETA_0 = THETA_0 - (ALPHA * (1/M)) * SUM_THETA_0
    THETA_1 = THETA_1 - (ALPHA * (1/M)) * SUM_THETA_1

    newCost = costFunction(THETA_0, THETA_1)

    if (abs(newCost - cost) < CONVERGENCE_LIMIT):
        break
    elif (nrIterations == ITERATIONS_LIMIT):
        break

    nrIterations += 1

X = raw_input('Wich base-value do you want to use to make a prediction? ')

h0 = THETA_0 + THETA_1 * int(X)

print 'Predicted value is', int(h0), 'the loop was executed', nrIterations, 'times'
