import pandas as pd
from scipy.stats import ttest_ind

def calculate_p_values(df):
    """
    Calculates p-values for each compound between overexpressed (oe) and wild-type (wt) samples.

    Parameters:
    df (pd.DataFrame): A DataFrame with a 'sample' column identifying 'oe' and 'wt' samples
                       and additional columns for compound values.

    Returns:
    pd.DataFrame: A DataFrame with compounds and their corresponding p-values.
    """
    oe_rows = df[df['sample'].str.startswith('oe')]
    wt_rows = df[df['sample'].str.startswith('wt')]
    
    p_values = {}

    for compound in df.columns[1:]:
        oe_values = oe_rows[compound].values
        wt_values = wt_rows[compound].values
        
        t_stat, p_val = ttest_ind(oe_values, wt_values, equal_var=False)
        
        p_values[compound] = p_val

    p_values_df = pd.DataFrame(list(p_values.items()), columns=['Compound', 'p-value'])
    
    return p_values_df
