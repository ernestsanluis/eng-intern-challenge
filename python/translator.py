english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '..OO.O', ',': 'O.....', '?': '..O.OO', '!': '..OO.O', ':': 'OO....',
    ';': 'O.O...', '-': '....O.', '/': '.O..O.', '(': '.O.O..', ')': '.O.O..',
    '<': 'O..OOO', '>': 'O.OOO.', '"': 'O.OO..', '\'': 'O.....', '_': '....O.', 
    '@': 'O.O...', '&': 'O.OO..', '#': '.O..O.', '$': '.OO.OO'
}

capital_indicator = '.....O'
number_indicator = '.O.OOO'

braille_to_english = {v: k for k, v in english_to_braille.items()}

def is_braille(text):
    return all(c in 'O.' for c in text)

def translate_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char == ' ':
            result.append(english_to_braille[' '])
            is_number = False
        elif char.isdigit():
            if not is_number:
                result.append(number_indicator)
                is_number = True
            result.append(english_to_braille[char])
        elif char.isupper():
            result.append(capital_indicator)
            result.append(english_to_braille[char.lower()])
        elif char in english_to_braille:
            result.append(english_to_braille[char])
        else:
            result.append('')
    return ''.join(result)

def translate_to_english(braille):
    result = []
    is_capital = False
    is_number = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == capital_indicator:
            is_capital = True
            i += 6
        elif symbol == number_indicator:
            is_number = True
            i += 6
        else:
            char = braille_to_english.get(symbol, '')
            if is_number:
                result.append(char)
                if char == ' ':
                    is_number = False
            elif is_capital:
                result.append(char.upper())
                is_capital = False
            else:
                result.append(char)
            i += 6
    return ''.join(result)

def translate(text):
    if is_braille(text):
        return translate_to_english(text)
    else:
        return translate_to_braille(text)

if __name__ == "__main__":
    import sys
    input_text = ' '.join(sys.argv[1:])
    print(translate(input_text))
