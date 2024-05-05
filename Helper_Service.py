import pandas as pd
import glob

# Input and output file paths
input_path = "C:/Users/alika/Desktop/Reporter_Project/Inputs"
output_path = "C:/Users/alika/Desktop/Reporter_Project/Outputs/veri.xlsx"

# Get the list of .csv files
file_names = glob.glob(input_path + "/*.csv")

# Read the first .csv file to start with
merged_df = pd.read_csv(file_names[0])

# Append 'Checks' columns from the rest of the files
for filename in file_names[1:]:
    # Get the checks column
    checks_column = pd.read_csv(filename)['Checks']
    # Extract the file name without extension
    file_name_without_extension = filename.split("/")[-1].split(".csv")[0]
    # Rename the checks column with the file name
    checks_column.name = file_name_without_extension
    # Append the checks column to the merged dataframe
    merged_df[file_name_without_extension] = checks_column

# Convert the appended dataframe to Excel
merged_df.to_excel(output_path, index=False)
print("Conversion to Excel is completed.")
