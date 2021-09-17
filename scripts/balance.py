def READ():
    try:
        balanceFile = open("data/balance", "r")
    except:
        WRITE("balance", 0)
        balanceFile = open("data/balance", "r")
    balance = balanceFile.read()
    if balance == '':
        return (0,0)
    bal = []
    for item in balance.split('.'):
        bal.append(int(item))

    balanceFile.close()
    return bal

def WRITE(file, data, type = "w"):
    dataFile = open(("data/" + file), type)
    dataFile.write(str(data[0]) + '.' + str(data[1]))
    dataFile.close()

def BACNKRUPT(balance, cost):
    if balance[0] - cost[0] < 0 or (balance[0] == cost[0] and balance[1] - cost[1] < 0):
        return balance, True
    val = [balance[0] - cost[0], balance[1] - cost[1]]
    if val[1] < 0:
        val[0] -= 1
        val[1] = 1 + val[1]
    return (val[0], val[1]), False
