from math import log2

file = open("/home/vlados/Загрузки/Telegram Desktop/idiot", "r")
content = file.read()
file.close()

symbols_count = len(content)
pairs_count = symbols_count - 1

symbols = {}

def initPairs(symbols):
    pairs = {}
    for key in symbols.keys():
        pairs[key] = {x : 0 for x in symbols.keys()}
    return pairs

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
        else:
            HBa -= 0
    HBA += HBa * pa1
print('H(B|A) = ' + str(HBA))
print('words = ' + str(symbols_count))
        
        
        