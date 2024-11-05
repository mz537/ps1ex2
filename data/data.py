import wbdata
import pandas as pd


def fetch_gdp_data(countries, start_year=2002, end_year=2022, output_file='gdp_data.csv'):
    """
    Fetch GDP data for given countries between specified years and save it to a CSV file.

    Parameters:
    countries (list)
    start_year (int)
    end_year (int)
    output_file (str)

    Returns:
    pd.DataFrame: The GDP data filtered by country and date.
    """
    indicator = 'NY.GDP.MKTP.CD'  # GDP (current US$)

    # Fetch the data from the World Bank API
    data = wbdata.get_dataframe({indicator: 'GDP'}, country=countries)

    # Reset the index to make 'date' and 'country' columns
    data = data.reset_index()

    # Convert the 'date' column to a pandas datetime object
    data['date'] = pd.to_datetime(data['date'])

    # Filter data between the specified start and end years
    data = data[(data['date'].dt.year >= start_year) & (data['date'].dt.year <= end_year)]

    # change data into trillion
    data['GDP'] = data['GDP'] / 1e12

    # Sort the data by country and date
    data = data.sort_values(by=['country', 'date'], ascending=[True, True])

    # Save the data to a CSV file
    data.to_csv(output_file, index=False)

    # Return the DataFrame for further use if needed
    return data


# Example usage of the function
countries = ['GB', 'JP', 'CN', 'DE', 'CH']  # UK, Japan, China, Germany, Switzerland
gdp_data = fetch_gdp_data(countries, start_year=2002, end_year=2022, output_file='gdp_data.csv')


# Display the first few rows of the fetched data
print(gdp_data.head())
