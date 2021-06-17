import math

def purchase():
    symbol = int(input("Symbol: "))
    lot_size = int(input("Shares in one lot:"))
    lots = int(input("Lots trading: "))
    pur_price = float(input("Purchase price: "))
    purcost = lot_size * pur_price * lots
    return purcost



def calhandlingfee(cost):
        brokeragefee = float(cost * 0.0025)
        if brokeragefee < 100:
            brokeragefee = 100
        if brokeragefee > 2500:
            brokeragefee = 2500

        stampduty = math.ceil(cost * 0.001)
        translevy = math.ceil(cost * 0.000027)
        hkexfee = math.ceil(cost * 0.00005)
        totalhandlfee = brokeragefee + stampduty + translevy + hkexfee

        print (f"Cost of purchase is : {cost}")
        print (f"Brokerage fee: {brokeragefee}")
        print (f"Stamp duty: {stampduty}")
        print (f"Transaction levy:{translevy}")
        print (f"Hkex fee: {hkexfee}")
        print (f"Total transaction fee: {totalhandlfee}")

cost1 = purchase()
calhandlingfee(cost1)
