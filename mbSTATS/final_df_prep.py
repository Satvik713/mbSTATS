import pandas as pd

def create_summary_dataframe(dataframes, required_columns=["Compound_Name", "Area_Percentage"]):
    # Identify common compounds across all DataFrames
    common_compounds = set(dataframes['wt_wt1_1']['Compound_Name'])  # Starting from one of the dataframes, e.g., wt_wt1_1
    for df in dataframes.values():
        common_compounds.intersection_update(set(df['Compound_Name']))

    compound_to_code = {compound: f"c{i+1}" for i, compound in enumerate(sorted(common_compounds))}

    data = []

    # Define a function to extract data for each sample
    def extract_values(df, sample_name):
        values = {'sample': sample_name}
        for compound, code in compound_to_code.items():
            # Use Area_Percentage or any specific metric from the original DataFrame
            value = df.loc[df['Compound_Name'] == compound, 'Area_Percentage'].values
            values[code] = value[0] if len(value) > 0 else None
        return values

    for sample_name, df in dataframes.items():
        data.append(extract_values(df, sample_name))

    summary_df = pd.DataFrame(data)

    return summary_df, compound_to_code
