import sys

BRAILLE_SYMBOLS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

CAPITAL_MARKER = '.....O'

def isBraille(s):
    return all(c in 'O. ' for c in s)

def englishToBraille(text):
    braille = []
    for char in text:
        if char.isupper():
            braille.append(CAPITAL_MARKER)
            char = char.lower()
        braille.append(BRAILLE_SYMBOLS.get(char, '......'))  
    return ''.join(braille)

input_text = sys.argv[1]
if len(sys.argv) > 1:
    if isBraille(sys.argv[1]):
        print(englishToBraille(sys.argv[1])
    else:
        print("invalid input. Please try again")

else:
    print("error: no string provided. Please try again.")

