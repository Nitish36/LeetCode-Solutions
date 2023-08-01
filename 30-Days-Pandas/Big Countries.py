import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    condition =  (world['area']>=3000000) | (world['population']>=25000000)
    df = world.loc[condition,['name','population','area']]
    
    return df
