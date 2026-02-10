def remove_punctuation(input_string):
    punctuation_string = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    non_punctuation_char_list = []

    for ch in input_string:
        if ch not in punctuation_string:
            non_punctuation_char_list.append(ch)
    return ''.join(non_punctuation_char_list)



