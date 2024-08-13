def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            shifted_index = (index + key) % 26
            result += alphabet[shifted_index] if char.islower() else alphabet[shifted_index].upper()
        else:
            result += char

    return result