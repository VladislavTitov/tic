from huffman import HuffmanCoding
from huffman import HuffmanPairsCoding
import os
from collections import OrderedDict

name = "don"

path = "books/" + name + "/" + name + ".txt"

h = HuffmanCoding(path)
out = h.compress()
print(OrderedDict(sorted(h.codes.items())))
stat = os.stat(out)
print(stat.st_size * 8 / h.symbols_count)
h.decompress(out)

h1 = HuffmanPairsCoding(path)
out = h1.compress()
print(h1.codes)
stat = os.stat(out)
print(stat.st_size * 8 / h.symbols_count)
h1.decompress(out)
