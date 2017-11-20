#Henry Maltby 2017
import numpy

def generate_probabilities(square, doubles, side, just_landed=False):
    """
    Returns a dictionary containing the probability of each potential
    state (square value, number of consecutive doubles rolled).
    """
    dice_rolls = [0] + [(side - abs(side + 1 - i)) / (side * side) for i in range(1, 2 * side + 1)]
    comm_chest = {(10, 0): 1/16, (0, doubles): 1/16, (square, doubles): 14/16}
    c1, c2, c3 = [1, 0, 0, 0, 1, 1, 0, 6, 0, 0, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 6, 0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1 + 1 / 16, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1 + 1 / 16, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 14 / 16, 0, 0, 6, 0, 0, 1]
    chance1, chance2, chance3 = {}, {}, {}
    for i in range(40):
        if c1[i] != 0:
            chance1[(i, doubles if i != 10 else 0)] = 1 / 16 * c1[i]
        if c2[i] != 0:
            chance2[(i, doubles if i != 10 else 0)] = 1 / 16 * c2[i]
        if c3[i] != 0:
            chance3[(i, doubles if i != 10 else 0)] = 1 / 16 * c3[i]
    go_to_jail = {(10, 0): 1}
    special_squares = {7: chance1, 22: chance2, 36: chance3, 2: comm_chest, 17: comm_chest, 33: comm_chest, 30: go_to_jail}
    if doubles == 3:
        return go_to_jail
    if just_landed and square in special_squares:
        return special_squares[square]
        ans = {}
        for state in special_squares[square]:
            end_locs = generate_probabilities(state[0], state[1], side, True)
            for state2 in end_locs:
                if state2 not in ans:
                    ans[state2] = 0
                ans[state2] += special_squares[square][state] * end_locs[state2]
        return ans
    if just_landed and square not in special_squares:
        return {(square, doubles): 1}
    ans = {}
    for i in range(len(dice_rolls)):
        if dice_rolls[i] != 0:
            new_square = (square + i) % 40
            prob = dice_rolls[i]
            if i % 2 == 0:
                prob2 = 1 / (side * side)
                prob -= prob2
                end_locs = generate_probabilities(new_square, doubles + 1, side, True)
                for state in end_locs:
                    if state not in ans:
                        ans[state] = 0
                    ans[state] += prob2 * end_locs[state]
            end_locs = generate_probabilities(new_square, 0, side, True)
            for state in end_locs:
                if state not in ans:
                    ans[state] = 0
                ans[state] += prob * end_locs[state]
    return ans

def populate_monopoly_matrix(k):
    """
    Returns a probability matrix for 120 states in the game Monopoly,
    given two dice with k sides. States 0-40 refer to the first forty
    squares and no immediately previous double rolls; 40-80 refer to
    the next forty squares and 1 immediately previous double roll; and
    80-120 refer to the final forty squares and 2 immediately previous
    double rolls.
    """
    probs = [[0] * 120 for i in range(120)]
    for i in range(120):
        doubles, x = divmod(i, 40)
        sent_to = generate_probabilities(x, doubles, k)
        for state in sent_to:
            j = state[1] * 40 + state[0]
            probs[j][i] = sent_to[state]
    M = numpy.array(probs)
    D, V = numpy.linalg.eig(M)
    stable_state = V[:,0]
    ans = [0] * 40
    total = 0
    for i in range(120):
        ans[i % 40] += stable_state[i].real
        total += stable_state[i].real
    total2 = 0
    for i in range(40):
        ans[i] /= total
        total2 += ans[i]
    ans2 = sorted(ans)[::-1]
    final_ans = ""
    for x in range(3):
        final_ans += str(ans.index(ans2[x]))
    return final_ans

print(populate_monopoly_matrix(4))