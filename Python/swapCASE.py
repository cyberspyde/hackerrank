def swap_case(s):
    result = []

    for index, str in enumerate(s):
        if str.lower() == str:
            result.insert(index, str.upper())
        elif str.upper() == str:
            result.insert(index, str.lower())

    return ''.join(result)




print(swap_case("HackerRank.com presents 'Pythonist 2'."))