import csv
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from preprocess import preprocess_data

def create_dataset(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    data = preprocess_data(data)
    if not data:
        print("No data after preprocessing.")
        return
    csv_file = 'data.csv'
    fieldnames = data[0].keys()
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print("Data written to CSV file:", csv_file)


def split_data():
    df = pd.read_csv("data.csv", encoding="latin1")
    train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)
    train_df.to_csv("train_data.csv", index=False)
    val_df.to_csv("val_data.csv", index=False)
    print("CSV file split into training and validation sets successfully.")

    
if __name__ == "__main__":
    json_file_path = "questions_answers.json"
    create_dataset(json_file_path)
    split_data()
