import seaborn as sns
import matplotlib.pyplot as plt

def generate_heatmap(df, target_column='sample'):
    """
    Plots a heatmap showing the compound intensities across samples.
    
    Parameters:
        df (DataFrame): DataFrame containing compound intensities with 'sample' and 'Group' columns.
        target_column (str): The column representing sample labels, default is 'sample'.
        group_column (str): The column representing sample groups, default is 'Group'.
    
    Returns:
        None: Displays the heatmap.
    """
    heatmap_df = df.drop(columns=[target_column]).set_index(df[target_column])
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_df.T, cmap="viridis", cbar_kws={'label': 'Intensity'}, annot=True, fmt=".2f")
    plt.xlabel('Samples')
    plt.ylabel('Compounds')
    plt.title('Heatmap of Compound Intensities Across Samples')
    plt.tight_layout()
    plt.show()

