import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_violin(df, code_to_compound, output):
    """
    Plots violin plots with swarm plots overlay to visualize the distribution of compound intensities across groups.
    Generates plots for all compounds in groups of 5.

    Parameters:
        df (DataFrame): DataFrame containing the compound intensity data and sample labels.
        code_to_compound (dict): Dictionary mapping compound codes to compound names.
        output (str): Directory path to save the output plots.
    
    Returns:
        None: Saves the violin and swarm plots as PNG files.
    """
    df['Group'] = df['sample'].apply(lambda x: 'wt' if 'wt' in x else 'oe1' if 'oe1' in x else 'oe2')
    compound_codes = [col for col in df.columns if col not in ['sample', 'Group']]
    
    num_compounds = len(compound_codes)
    compound_chunks = [compound_codes[i:i + 5] for i in range(0, num_compounds, 5)]
    
    for idx, compounds in enumerate(compound_chunks):
        melted_df = df.melt(id_vars=['sample', 'Group'], value_vars=compounds,
                            var_name='Compound', value_name='Intensity')
        
        melted_df['Compound'] = melted_df['Compound'].map(code_to_compound).fillna(melted_df['Compound'])
        plt.figure(figsize=(12, 6))
        sns.violinplot(x='Compound', y='Intensity', hue='Group', data=melted_df, split=True, inner=None)
        sns.swarmplot(x='Compound', y='Intensity', hue='Group', data=melted_df, dodge=True, color='k', alpha=0.6, marker="o", edgecolor="gray")
        plt.title('Distribution of Compound Intensities Across Groups')
        plt.xlabel('Compound')
        plt.ylabel('Intensity')
        plt.legend(title='Group', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=90, fontsize=6)
        plt.tight_layout()
        output_file = os.path.join(output, f"density_plot_part_{idx + 1}.png")
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to {output_file}")
