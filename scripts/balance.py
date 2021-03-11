def READ():
    balanceFile = open("data/balance", 'r')
    balance = float(balanceFile.read())
    balanceFile.close()
    return balance

def WRITE(balance):
    balanceInput = open('data/balance', 'w')
    balanceInput.write(str(balance))
    balanceInput.close()

def BACNKRUPT(balance, cost):
    if balance - cost < 0:
        return balance, False
    return balance - cost, True