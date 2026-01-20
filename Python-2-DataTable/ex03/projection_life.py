from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Display the projection of life expectancy in relation to GDP per capita
    for the year 1900.
    """
    life_exp = load("life_expectancy_years.csv")
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    if life_exp is None or gdp is None:
        raise SystemError("Failed to load one or both files")

    # Set country as index for both dataframes
    life_exp = life_exp.set_index('country')
    gdp = gdp.set_index('country')

    # Extract data for year 1900
    year = '1900'

    if year not in life_exp.columns or year not in gdp.columns:
        raise ValueError(f"Year {year} not found in datasets")

    # Get 1900 data, dropping NaN values
    life_1900 = life_exp[year].dropna()
    gdp_1900 = gdp[year].dropna()

    # Find common countries (intersection)
    common_countries = life_1900.index.intersection(gdp_1900.index)

    # Extract values for common countries
    x_values = [gdp_1900[country] for country in common_countries]
    y_values = [life_1900[country] for country in common_countries]

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values, alpha=0.6)

    # Add title and labels
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')

    # Add grid for better readability
    plt.grid(True, alpha=0.3)

    # Set x-axis scale (log scale might be better for GDP data)
    plt.xscale('log')

    # Format x-axis ticks
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
