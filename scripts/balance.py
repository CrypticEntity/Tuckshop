def READ():
    balanceFile = open("data/balance", 'r')
    balance = float(balanceFile.read())
    balanceFile.close()
    return balance

def WRITE(balance):
    balanceInput = open('data/balance', 'w')
    balanceInput.write(str(balance))
    balanceInput.close()

