from math import log2


class Entropy:
    def __init__(self, path):
        file = open(path, "r")
        self.content = file.read()
        file.close()

        self.symbols_count = len(self.content)
        self.pairs_count = self.symbols_count - 1
        self.triplets_count = self.pairs_count - 1

        self.symbols = {}

        for symbol in self.content:
            if symbol not in self.symbols.keys():
                self.symbols[symbol] = 1
            else:
                self.symbols[symbol] += 1

        self.freq = self.symbols

        for key in self.symbols.keys():
            self.symbols[key] /= self.symbols_count

    def init_pairs(self, symbols):
        pairs = {}
        for key in symbols.keys():
            pairs[key] = {x: 0 for x in symbols.keys()}
        return pairs

    def init_triplets(self, symbols):
        triplets = {}
        for key1 in symbols.keys():
            triplets[key1] = {}
            for key2 in symbols.keys():
                triplets[key1][key2] = {x: 0 for x in symbols.keys()}
        return triplets

    def HBA(self):
        content = self.content
        symbols = self.symbols
        symbols_count = self.symbols_count
        pairs_count = self.pairs_count

        self.pairs = self.init_pairs(symbols)

        for i in range(0, len(content) - 1):
            self.pairs[content[i]][content[i + 1]] += 1

        for key1, entry in self.pairs.items():
            for key2 in entry.keys():
                entry[key2] /= pairs_count

        HA = 0
        for value in symbols.values():
            HA -= value * log2(value)
        print('H(A) = ' + str(HA))

        HBA = 0
        for key1, entry in self.pairs.items():
            pa1 = symbols[key1]
            HBa = 0
            for key2 in entry.keys():
                pba = self.pairs[key1][key2] / pa1
                if pba > 0:
                    HBa -= pba * log2(pba)
            HBA += HBa * pa1
        print('H(B|A) = ' + str(HBA))
        return HBA

    def HCBA(self):
        content = self.content
        symbols = self.symbols
        symbols_count = self.symbols_count
        triplets_count = self.triplets_count

        triplets = self.init_triplets(symbols)

        for i in range(0, triplets_count):
            triplets[content[i]][content[i + 1]][content[i + 2]] += 1

        for key1, entry1 in triplets.items():
            for key2, entry2 in entry1.items():
                for key3 in entry2:
                    entry2[key3] /= triplets_count

        HCBA = 0
        for key1, entry1 in triplets.items():
            for key2, entry2 in entry1.items():
                pab = self.pairs[key1][key2]
                if pab > 0:
                    HCba = 0
                    for key3 in entry2.keys():
                        pcba = triplets[key1][key2][key3] / pab
                        if pcba > 0:
                            HCba -= pcba * log2(pcba)
                    HCBA += HCba * pab

        print('H(C|AB) = ' + str(HCBA))
        print('words = ' + str(symbols_count))
        return HCBA
