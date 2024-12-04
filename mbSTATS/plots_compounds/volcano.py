import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 

def plot_volcano(
    p_values_df, 
    code_to_compound, 
    output, 
    p_value_col='p-value', 
    compound_col='Compound', 
    fc_threshold=1, 
    p_value_threshold=0.1, 
    text_size=7
):
    """
    Plots a volcano plot for the given p-values DataFrame with compound names displayed.

    Parameters:
    p_values_df (pd.DataFrame): DataFrame containing 'Compound' and 'p-value' columns.
    code_to_compound (dict): Dictionary mapping compound codes to compound names.
    output (str): Directory path to save the output plot.
    p_value_col (str): Name of the column containing p-values. Default is 'p-value'.
    compound_col (str): Name of the column containing compound codes. Default is 'Compound'.
    fc_threshold (float): Fold change threshold for significance. Default is 1.
    p_value_threshold (float): P-value threshold for significance. Default is 0.1.
    text_size (int): Font size for compound names in the plot. Default is 10.
    """
    # Calculate -log10(p-value)
    p_values_df['-log10(p-value)'] = -np.log10(p_values_df[p_value_col])

    # Identify significantly changed compounds based on thresholds
    p_values_df['Significance'] = 'Not Significant'
    p_values_df.loc[(p_values_df[p_value_col] < p_value_threshold), 'Significance'] = 'Significant'

    # Map compound codes to names
    p_values_df['Compound_Name'] = p_values_df[compound_col].map(code_to_compound)

    # Plotting
    plt.figure(figsize=(12, 8))
    # Non-significant points
    non_significant = p_values_df[p_values_df['Significance'] == 'Not Significant']
    plt.scatter(
        non_significant['Compound_Name'], 
        non_significant['-log10(p-value)'], 
        c='gray', label='Not Significant', alpha=0.7
    )
    # Significant points
    significant = p_values_df[p_values_df['Significance'] == 'Significant']
    plt.scatter(
        significant['Compound_Name'], 
        significant['-log10(p-value)'], 
        c='red', label='Significant', alpha=0.7
    )

    # Plot formatting
    plt.axhline(-np.log10(p_value_threshold), color='blue', linestyle='--', label=f'p-value threshold = {p_value_threshold}')
    plt.xticks(rotation=90, fontsize=text_size)
    plt.xlabel('Compounds', fontsize=text_size + 2)
    plt.ylabel('-log10(p-value)', fontsize=text_size + 2)
    plt.title('Volcano Plot', fontsize=text_size + 4)
    plt.legend(fontsize=text_size)
    plt.tight_layout()
    
    # Save the plot
    output_file = os.path.join(output, "volcano_plot.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")

