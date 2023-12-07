import math

inputFile = "inputs/input7.txt"

#part 1
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
hands = []

def compare_hands(hand1, hand2):
    cards1, cards2 = [hand1.count(x) for x in cards], [hand2.count(x) for x in cards]
    max1, max2 = max(cards1), max(cards2)
    #bigger x of a kind
    if max1 > max2:
        return 1
    elif max1 < max2:
        return -1
    #full house vs 3 of a kind
    if max1 == 3:
        if (2 in cards1) and not (2 in cards2):
            return 1
        if not (2 in cards1) and (2 in cards2):
            return -1
    #two pair vs pair
    if max1 == 2:
        pairs1 = len([x for x in cards1 if x == 2])
        pairs2 = len([x for x in cards2 if x == 2])
        if pairs1 > pairs2:
            return 1
        if pairs1 < pairs2:
            return -1
    #look at high cards in order
    for (card1, card2) in zip(hand1, hand2):
        for card in cards:
            if card1 == card and card2 != card:
                return 1
            elif card1 != card and card2 == card:
                return -1
    return 0

def find_strength(hand, low, high):
    middle = math.floor((low + high) / 2)
    comparison = compare_hands(hand, hands[middle][0])
    
    #last comparison
    if low + 1 == high:
        if comparison == 1:
            return middle + 1
        else:
            return middle
    #hand is stronger (search in the stronger half)
    elif comparison == 1:
        return find_strength(hand, middle, high)
    #hand is weaker (search in the weaker half)
    elif comparison == -1:
        return find_strength(hand, low, middle)
    #same stregnth
    else:
        return middle


def place_hand(hand, bid):
    global hands
    index = find_strength(hand, 0, len(hands))
    hands.insert(index, (hand, bid))

total = 0
with open(inputFile, "r") as file:
    for line in file.readlines():
        hand, bid = line.strip().split(" ")
        if hands == []:
            hands.append((list(hand), int(bid)))
        else:
            place_hand(list(hand), int(bid))
    
    for i, hand in enumerate(hands):
        rank = i + 1
        total += rank * hand[1]


print("Part 1:", total)


#part 2
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hands = []

def compare_hands(hand1, hand2):
    jokers1, jokers2 = hand1.count("J"), hand2.count("J")
    cards1, cards2 = [hand1.count(x) for x in cards[:-1]], [hand2.count(x) for x in cards[:-1]]
    max1, max2 = max(cards1) + jokers1, max(cards2) + jokers2
    #bigger x of a kind
    if max1 > max2:
        return 1
    elif max1 < max2:
        return -1
    #full house vs 3 of a kind
    if max1 == 3:
        isFullHouse1 = sum([x for x in cards1 if x == 2 or x == 3]) + jokers1 == 5
        isFullHouse2 = sum([x for x in cards2 if x == 2 or x == 3]) + jokers2 == 5
        if isFullHouse1 and not isFullHouse2:
            return 1
        if not isFullHouse1 and isFullHouse2:
            return -1
    #two pair vs pair
    if max1 == 2:
        pairs1 = len([x for x in cards1 if x == 2]) + jokers1
        pairs2 = len([x for x in cards2 if x == 2]) + jokers2
        if pairs1 > pairs2:
            return 1
        if pairs1 < pairs2:
            return -1
    #look at high cards in order
    for (card1, card2) in zip(hand1, hand2):
        for card in cards:
            if card1 == card and card2 != card:
                return 1
            elif card1 != card and card2 == card:
                return -1
    return 0

total = 0
with open(inputFile, "r") as file:
    for line in file.readlines():
        hand, bid = line.strip().split(" ")
        if hands == []:
            hands.append((list(hand), int(bid)))
        else:
            place_hand(list(hand), int(bid))
    
    for i, hand in enumerate(hands):
        rank = i + 1
        total += rank * hand[1]

print("Part 2:", total)