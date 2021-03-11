def READ():
    balanceFile = open("data/balance", 'r')
    balance = float(balanceFile.read())
    balanceFile.close()
    return balance

def WRITE(file, data):
    balanceInput = open(('data/' + file), 'w')
    balanceInput.write(str(data))
    balanceInput.close()

def BACNKRUPT(balance, cost):
    if balance - cost < 0:
        return balance, False
    return balance - cost, True
