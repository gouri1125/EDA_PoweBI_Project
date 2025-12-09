import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def dataset_overview(df):
    print("\n===== DATASET OVERVIEW =====")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nMissing values:")
    print(df.isna().sum())
    print("\nData Types:")
    print(df.dtypes)

def summary_statistics(df):
    print("\n===== NUMERIC SUMMARY =====")
    display(df.describe(include='number').T)

def categorical_summary(df):
    print("\n===== CATEGORICAL SUMMARY =====")
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) == 0:
        print("No categorical columns.")
        return
    
    for col in cat_cols:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().head(5))

def correlation_heatmap(df):
    num_df = df.select_dtypes(include=np.number)
    if num_df.shape[1] < 2:
        print("Not enough numeric columns for correlation.")
        return
    
    plt.figure(figsize=(12,8))
    sns.heatmap(num_df.corr(), cmap="coolwarm", annot=False)
    plt.title("Correlation Heatmap")
    plt.show()

def plot_missing(df):
    plt.figure(figsize=(12,5))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title("Missing Values Heatmap")
    plt.show()

def outlier_report(df):
    report = {}
    num_cols = df.select_dtypes(include=np.number).columns
    
    for col in num_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        
        outliers = df[(df[col] < lower) | (df[col] > upper)].shape[0]
        report[col] = outliers
    
    return pd.DataFrame.from_dict(report, orient='index', columns=['Outlier_Count'])
