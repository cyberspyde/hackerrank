def minion_game(str):
    kevin_score = 0
    stuart_score = 0

    length = len(str)
    vowels = 'AEIOU'

    for i in range(length):
        substring_count = length - i
        if str[i] in vowels:
            kevin_score += substring_count
        else:
            stuart_score += substring_count

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")
minion_game("BANANA")