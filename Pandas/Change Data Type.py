import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students,columns = ["student_id","name","age","grade"])
    df["grade"] = df["grade"].astype("int")
    return df
