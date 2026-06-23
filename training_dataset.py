import pandas as pd
import numpy as np

#install required libraries (pip install pandas numpy scikit-learn if required)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

from filtering_dataset import filtered_datasets

# Assuming filtered_data1 to filtered_data6 are preprocessed
#filtered_datasets = [filtered_data1, filtered_data2, filtered_data3, filtered_data4, filtered_data5, filtered_data6]
full_data = pd.concat(filtered_datasets, ignore_index=True)

# Encoding categorical labels
full_data['category'] = full_data['category'].astype('category').cat.codes
full_data['specific_class'] = full_data['specific_class'].astype('category').cat.codes

# Splitting into features and target
X = full_data.drop(columns=['category', 'specific_class'])  # Features
y = full_data['specific_class']  # Attack type

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predictions & Probabilities
y_pred = clf.predict(X_test)
y_probs = clf.predict_proba(X_test)  # Get probability scores

# Evaluate the model
if __name__ == "__main__":
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))

#Prevent execution when imported
if __name__ == "__main__":
    pass