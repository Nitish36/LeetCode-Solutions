import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    condition = views['author_id'] == views['viewer_id']
    df = views.loc[condition,['author_id']]
    df.rename(columns = {'author_id':'id'},inplace = True)
    unique_ids_df = df.drop_duplicates()
    return unique_ids_df.sort_values(by = ['id'])
