import pandas as pd
from sklearn.model_selection import train_test_split

# Load Iris dataset
data = pd.read_csv('data/iris.csv')

# Preprocess data (if needed)
# Split into train and test sets
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Save the splits
train.to_csv('data/train.csv', index=False)
test.to_csv('data/test.csv', index=False)
