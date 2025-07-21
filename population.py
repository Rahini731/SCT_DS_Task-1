# SCT_DS_Task-1
import pandas as pd
import matplotlib.pyplot as plt

def plot_population_from_csv(file_path):
    df = pd.read_csv(file_path, skiprows=4)
    df_2022 = df[['Country Name', '2022']].dropna()
    df_2022 = df_2022.sort_values(by='2022', ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    plt.bar(df_2022['Country Name'], df_2022['2022'], color='steelblue')
    plt.xlabel('Country')
    plt.ylabel('Population in 2022')
    plt.title('Top 10 Most Populous Countries (2022)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

if _name_ == "_main_":
    csv_path = "API_SP.POP.TOTL_DS2_en_csv_v2_123456.csv"  # Replace this with your actual file name
    plot_population_from_csv(csv_path)
