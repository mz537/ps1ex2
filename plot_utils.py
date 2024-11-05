import pandas as pd
import matplotlib.pyplot as plt


def plot_gdp(csv_file, countries, output_file='gdp_plot.png'):

    # Load the CSV file into a DataFrame
    data = pd.read_csv(csv_file)

    # Convert the 'date' column to a pandas datetime object
    data['date'] = pd.to_datetime(data['date'])

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plot each country's GDP over time
    for country in countries:
        country_data = data[data['country'] == country]
        plt.plot(country_data['date'], country_data['GDP'], label=country)

    plt.xlabel('Year')
    plt.ylabel('GDP (Current US T$)')
    plt.ylim(0, 20)
    plt.title('GDP Over Time (2002-2022)')
    plt.legend(loc='upper left')

    # Save the plot to a file
    plt.savefig(output_file)

    # Optionally, show the plot
    plt.show()


# plot the gdp
countries1 = ['China', 'Germany', 'Japan', 'Switzerland', 'United Kingdom']


plot_gdp("gdp_data.csv", countries1, output_file='gdp_plot.png')
