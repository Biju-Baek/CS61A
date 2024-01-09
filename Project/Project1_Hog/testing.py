import dice
import hog

def sus_update(num_rolls, player_score, opponent_score, dice=dice.six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    new_score = hog.simple_update(num_rolls, player_score, opponent_score, dice)
    factors_count = hog.num_factors(new_score)
    if factors_count == 3 or factors_count == 4: 
        return hog.sus_point(new_score)
    else:
        return new_score

print(sus_update(2,5,7,dice.make_test_dice(2,4)))