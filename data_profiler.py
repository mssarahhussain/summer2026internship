import numpy as np
import pandas as pd


def load_csv():
    """Ask the user for a CSV file and load it into a Pandas DataFrame."""

    # input() --> user inputs csv file path
    # strip() --> removes accidental spaces in path
    file_name = input("Enter the path to your CSV file: ").strip()

    # Make sure file name ends in csv
    # lower() --> allows file name to be uppercase .CSV
    if not file_name.lower().endswith(".csv"):
        print("Error: Please enter a CSV file.")
        return None

    try:
        # pd.read_csv() reads the CSV and stores it as a DataFrame.
        dataframe = pd.read_csv(file_name)
        return dataframe
        # if the file is not found prints the error
    except FileNotFoundError:
        print("Error: File not found.")
        return None


def profile_data(dataframe):
    """Calculate and print a simple profile of the dataset."""

    # dataframe.shape returns (number of rows, number of columns).
    print("\nDATASET OVERVIEW")
    print("Rows:", dataframe.shape[0])
    print("Columns:", dataframe.shape[1])

    # dataframe.columns --> prints list of all the names of the columns
    print("Column names:", list(dataframe.columns))

    # duplicated() and sum() --> mark the repeated rows and counts them
    print("Duplicate rows:", dataframe.duplicated().sum())

    print("\nCOLUMN SUMMARY")

    # New table created 
    column_summary = pd.DataFrame({
        # dtypes --> type of data in each colummn 
        "Data type": dataframe.dtypes.astype(str),

        # isna() and sum() --> finds missing values and counts them 
        "Missing values": dataframe.isna().sum(),

        # mean() --> finds how much the column are missing values and multiples by 100 to make it a percentage
        "Missing percentage": (dataframe.isna().mean() * 100).round(2)
    })
    print(column_summary)

    # Selects only the number columns to use for calculations 
    numeric_data = dataframe.select_dtypes(include=np.number)

    print("\nNUMERIC SUMMARY")

    # Show a message if there are no numeric columns to calculate.
    if numeric_data.empty:
        print("No numeric columns were found.")
    else:
        # Create a table of statistics for every numeric column.
        numeric_summary = pd.DataFrame({
            "Mean": numeric_data.mean(),
            "Median": numeric_data.median(),
            "Standard deviation": numeric_data.std()
        })
        print(numeric_summary.round(2))

        print("\nCORRELATION MATRIX")

        # corr() measures how strongly numeric columns are related.
        # Values are between -1 and 1.
        print(numeric_data.corr().round(2))


def main():
    # First ask for and load the CSV file.
    dataframe = load_csv()

    # Only create the report if the CSV was loaded successfully.
    if dataframe is not None:
        profile_data(dataframe)


# This makes main() run when this file is started directly.
if __name__ == "__main__":
    main()
