#Write a Python program to perform Huffman Coding for a given string. Print the encoded string and decode it back to the original string.


import heapq  #solution
from collections import defaultdict, Counter

# Node class for Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(freq_map):
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Generate Huffman Codes
def generate_codes(node, current_code, huffman_codes):
    if node is None:
        return
    if node.char is not None:
        huffman_codes[node.char] = current_code
    generate_codes(node.left, current_code + "0", huffman_codes)
    generate_codes(node.right, current_code + "1", huffman_codes)

# Encode the input string
def huffman_encode(input_string, huffman_codes):
    return ''.join(huffman_codes[char] for char in input_string)

# Decode the encoded string
def huffman_decode(encoded_string, root):
    decoded_string = []
    current_node = root
    for bit in encoded_string:
        current_node = current_node.left if bit == "0" else current_node.right
        if current_node.char is not None:
            decoded_string.append(current_node.char)
            current_node = root
    return ''.join(decoded_string)

# Example usage
input_string = "huffman coding is fun"
freq_map = Counter(input_string)
huffman_tree_root = build_huffman_tree(freq_map)

huffman_codes = {}
generate_codes(huffman_tree_root, "", huffman_codes)

encoded_string = huffman_encode(input_string, huffman_codes)
decoded_string = huffman_decode(encoded_string, huffman_tree_root)

print("Original String:", input_string)
print("Character Frequencies:", freq_map)
print("Huffman Codes:", huffman_codes)
print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
