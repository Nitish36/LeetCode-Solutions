import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students,columns = ["id","first","last","age"])
    df.rename(columns = {"id":"student_id","first":"first_name","last":"last_name","age":"age_in_years"}, inplace = True)
    return df
    
