import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data(input_path, output_path):

    df = pd.read_csv(input_path)

    # Hapus customerID
    df.drop("customerID", axis=1, inplace=True)
    # Konversi TotalCharges
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Missing value
    df.dropna(subset=["TotalCharges"], inplace=True)

    # Encode target
    df["Churn"] = df["Churn"].map({
        "No": 0,
        "Yes": 1
    })

    # Binary encoding
    binary_cols = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "PaperlessBilling"
    ]

    for col in binary_cols:
        df[col] = df[col].map({
            "No": 0,
            "Yes": 1,
            "Female": 0,
            "Male": 1
        })

    # One hot encoding
    df = pd.get_dummies(
        df,
        drop_first=True
    )

    # Scaling
    scaler = StandardScaler()

    num_cols = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    df[num_cols] = scaler.fit_transform(
        df[num_cols]
    )

    os.makedirs(
        "dataset_preprocessing",
        exist_ok=True
    )

    df.to_csv(
        output_path,
        index=False
    )

    return df


if __name__ == "__main__":

    preprocess_data(
        "../dataset_raw/WA_Fn-UseC_-Telco-Customer-Churn.csv",
        "./dataset_preprocessing/telco_preprocessed.csv"
    )