import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

# Load test data
test = pd.read_csv('data/test.csv')
X_test = test.drop('species', axis=1)
y_test = test['species']

# Load the model
model = joblib.load('models/model.pkl')

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save evaluation metrics
with open('models/evaluation.txt', 'w') as f:
    f.write(f'Accuracy: {accuracy}\n')
