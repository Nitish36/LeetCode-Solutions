import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    d1 = pd.DataFrame(df1,columns = ["student_id","name","age"])
    d2 = pd.DataFrame(df2,columns = ["student_id","name","age"])
    new_df = pd.concat([d1,d2])
    return new_df    
