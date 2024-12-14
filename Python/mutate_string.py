def mutate_string(string, position, character):
    result = list(string)
    result[position] = character
    return ''.join(result)