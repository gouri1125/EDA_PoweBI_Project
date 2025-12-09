import pandas as pd

dataset_links = {
    "IPL": "https://raw.githubusercontent.com/amankharwal/Website-data/master/IPL%20Player%20Stats.csv",
    "Bank": "https://raw.githubusercontent.com/jbrownlee/Datasets/master/bank.csv",
    "FoodDelivery": "https://raw.githubusercontent.com/amankharwal/Website-data/master/zomato.csv",
    "GDP": "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv",
    "CovidStates": "https://raw.githubusercontent.com/imdevskp/covid19-india-data/master/national/covid_vaccine_statewise.csv",
    "Avengers": "https://raw.githubusercontent.com/fivethirtyeight/data/master/avengers/avengers.csv",
    "WaterQuality": "https://raw.githubusercontent.com/amankharwal/Website-data/master/water_potability.csv",
    "USPresidents": "https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-states.csv",
    "IndianStates": "https://raw.githubusercontent.com/datameet/india-census-data/master/data/india_states.csv",
    "Emergency911": "https://raw.githubusercontent.com/Premalatha-success/Datasets/main/911.csv",
    "Mushroom": "https://raw.githubusercontent.com/dphi-official/Datasets/master/mushrooms.csv",
    "WineQuality": "https://raw.githubusercontent.com/plotly/datasets/master/winequality-red.csv",
    "CarEvaluation": "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
}

def load_dataset(name):
    url = dataset_links[name]
    df = pd.read_csv(url)
    print(f"\nLoaded {name} dataset. Shape: {df.shape}")
    return df

# Example usage:
ipl_df = load_dataset("IPL")
ipl_df.head()
