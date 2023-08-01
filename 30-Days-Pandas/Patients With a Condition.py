import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    condition = patients['conditions'].str.contains('DIAB1')
    df = patients.loc[condition,['patient_id','patient_name','conditions']]

    return df
