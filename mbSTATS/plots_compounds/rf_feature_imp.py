from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def rf_features(df, target_column='sample', n_estimators=100, random_state=42):
    """
    Performs Random Forest feature importance analysis on the provided DataFrame,
    identifies the most important features (compounds), and plots the results.
    
    Parameters:
        df (DataFrame): DataFrame with samples as rows and compounds as columns.
                         The first column should be 'sample' indicating sample labels.
        target_column (str): The name of the column containing the sample group labels.
        n_estimators (int): The number of trees in the Random Forest model.
        random_state (int): The random state for reproducibility.
    
    Returns:
        importance_df (DataFrame): DataFrame with compounds and their corresponding importance scores.
    """
    
    X = df.drop(columns=[target_column]) 
    y = LabelEncoder().fit_transform(df[target_column]) 
    rf_model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    rf_model.fit(X, y)
    feature_importances = rf_model.feature_importances_
    importance_df = pd.DataFrame({
        'Compound': X.columns,
        'Importance': feature_importances
    }).sort_values(by='Importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Compound', data=importance_df, palette='viridis')
    plt.title('Random Forest Feature Importance')
    plt.xlabel('Importance')
    plt.ylabel('Compound')
    plt.tight_layout()
    plt.show()
    
    return importance_df