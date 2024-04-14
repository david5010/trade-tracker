import itertools as its
import pandas as pd

def possible_trades(trades_df: pd.DataFrame, orders: int, shares: int, approx: int = 0):
    """Yields the possible trades given the trades dataframe, orders, shares, and approx

    Args:
        trades_df (pd.DataFrame): pd.DataFrame of trades, containing only the size column
        orders (int): Integer representing the number of orders a firm has made
        shares (int): Total sum of shares
        approx (int, optional): If there are no exact matches, approx will allow ±approx of the total. Defaults to 0.
    """
    for combo in its.combinations(trades_df.iterrows(), orders):
        combo_ids, combo_sizes = zip(*[(index, row.SIZE) for index, row in combo])
        if sum(combo_sizes) + approx >= shares >= sum(combo_sizes) - approx:
            yield combo_ids, sum(combo_sizes)