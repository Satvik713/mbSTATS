import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import os 

def perform_pls_da_and_plot(data, code_to_compound, output):
    """
    Perform PLS-DA on the given data, create a scatter plot with compound names, and return components for VIP score plotting.

    Parameters:
    - data (DataFrame): The data containing features to perform PLS-DA on (excluding 'Compounds' column).
    - code_to_compound (dict): A dictionary mapping compound codes to compound names.
    - save_path (str): Path to save the PLS-DA plot.
    
    Returns:
    - vip_scores (array): The VIP scores for the features.
    - feature_names (list): The names of the features (compounds) corresponding to the VIP scores.
    """
    X = data.drop(columns=['Compounds'])
    y = data['Compounds'] 
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    X_std = StandardScaler().fit_transform(X)
    pls = PLSRegression(n_components=2)
    pls_components = pls.fit_transform(X_std, y_encoded)
    pls_df = pd.DataFrame(pls_components[0], columns=['PLS1', 'PLS2'])

    compound_codes = label_encoder.inverse_transform(y_encoded)
    pls_df['Compound'] = [code_to_compound.get(code, 'Unknown') for code in compound_codes]
    plt.figure(figsize=(10, 8))
    plt.scatter(pls_df['PLS1'], pls_df['PLS2'], color='b', s=50)

    for i in range(pls_df.shape[0]):
        offset_x = np.random.uniform(0.02, 0.05)
        offset_y = np.random.uniform(0.02, 0.05)
        plt.text(pls_df['PLS1'][i] + offset_x, pls_df['PLS2'][i] + offset_y, pls_df['Compound'][i], fontsize=6)

    plt.xlabel('PLS Component 1')
    plt.ylabel('PLS Component 2')
    plt.title('PLS-DA Plot')
    plt.grid(True)

    output_file = os.path.join(output, "pls_da_plot_compounds.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")
