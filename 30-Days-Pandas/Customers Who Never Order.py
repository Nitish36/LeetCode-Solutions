import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders,how = 'left',left_on = 'id',right_on = 'customerId')
    customers_never_ordered = merged[merged['customerId'].isnull()]
    customers_never_ordered.rename({'name':'Customers'},axis = 1,inplace = True)

    return customers_never_ordered[['Customers']]
