from trade_generators import possible_trades
from dataclasses import dataclass
import pandas as pd
import itertools as its

@dataclass
class Combo:
    trades: tuple
    size: int
    shares: int

class Firm:
    def __init__(self, name: str, orders:int = 0, shares:int = 0, **kwargs) -> None:
        self.name = name
        self.orders = orders
        self.shares = shares
        self.possibilities = []
        
    def gen_combos(self, trades_df: pd.DataFrame ,possibilities:int = 10, approx: int = 0):
        
        for combo in list(its.islice(possible_trades(trades_df, self.orders, self.shares, approx), possibilities)):
            trades, shares = combo
            self.possibilities.append(Combo(trades, len(trades), shares))
        
        return self.possibilities