import csv
import json
import pandas as pd
from sklearn.model_selection import train_test_split

def create_dataset(json_file_path):
    with open(json_file_path, mode="r") as file:
        data = json.load(file)
        print(data)

        csv_file_path = "data.csv"
        field_names = ["question", "answer", "context"]

        with open(csv_file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)

            writer.writeheader()
            for item in data:
                writer.writerow(item)

        print("CSV file created successfully.")

def split_data():
    df = pd.read_csv("data.csv")
    train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)
    train_df.to_csv("train_data.csv", index=False)
    val_df.to_csv("val_data.csv", index=False)
    print("CSV file split into training and validation sets successfully.")
if __name__ == "__main__":
    json_file_path = "questions_answers.json"
    create_dataset(json_file_path)
    split_data()
