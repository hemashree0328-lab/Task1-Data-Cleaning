import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Display the first 5 rows
print(df.head())
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Display the first 5 rows
print(df.head())

# Shape of the dataset
print("\nShape of Dataset:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Dataset information
print("\nDataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())
# Check missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
# Fill missing values in Income with median
df["Income"] = df["Income"].fillna(df["Income"].median())

# Check again
print("\nMissing Values After Filling:")
print(df.isnull().sum())
# Check duplicate rows
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())
# Remove duplicate rows
df = df.drop_duplicates()

# Check duplicates again
print("\nDuplicate Rows After Removing:")
print(df.duplicated().sum())

# Display new dataset shape
print("\nNew Shape of Dataset:")
print(df.shape)
# Standardize column names
df.columns = df.columns.str.lower()          # Convert to lowercase
df.columns = df.columns.str.strip()          # Remove leading/trailing spaces
df.columns = df.columns.str.replace(" ", "_") # Replace spaces with underscores

# Display updated column names
print("\nUpdated Column Names:")
print(df.columns)
# Remove extra spaces from all text columns
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

print("\nExtra spaces removed from text columns.")
# Display data types
print("\nData Types:")
print(df.dtypes)
# Convert dt_customer to datetime format
df["dt_customer"] = pd.to_datetime(df["dt_customer"], dayfirst=True)

print("\nUpdated Data Type of dt_customer:")
print(df["dt_customer"].dtype)
# Detect and remove outliers in the income column

Q1 = df["income"].quantile(0.25)
Q3 = df["income"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

df = df[(df["income"] >= lower_limit) & (df["income"] <= upper_limit)]

print("\nDataset Shape After Removing Outliers:")
print(df.shape)
print("\nFinal Dataset Information:")
print(df.info())

print("\nFirst 5 Rows of Cleaned Dataset:")
print(df.head())
# Save cleaned dataset
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")
print("\n========== DATA CLEANING SUMMARY ==========")
print("Original Dataset Shape :", pd.read_csv("marketing_campaign.csv", sep="\t").shape)
print("Cleaned Dataset Shape  :", df.shape)
print("Missing Values Remaining:")
print(df.isnull().sum())
print("Duplicate Rows Remaining:", df.duplicated().sum())