import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("PRJEB64127.csv")

# Create a new DataFrame to store the split strings
new_rows = []

# Iterate through the original DataFrame
for index, row in df.iterrows():
    files = row["ftp_submitted"].split(";")  # Split the string by semicolons
    for file in files:
        new_row = {"ftp_submitted": file.strip()}  # Create a new row
        new_rows.append(new_row)

# Create a new DataFrame from the new rows
new_df = pd.DataFrame(new_rows)
pd.set_option("display.max_columns", 1)
pd.set_option("display.max_rows", 516)
pd.set_option("display.max_colwidth", None)

# Save the new DataFrame to a new CSV file
new_df.to_csv("split_data.csv", index = False)
