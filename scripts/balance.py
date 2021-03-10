def READ():
    dataFile = open("data/balance", 'r')
    balance = float(dataFile.read())
    dataFile.close()
    return balance

def DUMP(balance):
    return balance
