from load_csv import load
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt


def convert_population(value):
    """
    Convert population string with M/k suffix to numerical value.

    Args:
        value: String with population (e.g., "1.5M", "500k")

    Returns:
        Float value of population
    """
    if isinstance(value, str):
        if 'M' in value:
            return float(value.replace('M', '')) * 1e6
        elif 'k' in value:
            return float(value.replace('k', '')) * 1e3
    return float(value)


def main():
    """
    Display population projections for France and Belgium from 1800 to 2050.
    """
    df = load("population_total.csv")
    if df is None:
        raise SystemError("Failed to load file")

    df = df.set_index('country')
    france_data = df.loc['France']
    belgium_data = df.loc['Belgium']
    years = [str(year) for year in range(1800, 2051)]
    years_in_data = [year for year in years if year in df.columns]
    france_pop = [convert_population(france_data[year])
                  for year in years_in_data]
    belgium_pop = [convert_population(belgium_data[year])
                   for year in years_in_data]
    years_int = [int(year) for year in years_in_data]

    plt.plot(years_int, france_pop, label='France', color='green')
    plt.plot(years_int, belgium_pop, label='Belgium', color='blue')

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='lower right')

    ax = plt.gca()
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, p: f'{int(x/1e6)}M'))

    ax.yaxis.set_major_locator(MultipleLocator(20e6))
    ax.xaxis.set_major_locator(MultipleLocator(40))
    plt.xlim(1800, 2050)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
