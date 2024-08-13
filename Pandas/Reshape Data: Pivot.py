import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(weather,columns=["city","month","temperature"])
    new_df = df.pivot_table(index = 'month', columns = 'city',values= 'temperature',aggfunc='max')
    return new_df
