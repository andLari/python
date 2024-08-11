def is_pangram(sentence):
    lower_case_sentence = sentence.lower()
    alphabet_string = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet_string:
        if letter not in lower_case_sentence:
            return False
    
    return True
