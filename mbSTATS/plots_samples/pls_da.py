import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import os 

def pls_da_samples(data, output, code_to_compound):
    """
    Perform PLS-DA on the given data, create a scatter plot with compound names, 
    and return components for VIP score plotting.

    Parameters:
    - data (DataFrame): The data containing features to perform PLS-DA on (excluding 'sample' column).
    - code_to_compound (dict): A dictionary mapping compound codes to compound names.
    - save_path (str): Path to save the PLS-DA plot.

    Returns:
    - vip_scores (array): The VIP scores for the features.
    - feature_names (list): The names of the features (compounds) corresponding to the VIP scores.
    """
    
    X = data.drop(columns=['sample'])
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(data['sample'])  
    X_std = StandardScaler().fit_transform(X)
    pls = PLSRegression(n_components=2)
    pls_components = pls.fit_transform(X_std, y)
    pls_df = pd.DataFrame(pls_components[0], columns=['PLS1', 'PLS2'])
    sample_names = label_encoder.inverse_transform(y)
    feature_names = [code_to_compound.get(f'c{i+1}', f'Compound_{i+1}') for i in range(X.shape[1])]

    plt.figure(figsize=(10, 8))
    plt.scatter(pls_df['PLS1'], pls_df['PLS2'], color='b', s=50)

    for i in range(pls_df.shape[0]):
        offset_x = np.random.uniform(0.02, 0.05)
        offset_y = np.random.uniform(0.02, 0.05)
        plt.text(pls_df['PLS1'][i] + offset_x, pls_df['PLS2'][i] + offset_y, sample_names[i], fontsize=7)

    plt.xlabel('PLS Component 1')
    plt.ylabel('PLS Component 2')
    plt.title('PLS-DA Plot')
    plt.grid(True)

    output_file = os.path.join(output, "pls_da_plot_samples.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")

    vip_scores = calculate_vip_scores(pls, X_std, y)

    return vip_scores, feature_names

def calculate_vip_scores(pls, X, y):
    """
    Calculate the VIP scores for a PLS model.

    Parameters:
    - pls (PLSRegression): The fitted PLS model.
    - X (array): The feature matrix (samples x features).
    - y (array): The target variable.

    Returns:
    - vip_scores (array): The calculated VIP scores for each feature.
    """
    n_features = X.shape[1]
    n_components = pls.n_components
    X_std = StandardScaler().fit_transform(X)
    explained_variance = np.var(pls.x_scores_, axis=0)
    vip_scores = np.zeros(n_features)
    for i in range(n_features):
        w = pls.coef_[:, i]  
        vip_scores[i] = np.sqrt(n_components * np.sum(explained_variance * w**2) / np.sum(explained_variance))

    return vip_scores





