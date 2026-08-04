import numpy as np
import pandas as pd


def load_csv():
    """Ask the user for a CSV file and load it into a Pandas DataFrame."""

    # input() pauses the program and lets the user type the file location.
    # strip() removes any accidental spaces before or after the path.
    file_name = input("Enter the path to your CSV file: ").strip()

    # Check that the file name ends in .csv.
    # lower() also accepts uppercase names such as DATA.CSV.
    if not file_name.lower().endswith(".csv"):
        print("Error: Please enter a CSV file.")
        return None

    try:
        # pd.read_csv() reads the CSV and stores it as a DataFrame.
        dataframe = pd.read_csv(file_name)
        return dataframe

    # These messages explain common problems without crashing the program.
    except FileNotFoundError:
        print("Error: The file could not be found. Check the file path and try again.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: The CSV file could not be read correctly.")

    return None


def profile_data(dataframe):
    """Calculate and print a simple profile of the dataset."""

    # dataframe.shape returns (number of rows, number of columns).
    print("\nDATASET OVERVIEW")
    print("Rows:", dataframe.shape[0])
    print("Columns:", dataframe.shape[1])

    # dataframe.columns contains the names of all columns.
    print("Column names:", list(dataframe.columns))

    # duplicated() marks repeated rows as True, and sum() counts them.
    print("Duplicate rows:", dataframe.duplicated().sum())

    print("\nCOLUMN SUMMARY")

    # This creates a new table containing information about every column.
    column_summary = pd.DataFrame({
        # dtypes shows the type of data in each column.
        "Data type": dataframe.dtypes.astype(str),

        # isna() finds missing values, and sum() counts them by column.
        "Missing values": dataframe.isna().sum(),

        # mean() finds the fraction of missing values. Multiplying by 100
        # changes the fraction into a percentage.
        "Missing percentage": (dataframe.isna().mean() * 100).round(2)
    })
    print(column_summary)

    # Keep only number columns because mean, median, standard deviation,
    # and correlation cannot be calculated for text columns.
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
