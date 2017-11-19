from huffman import HuffmanCoding
from huffman import HuffmanPairsCoding
from shannon_fano import ShannonFanoCoding
from shannon_fano import ShannonFanoPairsCoding
import os
from collections import OrderedDict

name = "don"

path = "books/" + name + "/" + name + ".txt"

h = ShannonFanoCoding(path)
out = h.compress()
print(OrderedDict(sorted(h.reverse_mapping.items())))
stat = os.stat(out)
print(stat.st_size * 8 / h.symbols_count)
h.decompress(out)

h1 = ShannonFanoPairsCoding(path)
out = h1.compress()
print(h1.codes)
stat = os.stat(out)
print(stat.st_size * 8 / h.symbols_count)
h1.decompress(out)

