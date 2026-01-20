from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def main():
    """
    Display life expectancy projections for France from 1800 to 2100.
    """
    df = load("life_expectancy_years.csv")
    if df is None:
        raise SystemError("Failed to load file")

    france_data = df[df['country'] == 'France']
    if france_data.empty:
        raise ValueError("France not found in dataset")

    years = df.columns[1:].astype(int)
    life_expectancy = france_data.iloc[0, 1:].values

    plt.plot(years, life_expectancy)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(40))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
