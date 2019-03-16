# Let's look at the lowercase letters.
import string
alphabet = ' ' + string.ascii_lowercase

positions = {' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
             'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
             'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
             }

message = "hi my name is caesar"

# encoded_message = ""
# keyList = list(positions.keys())
# valueList = list(positions.values())

# for m in message:
#     newPos = positions[m] + 1
#     encoded_message += keyList[valueList.index(newPos)]

def encoding(message, key):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
        encoded_string = "".join(encoding_list)

    return encoded_string


encoded_message = encoding(message, 3)
decoded_message = encoding(encoded_message, -3) #Just unshift the alphabets by -3 positions
print("Encoded: " + encoded_message + "\n" + "Decoded: " + decoded_message)
