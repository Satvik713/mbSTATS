import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import os 

def plot_pca(df, code_to_compound, output):
    """
    This function performs PCA on the provided DataFrame and plots the results with compound names.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing compounds as rows and samples as columns.
    code_to_compound (dict): A dictionary mapping compound codes to compound names.
    """
    X = df.drop(columns=['Compounds'])
    X_std = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2)
    pca_components = pca.fit_transform(X_std)
    pca_df = pd.DataFrame(pca_components, columns=['PC1', 'PC2'])
    pca_df['Compound'] = df['Compounds']
    pca_df['Compound_Name'] = pca_df['Compound'].map(code_to_compound)
    plt.figure(figsize=(10, 8))
    plt.scatter(pca_df['PC1'], pca_df['PC2'], color='b', s=100)

    for i in range(pca_df.shape[0]):
        plt.text(pca_df['PC1'][i] + 0.05, pca_df['PC2'][i], pca_df['Compound_Name'][i], fontsize=6)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA Plot of Compounds')
    plt.grid(True)
    output_file = os.path.join(output, "pca_compounds.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")
    # plt.show()
