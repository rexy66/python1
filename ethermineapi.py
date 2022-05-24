import requests 
import time

ming = 'https://api.ethermine.org/miner/0xee6353c15412C6aB825Ef91c85E7aa904802dC/currentStats'
canus = 'https://api.ethermine.org/miner/0x4b12d3a324088A37F5C48467f74c5121106D12/currentStats'
mingdefault=3
canusdefault =3
diff= False
displayed = False

def checkworkers(link):
    req = requests.get(link)
    result = req.text
    result = result.replace("{","")
    result = result.replace("}","")
    result = result.replace("\"","")
    result = result.replace(":",",")
    result = list(result.split(","))
    index = result.index("activeWorkers")
    end_index = index + 1
    end_result = result[end_index]
    return end_result

def checkdiff(user,default):
    if checkworkers(user) != default:
        diff = True
        diff = True
        displayed = False
    else:
        diff = False
        displayed = True


print('Running...')

while True:
    checkdiff(ming,mingdefault)
    checkdiff(canus,canusdefault)
    time.sleep(10)
    if diff and not displayed:
        displayed = True
        print("The number of workers for Ming is now: " + str(checkworkers(ming)))
        print("The number of workers for Canus is now: " + str(checkworkers(canus)))
        
    else:
        displayed = True
