import urllib.request

def readNames():
    boysRanking = {}
    girlsRanking = {}
    
    for i in range(0, 10):
        if i == 9:
            filename = "babynamesranking2010.txt"
        else:
            filename = "babynamesranking200" + str(i + 1) + ".txt"

        input = urllib.request.urlopen(
            "https://liveexample.pearsoncmg.com/data/" + filename)
        for line in input:
            items = line.split()
            if items[1].decode() in boysRanking:
                boysRanking[items[1].decode()] += int(items[2].decode())
            else:
                boysRanking[items[1].decode()] = int(items[2].decode())
                
            if items[3].decode() in girlsRanking:
                girlsRanking[items[3].decode()] += int(items[4].decode())
            else:
                girlsRanking[items[3].decode()] = int(items[4].decode())
        
    return boysRanking, girlsRanking
      
def main():
    boysRanking, girlsRanking = readNames()
    lstBoysRanking = [[x, y] for (y, x) in list(boysRanking.items())]
    lstBoysRanking.sort()
    print("Boys rankings")
    for e in lstBoysRanking:
        print(format(e[1], "20s"), e[0])
        
    lstGirlsRanking = [[x, y] for (y, x) in list(girlsRanking.items())]
    lstGirlsRanking.sort()
    print("Girls rankings")
    for e in lstGirlsRanking:
        print(format(e[1], "20s"), e[0])    
        
main()