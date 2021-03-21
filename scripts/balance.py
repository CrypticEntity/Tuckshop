def READ():
    try:
        balanceFile = open("data/balance", "r")
    except:
        WRITE("balance", "0")
        balanceFile = open("data/balance", 'r')
    balance = float(balanceFile.read())
    balanceFile.close()
    return balance

def WRITE(file, data, type = "w"):
    dataFile = open(("data/" + file), type)
    dataFile.write(str(data))
    dataFile.close()

def BACNKRUPT(balance, cost):
    if balance - cost < 0:
        return balance, True
    return round(balance - cost, 2), False
