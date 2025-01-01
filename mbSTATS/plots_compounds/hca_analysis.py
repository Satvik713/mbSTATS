import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from mbSTATS.color_pal import generate_color_palette
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import os

def plot_hca(data, output, code_to_compound):
    """
    Perform Hierarchical Clustering Analysis (HCA) on the given data and create a dendrogram plot with compound names.
    
    Parameters:
    - data (DataFrame): The data containing features to be clustered (excluding 'Compounds' column).
    - code_to_compound (dict): A dictionary that maps compound codes to compound names.
    - save_path (str): Path to save the dendrogram plot.
    - generate_color_palette (function): Function to generate color palette for the plot.
    - save_plot (function): Function to save the plot to the specified location.
    
    Returns:
    - None
    """
    data_for_clustering = data.drop(columns=["Compounds"])
    linked = linkage(data_for_clustering, method='ward')
    colors = generate_color_palette(len(data_for_clustering.columns))
    labels = [code_to_compound.get(code, code) for code in data['Compounds']]

    plt.figure(figsize=(12, 8))
    dendrogram(
        linked,
        labels=labels,  
        orientation='top',
        distance_sort='descending',
        show_leaf_counts=True,
        color_threshold=0.5  
    )

    plt.title('Hierarchical Cluster Analysis Dendrogram', fontsize=16)
    plt.xlabel('Compounds', fontsize=14)
    plt.ylabel('Distance', fontsize=14)
    plt.xticks(fontsize=6, rotation=55)  
    plt.yticks(fontsize=12)
    plt.tight_layout()
    output_file = os.path.join(output, "hca_compounds.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")
    # save_plot(plt, save_path)
    # plt.show()
