import csv

def readFile():

    dataSet = []

    with open('dataset/teste.csv', 'rb') as csvfile:
    #with open('machine.data', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        #reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            #machine
            #dataSet.append(row[2] + ', ' + row[9])
            #precos
            dataSet.append(row[0] + ', ' + row[1])
    return dataSet
