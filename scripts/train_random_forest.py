import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_random_forest(features, labels):
    # Initialize Random Forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    clf.fit(features, labels)
    
    # Save the trained model
    joblib.dump(clf, 'model/random_forest_model.pkl')
    print("Model trained and saved!")

if __name__ == "__main__":
    # Assuming features and labels are already prepared
    features = np.load('data/features.npy')   # Load pre-extracted features
    labels = np.load('data/labels.npy')       # Load corresponding labels (0 = natural, 1 = man-made)
    
    train_random_forest(features, labels)
