import os
import matplotlib.pyplot as plt
import numpy as np

def plot_grp_avg(df, code_to_compound, output):
    """
    Plots the average intensities of compounds across different sample groups.

    Parameters:
        df (DataFrame): DataFrame containing the sample intensities and group labels.
        code_to_compound (dict): Dictionary mapping compound codes to compound names.
        output (str): Directory where plots will be saved.
        
    Returns:
        None: Saves bar plots of average compound intensities across groups.
    """
    # Assign group labels based on sample names
    df['Group'] = df['sample'].apply(lambda x: 'wt' if 'wt' in x else 'oe1' if 'oe1' in x else 'oe2')

    # Select only numeric columns (assumed to be compound intensities) and group information
    compound_codes = [col for col in df.columns if col not in ['sample', 'Group']]
    selected_compounds_df = df[['sample', 'Group'] + compound_codes]

    # Calculate the average intensity for each compound per group
    avg_df = selected_compounds_df.groupby('Group')[compound_codes].mean().T  # Transpose for easier plotting
    
    # Map compound codes to names
    avg_df.index = avg_df.index.map(code_to_compound)

    # Split compounds into chunks of 5 for plotting
    compound_chunks = [avg_df.index[i:i + 5] for i in range(0, len(avg_df.index), 5)]

    # Generate bar plots for each chunk of compounds
    for idx, compounds in enumerate(compound_chunks):
        chunk_df = avg_df.loc[compounds]
        ax = chunk_df.plot(kind='bar', figsize=(10, 6))
        plt.title(f'Average Compound Intensities (Compounds {idx * 5 + 1} to {idx * 5 + len(compounds)})')
        plt.xlabel('Compounds')
        plt.ylabel('Average Intensity')
        plt.xticks(rotation=45, fontsize=8)  # Smaller font size for compound names
        plt.legend(title='Group')
        plt.tight_layout()

        # Save plot
        output_file = os.path.join(output, f'avg_compounds_{idx + 1}.png')
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to {output_file}")
