import os
import random
import string
import gzip
import shutil


def random_string(length):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def create_dummy_structure():
    os.makedirs("LinuxTutorialData", exist_ok=True)
    os.chdir("LinuxTutorialData")

    # Create subdirectories
    directories = ["RawData", "ProcessedData", "Analysis", "Models", "Results"]
    for dir in directories:
        os.makedirs(dir, exist_ok=True)

    # Create dummy CSV files in RawData
    for i in range(5):
        with open(f"RawData/dataset_{i}.csv", "w") as f:
            f.write("id,feature1,feature2,target\n")
            for j in range(1000):
                f.write(
                    f"{j},{random.random()},{random.random()},{random.choice([0, 1])}\n"
                )

    # Create a large file
    with open("RawData/large_dataset.csv", "w") as f:
        f.write("id,text,label\n")
        for i in range(1000000):
            f.write(f"{i},\"{random_string(100)}\",{random.choice(['A', 'B', 'C'])}\n")

    # Create some hidden files
    with open(".config", "w") as f:
        f.write("secret_key=abcdefghijklmnop\n")
        f.write("crucial_dataset=large_dataset.csv\n")
    with open(".gitignore", "w") as f:
        f.write("*.log\n*.tmp\n")

    # Create a compressed file
    with gzip.open("ProcessedData/compressed_data.csv.gz", "wt") as f:
        f.write("id,processed_feature1,processed_feature2\n")
        for i in range(10000):
            f.write(f"uid_{i},{random.random() * 10},{random.random() * 10}\n")

    # Create some log files
    for i in range(3):
        with open(f"analysis_run_{i}.log", "w") as f:
            f.write(f"Analysis started at {random_string(10)}\n")
            f.write(f"Processed 1000000 rows\n")
            f.write(f"Analysis completed at {random_string(10)}\n")

    # Create a dummy Python script
    with open("Models/train_model.py", "w") as f:
        f.write(
            """import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier

        # Load data
        data = pd.read_csv('../ProcessedData/processed_data.csv')
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(data.drop('target', axis=1), data['target'])
        # Train model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        # Save model
        import joblib
        joblib.dump(model, 'random_forest_model.joblib')
        """
        )

    print("Dummy file structure created successfully!")


if __name__ == "__main__":
    create_dummy_structure()
