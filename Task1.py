import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv('sample.csv')

# Extract the 'genders' and 'counts' columns
genders = data['genders'].tolist()
counts = data['counts'].tolist()

# Create a bar chart
plt.bar(genders, counts, color=['blue', 'pink', 'purple', 'gray'])

# Customize the chart
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')

# Display the chart
plt.show()
