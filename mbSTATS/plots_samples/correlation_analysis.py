import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 

def plot_correlation_matrix_compounds(data, code_to_compound, output):
    """
    Plot the correlation matrix of the given data with compound names as labels.
    
    Parameters:
    data (pd.DataFrame): DataFrame with the first column as sample names and
                         the remaining columns as features (compound codes).
    code_to_compound (dict): Dictionary mapping compound codes to compound names.
    output (str): Directory path to save the output plot.
                         
    Returns:
    pd.DataFrame: Correlation matrix of the features with renamed indices and columns.
    """
    
    features = data.iloc[:, 1:]
    correlation_matrix = features.corr()
    correlation_matrix.rename(index=code_to_compound, columns=code_to_compound, inplace=True)
   
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True, cbar_kws={'shrink': 0.6})
    plt.title("Correlation Matrix (with Compound Names)")
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    output_file = os.path.join(output, "correlation_compounds.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")
    
    return correlation_matrix
