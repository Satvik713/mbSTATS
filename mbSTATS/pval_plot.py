import matplotlib.pyplot as plt
import os 
from mbSTATS.color_pal import generate_color_palette

def plot_p_values(p_values_df, code_to_compound, output, th):
    """
    Plot p-values with a color palette and pastel colors, using compound names instead of codes.

    Parameters:
    p_values_df (DataFrame): A DataFrame containing compounds and their corresponding p-values.
    code_to_compound (dict): A dictionary mapping compound codes to their respective names.
    """
    p_values_df['Compound Name'] = p_values_df['Compound'].map(code_to_compound)

    if p_values_df['Compound Name'].isnull().any():
        print("Warning: Some compound codes could not be mapped to names.")
        print(p_values_df[p_values_df['Compound Name'].isnull()])

    compounds = p_values_df['Compound Name'].fillna(p_values_df['Compound'])  # Use original code if name is not mapped
    p_values = p_values_df['p-value']

    colors = generate_color_palette(len(compounds))
    plt.figure(figsize=(12, 8))
    plt.bar(compounds, p_values, color=colors)
    plt.axhline(y=th, color='red', linestyle='--', label='Significance Threshold (p = 0.05)')
    plt.xlabel('Compound Names', fontsize=14)
    plt.ylabel('p-value', fontsize=14)
    plt.title('P-Values for Each Compound', fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()
    output_file = os.path.join(output, "pvalue_plot.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Plot saved to {output_file}")