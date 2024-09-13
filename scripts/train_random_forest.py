import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(X, y):
    # Flatten the two-channel features into a single feature vector per pixel
    X = X.reshape(X.shape[0], -1)  # Flatten VV and VH channels into one long feature vector

    # Split data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train a Random Forest model
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(clf, 'model/random_forest_model.pkl')

    print("Model training completed.")
