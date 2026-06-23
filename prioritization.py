import pandas as pd
import numpy as np

from training_dataset import full_data, clf, y_probs

# Example: Manually defined mapping of encoded specific_class values to attack names
custom_class_names = {
    0: "DoS Attack",
    1: "Spoofing RPM",
    2: "Spoofing SPEED",
    3: "Spoofing STEERING WHEEL"  
}

# Convert 'specific_class' to categorical
full_data['specific_class'] = full_data['specific_class'].astype('category')

# Compute frequency of each attack type (normalized)
attack_counts = full_data['specific_class'].value_counts(normalize=True).reindex(full_data['specific_class'].cat.categories, fill_value=0)

# Compute average confidence per attack
attack_confidence = {}
for i, attack_class in enumerate(clf.classes_):
    attack_confidence[attack_class] = np.mean(y_probs[:, i])  # Mean confidence per attack

# Replace specific_class values using custom names
attack_prioritization = pd.DataFrame({
    "Specific Class": [custom_class_names.get(a, f"Unknown Attack {a}") for a in clf.classes_],  # Use custom names
    "Frequency": attack_counts.values,
    "Avg Confidence": [attack_confidence.get(i, 0) for i in range(len(custom_class_names))]  # Default to 0 if missing
})

# Compute final prioritization score
attack_prioritization["Priority Score"] = (
    attack_prioritization["Avg Confidence"] * 0.7 +
    attack_prioritization["Frequency"] * 0.3
)

# Sort by priority score
attack_prioritization = attack_prioritization.sort_values(by="Priority Score", ascending=False)

# Store this DataFrame for further use in visualization
attack_prioritization.to_csv("attack_prioritization.csv", index=False)  # Save for reuse

# Display prioritized attack list
print("\n=== Attack Prioritization ===")
print(attack_prioritization)