VANET Attack Prioritization

Overview

This project detects and prioritizes different types of attacks in a VANET dataset using machine learning. It uses a Random Forest model to classify attacks and assigns a priority score based on confidence and frequency.

Files in the Project -
data_loading.py → Loads CSV datasets, 
filtering.py → Cleans and filters data, 
training_dataset.py → Trains ML model, 
prioritization.py → Calculates attack priority, 
visualization.py → Generates graphs.

Working -
Load multiple VANET datasets, 
Filter and clean data, 
Train Random Forest classifier, 
Predict attack types, 
Compute priority score : Priority Score = 0.7 × Confidence + 0.3 × Frequency, 
Visualize results using bar and line graphs.

Output -
attack_prioritization.csv → Ranked attack list, 
bar_graph.png → Priority comparison, 
line_graph.png → Trend visualization.

Run Project -

Run files in order:
python filtering.py, 
python training_dataset.py, 
python prioritization.py, 
python visualization.py.

Requirements -
pip install pandas numpy scikit-learn matplotlib seaborn.
