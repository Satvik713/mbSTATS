import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_density(df, code_to_compound, output):
    """
    Plots the density of compound intensities across samples.

    Parameters:
        df (DataFrame): DataFrame containing the sample intensities.
        code_to_compound (dict): Dictionary mapping compound codes to compound names.
        output (str): Directory where plots will be saved.

    Returns:
        None: Saves the density plots as files.
    """
    compound_codes = [col for col in df.columns if col not in ['sample', 'Group']]
    compound_names = {code: code_to_compound.get(code, code) for code in compound_codes}
    melted_df = df.melt(id_vars='sample', value_vars=compound_codes, 
                        var_name='Compound', value_name='Intensity')
    
    melted_df['Compound'] = melted_df['Compound'].map(compound_names)
    unique_compounds = melted_df['Compound'].unique()
    compound_chunks = [unique_compounds[i:i + 5] for i in range(0, len(unique_compounds), 5)]
    
    for idx, compounds in enumerate(compound_chunks):
        plt.figure(figsize=(10, 6))
        sns.kdeplot(data=melted_df[melted_df['Compound'].isin(compounds)], 
                    x='Intensity', hue='Compound', fill=True, 
                    common_norm=False, palette='muted')
        
        plt.title(f'Density Plot of Compound Intensities (Compounds {idx * 5 + 1} to {idx * 5 + len(compounds)})')
        plt.xlabel('Intensity')
        plt.ylabel('Density')
        plt.tight_layout()
        output_file = os.path.join(output, f'density_plot_{idx + 1}.png')
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to {output_file}")
