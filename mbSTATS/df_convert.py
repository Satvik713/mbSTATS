import pandas as pd

def convert(df):
    """
    This function melts and pivots a DataFrame. It assumes the DataFrame has a column 'sample' and compound columns.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing sample and compound data.
    
    Returns:
    pd.DataFrame: A DataFrame that has been melted and then pivoted.
    """
    df_melted = df.melt(id_vars='sample', var_name='Compounds', value_name='Intensity')
    
    df_pivoted = df_melted.pivot(index='Compounds', columns='sample', values='Intensity').reset_index()
    
    return df_pivoted

