#Henry Maltby 2017

class PokerHand(object):

    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,\
     '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    hand_values = {}

    def __init__(self, cards):
        self.cards = cards
        self.mults = {}
        for card in self.cards:
            if card[0] not in self.mults:
                self.mults[card[0]] = 0
            self.mults[card[0]] += 1
        self.mult_dist = {}
        for key in self.mults:
            if self.mults[key] not in self.mult_dist:
                self.mult_dist[self.mults[key]] = 0
            self.mult_dist[self.mults[key]] += 1
        self.sort_hand()

    def sort_hand(self):
        val = {key: self.card_values[key] for key in self.card_values}
        for key in self.mults:
            val[key] += 13 * (self.mults[key] - 1)
        for i in range(len(self.cards)):
            for j in range(i):
                if val[self.cards[j][0]] < val[self.cards[i][0]]:
                    self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def rank_hand(self):
        rank = [self.card_values[self.cards[i][0]] for i in range(len(self.cards))]
        if self.is_straight_flush():
            return [9, rank[0]]
        elif self.is_four_of_a_kind():
            return [8, rank[0]]
        elif self.is_full_house():
            return [7, rank[0]]
        elif self.is_flush():
            return [6] + rank
        elif self.is_straight():
            return [5, rank[0]]
        elif self.is_three_of_a_kind():
            return [4, rank[0]]
        elif self.is_two_pair():
            return [3, rank[0], rank[2], rank[4]]
        elif self.is_pair():
            return [2, rank[0], rank[2], rank[3], rank[4]]
        return [1] + rank

    def is_straight_flush(self):
        return self.is_straight() and self.is_flush()

    def is_four_of_a_kind(self):
        return self.mult_dist == {4: 1, 1: 1}

    def is_full_house(self):
        return self.mult_dist == {3: 1, 2: 1}

    def is_flush(self):
        suit = self.cards[0][1]
        for card in self.cards[1:]:
            if card[1] != suit:
                return False
        return True

    def is_straight(self):
        vals = set()
        for card in self.cards:
            vals.add(card[0])
        straights = [{'A', '2', '3', '4', '5'}, {'2', '3', '4', '5', '6'}, {'3',\
         '4', '5', '6', '7'}, {'4', '5', '6', '7', '8'}, {'5', '6', '7', '8',\
         '9'}, {'6', '7', '8', '9', 'T'}, {'7', '8', '9', 'T', 'J'}, {'8', '9',\
         'T', 'J', 'Q'}, {'9', 'T', 'J', 'Q', 'K'}, {'T', 'J', 'Q', 'K', 'A'}]
        if vals in straights:
            return True
        return False

    def is_three_of_a_kind(self):
        return self.mult_dist == {3: 1, 1: 2}

    def is_two_pair(self):
        return self.mult_dist == {2: 2, 1: 1}

    def is_pair(self):
        return self.mult_dist == {2: 1, 1: 3}


def compare_hands(player1, player2):
    rank1 = player1.rank_hand()
    rank2 = player2.rank_hand()
    l = min(len(rank1), len(rank2))
    for i in range(l):
        if rank1[i] > rank2[i]:
            return 1
        elif rank1[i] < rank2[i]:
            return 2
    return -1

def poker_hands(games):
    total = 0
    for game in games:
        player1 = PokerHand(game[:5])
        player2 = PokerHand(game[5:])
        if compare_hands(player1, player2) == 1:
            total += 1
    return total

f = open("problem_54_poker.txt")
print(poker_hands([line.split(' ') for line in f.read().strip().split('\n')]))