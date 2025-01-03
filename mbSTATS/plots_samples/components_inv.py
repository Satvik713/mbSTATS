from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

def investigate(df, top_n):
    """
    Performs PLS-DA on the provided DataFrame, identifies the top contributing
    compounds for Component 1 and Component 2, and plots the results.
    
    Parameters:
        df (DataFrame): DataFrame with samples as rows and compounds as columns.
                         The first column should be 'sample' indicating sample labels.
        top_n (int): Number of top contributing compounds to display for each component.
    
    Returns:
        loadings_df (DataFrame): DataFrame of compounds and their loadings for both Component 1 and 2.
    """
    sample_labels = df['sample']
    compound_data = df.drop(columns='sample')
    labels = sample_labels.apply(lambda x: 1 if 'oe' in x else 0)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(compound_data)
    pls = PLSRegression(n_components=2)
    pls.fit(X_scaled, labels)
    
    loadings_df = pd.DataFrame({
        'Compound': compound_data.columns,
        'Component_1_Loading': pls.x_loadings_[:, 0],
        'Component_2_Loading': pls.x_loadings_[:, 1]
    }).set_index('Compound')

    top_contributors_1 = loadings_df['Component_1_Loading'].abs().sort_values(ascending=False).head(top_n)
    top_contributors_2 = loadings_df['Component_2_Loading'].abs().sort_values(ascending=False).head(top_n)
    
    plt.figure(figsize=(10, 6))
    top_contributors_1.plot(kind='bar', color='skyblue')
    plt.title(f'Top {top_n} Compounds Contributing to Component 1')
    plt.xlabel('Compound')
    plt.ylabel('Loading Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(10, 6))
    top_contributors_2.plot(kind='bar', color='lightgreen')
    plt.title(f'Top {top_n} Compounds Contributing to Component 2')
    plt.xlabel('Compound')
    plt.ylabel('Loading Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return loadings_df
