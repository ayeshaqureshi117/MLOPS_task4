import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load training data
train = pd.read_csv('data/train.csv')
X_train = train.drop('species', axis=1)
y_train = train['species']

# Train a RandomForest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'models/model.pkl')
