import argparse
import os
from mbSTATS.data_preparation import load_csv_data
from mbSTATS.final_df_prep import create_summary_dataframe
from mbSTATS.normalization_methods.pqn_normalization import pqn_normalization
from mbSTATS.plots_samples.pca_analysis import perform_pca
from mbSTATS.plots_samples.hca_analysis import perform_hca
from mbSTATS.plots_samples.correlation_analysis import plot_correlation_matrix_compounds
from mbSTATS.plots_samples.pls_da import pls_da_samples
from mbSTATS.plots_compounds.hca_analysis import plot_hca
from mbSTATS.plots_compounds.pca_analysis import plot_pca
from mbSTATS.plots_compounds.correlation_matrix import plot_correlation_matrix
from mbSTATS.plots_samples.plot_vip_score import plot_vip_scores
from mbSTATS.plots_compounds.volcano import plot_volcano
from mbSTATS.plots_compounds.rf_feature_imp import rf_features
from mbSTATS.plots_compounds.heatmap_comp_v_samp import generate_heatmap
from mbSTATS.plots_compounds.pls_da_comps import perform_pls_da_and_plot
from mbSTATS.plots_compounds.violin_plot import plot_violin
from mbSTATS.plots_compounds.grp_avg import plot_grp_avg
from mbSTATS.plots_compounds.comp_density import plot_density
from mbSTATS.df_convert import convert
from mbSTATS.pval_calculation import calculate_p_values
from mbSTATS.pval_plot import plot_p_values

def main():
    parser = argparse.ArgumentParser(description="Run metabolomics analysis with mbSTATS")
    parser.add_argument('-f', '--folders', type=str, nargs='+', required=True, help="Folders containing data")
    parser.add_argument('-o', '--output', type=str, required=True, help="Folder to save the output plots")
    args = parser.parse_args()
    column_names = ["Start_Time", "End_Time", "Retention_Time", "Ion_Mode", 
                    "Intensity", "Area_Percentage", "Adjusted_Intensity", 
                    "Adjusted_Area_Percentage", "Peak_Width", "Flag", 
                    "Compound_Name", "CAS_Number", "Similarity_Score"]
    
    dataframes = load_csv_data(args.folders, column_names)
    print("Dataframes loaded:", list(dataframes.keys()))
    summary_df, compound_to_code = create_summary_dataframe(dataframes)
    code_to_compound = {value: key for key, value in compound_to_code.items()}

    print("Summary DataFrame:")
    print(summary_df)
    print("Compounds to code:")
    print(compound_to_code)
    pqn_normalized_df = pqn_normalization(summary_df)
    print("Normalization complete.")
    converted_df = convert(pqn_normalized_df)
    p_values_df = calculate_p_values(pqn_normalized_df)
    plot_p_values(p_values_df, code_to_compound, args.output, th=0.1)
    perform_pca(pqn_normalized_df, args.output)

    perform_hca(pqn_normalized_df, args.output)
    plot_correlation_matrix_compounds(pqn_normalized_df, code_to_compound, args.output)
    pls_da_samples(pqn_normalized_df, args.output, code_to_compound)
    
    plot_hca(converted_df, args.output, code_to_compound)
    plot_pca(converted_df, code_to_compound, args.output)
    plot_correlation_matrix(converted_df, args.output)
    perform_pls_da_and_plot(converted_df, code_to_compound, args.output)
    vip_scores, feature_names = pls_da_samples(pqn_normalized_df, args.output, code_to_compound)
    plot_vip_scores(vip_scores, feature_names, args.output)
    plot_violin(pqn_normalized_df, code_to_compound, args.output)
    plot_grp_avg(pqn_normalized_df, code_to_compound, args.output)
    plot_density(pqn_normalized_df, code_to_compound, args.output)

    print(f"Analysis complete. Plots saved in {args.output}")

if __name__ == "__main__":
    main()
