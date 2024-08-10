import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students,columns = ["student_id","name","age"])
    selected_columns = df.loc[df['student_id'] == 101, ['name', 'age']]
    return selected_columns
