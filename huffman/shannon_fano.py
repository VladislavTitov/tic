import heapq
import os
from entropy import Entropy
from huffman import HuffmanCoding
from huffman import HeapNode
from huffman import untrim


class ShannonFanoCoding(HuffmanCoding):
    def merge_nodes(self):
        ordered = []
        while self.heap:
            ordered.append(heapq.heappop(self.heap))
        # ordered.reverse()

        root = HeapNode(None, 0)
        self.make_tree(root, ordered)
        heapq.heappush(self.heap, root)

    def make_tree(self, root, ordered_nodes):
        if len(ordered_nodes) == 1:
            root.left = ordered_nodes[0]
            return
        if len(ordered_nodes) == 2:
            root.left = ordered_nodes[0]
            root.right = ordered_nodes[1]
            return

        n = 0
        for i in ordered_nodes:
            n += i.freq
        x = 0
        distance = abs(2 * x - n)
        j = 0
        for i in range(len(ordered_nodes)):
            x += ordered_nodes[i].freq
            if (2 * x - n) >= 0:
                j = i
                break
        root.left = HeapNode(None, 0)
        root.right = HeapNode(None, 0)
        self.make_tree(root.left, ordered_nodes[:j + 1])
        self.make_tree(root.right, ordered_nodes[j + 1:])


class ShannonFanoPairsCoding(ShannonFanoCoding):
    def __init__(self, path):
        super().__init__(path)
        untrim(path)

    def make_frequency_dict(self, text):
        ent = Entropy(self.path)
        ent.HBA()
        return ent.pairs

    def make_heap(self, frequency):
        for key, entry in frequency.items():
            for key1 in entry:
                if frequency[key][key1] > 0:
                    node = HeapNode(key + key1, frequency[key][key1])
                    heapq.heappush(self.heap, node)

    def get_encoded_text(self, text):
        encoded_text = ""
        for i in range(0, len(text), 2):
            encoded_text += self.codes[text[i] + text[i + 1]]
        return encoded_text

    def output_decompressed_path(self, path):
        filename, file_extension = os.path.splitext(path)
        output_path = filename + "_decompressed_pairs" + ".txt"
        return output_path

    def output_compressed_path(self, path):
        filename, file_extension = os.path.splitext(path)
        return filename + "_pairs" + ".bin"
