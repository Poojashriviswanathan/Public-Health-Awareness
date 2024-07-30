import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv('/content/survey.csv')  # Replace 'your_dataset.csv' with the actual file path

# Ensure 'mental_health_consequence' is treated as a categorical variable
data['mental_health_consequence'] = data['mental_health_consequence'].astype('category')

# Check and convert 'Age' and 'treatment' to numeric if necessary
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')  # Convert 'Age' to numeric
data['treatment'] = pd.to_numeric(data['treatment'], errors='coerce')  # Convert 'treatment' to numeric

# Example 1: Pie chart of Gender distribution
gender_counts = data['Gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution')
plt.show()

# Example 2: Bar chart of Mental Health Consequence
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.countplot(x='mental_health_consequence', data=data)
plt.xlabel('Mental Health Consequence')
plt.ylabel('Count')
plt.title('Mental Health Consequence Distribution')
plt.show()

