<<<<<<< HEAD
def test():
    Balance = open('data')
=======
def READ():
    dataFile = open("data/balance", 'r')
    balance = float(dataFile.read())
    dataFile.close()
    return balance

def DUMP(balance):
    return balance
>>>>>>> b9dd1e0c4bf8db3e445741e1fd34784fc60067a4
