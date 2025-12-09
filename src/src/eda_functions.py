import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def dataset_overview(df):
    print("\n===== DATASET OVERVIEW =====")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nMissing values:")
    print(df.isna().sum())

def summary_statistics(df):
    print("\n===== NUMERIC SUMMARY =====")
    display(df.describe().T)

def categorical_summary(df):
    print("\n===== CATEGORICAL SUMMARY =====")
    for col in df.select_dtypes(include='object').columns:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().head(5))

def correlation_heatmap(df):
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm', annot=False)
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
        lower = q1 - 1.5*iqr
        upper = q3 + 1.5*iqr
        count = df[(df[col] < lower) | (df[col] > upper)].shape[0]
        report[col] = count
    return pd.DataFrame.from_dict(report, orient='index', columns=['Outliers'])
