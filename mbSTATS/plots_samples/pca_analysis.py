import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

def perform_pca(data, output):
    """
    Perform PCA on the given data and plot the results with sample labels.
    
    Parameters:
    data (pd.DataFrame): DataFrame with the first column as sample names and
                         the remaining columns as features.
                         
    Returns:
    pd.DataFrame: DataFrame containing the PCA components.
    """
    features = data.iloc[:, 1:].values
    samples = data.iloc[:, 0].values
    scaler = StandardScaler()
    features_std = scaler.fit_transform(features)
    pca = PCA(n_components=2) 
    pca_components = pca.fit_transform(features_std)
    pca_df = pd.DataFrame(data=pca_components, columns=['PC1', 'PC2'])
    pca_df['sample'] = samples
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='PC1', y='PC2', hue='sample', data=pca_df, palette="viridis", s=100)
    
    for i, sample in enumerate(pca_df['sample']):
        plt.text(pca_df['PC1'][i], pca_df['PC2'][i], sample, fontsize=9, ha='right')
        
    plt.title("PCA of Samples")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend(title="Sample Type", bbox_to_anchor=(1, 1))
    output_file = os.path.join(output, "pca_samples.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")
    # plt.show()
    
    return pca_df
