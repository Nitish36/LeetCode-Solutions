import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(products, columns=["name","quantity","price"])
    df["quantity"].fillna(0,inplace=True)
    return df
    
