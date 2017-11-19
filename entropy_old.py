from math import log2

file = open("/home/vlados/tic/books/uliss.txt", "r")
content = file.read()
file.close()

symbols_count = len(content)
pairs_count = symbols_count - 1
triplets_count = pairs_count - 1

symbols = {}

def initPairs(symbols):
    pairs = {}
    for key in symbols.keys():
        pairs[key] = {x : 0 for x in symbols.keys()}
    return pairs

def initTriplets(symbols):
    triplets = {}
    for key1 in symbols.keys():
        triplets[key1] = {}
        for key2 in symbols.keys():
            triplets[key1][key2] = {x : 0 for x in symbols.keys()}
    return triplets
            

for symbol in content:
    if symbol not in symbols.keys():
        symbols[symbol] = 1
    else:
        symbols[symbol] += 1

for key in symbols.keys():
    symbols[key] /= symbols_count

pairs = initPairs(symbols)

for i in range(0, len(content) - 1):
    pairs[content[i]][content[i + 1]] += 1

for key1, entry in pairs.items():
    for key2 in entry.keys():
        entry[key2] /= pairs_count

HA = 0
for value in symbols.values():
    HA -= value * log2(value)
print('H(A) = ' + str(HA))

HBA = 0
for key1, entry in pairs.items():
    pa1 = symbols[key1]
    HBa = 0
    for key2 in entry.keys():
        pba = pairs[key1][key2] / pa1
        if pba > 0:
            HBa -= pba * log2(pba)
    HBA += HBa * pa1
print('H(B|A) = ' + str(HBA))


triplets = initTriplets(symbols)

for i in range(0, triplets_count):
    triplets[content[i]][content[i + 1]][content[i + 2]] += 1

for key1, entry1 in triplets.items():
    for key2, entry2 in entry1.items():
        for key3 in entry2:
            entry2[key3] /= triplets_count

HCBA = 0
for key1, entry1 in triplets.items():
    for key2, entry2 in entry1.items():
        pab = pairs[key1][key2]
        if pab > 0:
            HCba = 0
            for key3 in entry2.keys():
                pcba = triplets[key1][key2][key3] / pab
                if pcba > 0:
                    HCba -= pcba * log2(pcba)
            HCBA += HCba * pab
        
print('H(C|AB) = ' + str(HCBA))
print('words = ' + str(symbols_count))
            
            
            


        
        
        