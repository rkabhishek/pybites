def remove_punctuation(input_string):
    punctuation_string = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    result = ""
    for ch in input_string:
        if ch not in punctuation_string:
            result += ch

    return result

