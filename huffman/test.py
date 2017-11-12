from huffman import HuffmanCoding
from huffman import HuffmanPairsCoding

name = "uliss"

path = "books/" + name + "/" + name + ".txt"

h = HuffmanCoding(path)
out = h.compress()
h.decompress(out)

h1 = HuffmanPairsCoding(path)
out = h1.compress()
h1.decompress(out)
