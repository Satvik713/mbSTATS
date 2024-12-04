import seaborn as sns
import matplotlib.pyplot as plt
import os 

def plot_correlation_matrix(df, output):
    """
    This function computes and plots the correlation matrix of the provided DataFrame.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing compounds as rows and samples as columns.
    """
    # Drop 'Compounds' column for correlation calculation
    df_numeric = df.drop(columns=['Compounds'])
    correlation_matrix = df_numeric.corr()

    # Plot the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True)
    plt.title("Correlation Matrix")
    output_file = os.path.join(output, "correlation_samples.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")
    # plt.show()
    
    return correlation_matrix
