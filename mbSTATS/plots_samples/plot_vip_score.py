import matplotlib.pyplot as plt
import numpy as np
import os

def plot_vip_scores(vip_scores, feature_names, output):
    """
    Plot VIP scores for the PLS model.

    Parameters:
    - vip_scores (array): The VIP scores from the PLS model.
    - feature_names (list): The names of the features (compounds) corresponding to the VIP scores.
    - save_path (str): Path to save the VIP score plot.

    Returns:
    - None
    """
    
    if len(vip_scores) != len(feature_names):
        print("Error: Length of VIP scores and feature names must be the same.")
        return

    sorted_idx = np.argsort(vip_scores)[::-1]
    vip_scores_sorted = vip_scores[sorted_idx]
    feature_names_sorted = [feature_names[i] for i in sorted_idx]
    plt.figure(figsize=(12, 8))
    plt.barh(feature_names_sorted, vip_scores_sorted, color='lightblue')
    plt.xlabel('VIP Score')
    plt.title('VIP Scores Plot')
    plt.grid(True)

    output_file = os.path.join(output, "vip_plot.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")