import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students,columns = ["student_id","name","age"])
    df = df.dropna()
    return df
    
