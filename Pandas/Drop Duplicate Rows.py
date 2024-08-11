import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(customers,columns = ["customer_id","name","email"])
    df = df.drop_duplicates('email')
    return df
    
