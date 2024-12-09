def birthdayCakeCandles(candles):
    occ = 0
    max_number = max(candles)
    for i in candles:
        if i == max_number:
            occ += 1

    return occ


candles = [4, 6, 2, 6, 4, 6]
birthdayCakeCandles(candles)