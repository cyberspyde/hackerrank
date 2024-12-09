def compareTriplets(a, b):
    # Write your code here
    mixed = a + b
    alice = 0
    bob = 0
    for index, number in enumerate(mixed):
        if index == 3:
            if number > mixed[index - 3]:
                bob += 1
            elif number < mixed[index - 3]:
                alice += 1
        elif index == 4:
            if number > mixed[index - 3]:
                bob += 1
            elif number < mixed[index - 3]:
                alice += 1
        elif index == 5:
            if number > mixed[index - 3]:
                bob += 1
            elif number < mixed[index - 3]:
                alice += 1

    print([alice, bob])

compareTriplets([3, 6, 7], [3, 6, 10])