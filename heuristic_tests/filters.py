from firms import Firm
import itertools as its
import pandas as pd

def create_combos(firms: [Firm], trades_df: pd.DataFrame, possibilities:int = 10, approx: int = 0):
    """Create the combo trades

    Args:
        firms (Firm]): Firm object without any trade combos yet
    """
    combs = []
    for firm in firms:
        combo = firm.gen_combos(trades_df, possibilities, approx)
        combs.append(combo)
    # return combs

def filter_combos(firms: [Firm]):
    """Filters 'impossible' combinations of trades from the list of firms

    Args:
        firms (Firm]): Firm object with possible trades already
    """
    
    trade_combos = [firm.possibilities for firm in firms]
    for combo in its.product(*trade_combos):
        if not flag_trades(combo):
            yield combo

def flag_trades(combos):
    seen = set()
    for inner_tuple in combos:
        for num in inner_tuple:
            if num in seen:
                return True  # Found a repeated integer
            seen.add(num)
    return False  # No repetitions found

# create combos conditionally
# takes in firms, condition from left to right
# take the first firm and iterate through the possibilities, but block off the trades that are already made
# then take the second firm and iterate through the possibilities, but block off the trades that are already made
# continue until you find a firm that is still possible


# subset sum variation
# reformat the data into "integers" but keep track of how many trades of the same size
# then see if you can make a combination of trades that add up to the shares of a given firm
# reuse the list
# if not possible, go back up the "tree" 