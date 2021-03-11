def READ():
    balanceFile = open("data/balance", "r")
    balance = float(balanceFile.read())
    balanceFile.close()
    return balance

def WRITE(file, data, type = "w"):
    balanceInput = open(("data/" + file), type)
    balanceInput.write(str(data))
    balanceInput.close()

def BACNKRUPT(balance, cost):
    if balance - cost < 0:
        return balance, True
    return balance - cost, False
