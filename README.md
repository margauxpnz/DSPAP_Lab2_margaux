# **Essential Tools and Practices for Programming Projects in AI**

## Description

This project demonstrates:

- **Setting up a well-structured Python project**
- **Using conda to manage environments**
- **Version control with Git and GitHub**
- **Principal component analysis (PCA)** on nutritional data (sugars, fats, salt, protein, energy, fiber*)
- **Creating and using a generic function** to display a correlation circle

## 🛠️ Prerequisites

- Python >= 3.11
- conda for the environment
- Required libraries:
```bash
pip install numpy pandas matplotlib scikit-learn pyyaml
```

## Installation

Clone the project:
```bash
git clone https://github.com/your-repo/DSPAP_Lab2.git
cd DSPAP_Lab2
```

Create and activate the environment:
```bash
conda create -n lab2_env python=3.11
conda activate lab2_env
```


## Use

Example: load the data and launch a PCA

```python
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from src.pca_tools import plot_correlation_circle

# Load data
df = pd.read_csv("data/data_cleaned.csv")

# Standardize
X_scaled = StandardScaler().fit_transform(df[["sugars_100g", "fat_100g", 
"salt_100g", "proteins_100g", 
"energy-kcal_100g", "fiber_100g"]])

#PCA
pca = PCA(n_components=3)
pca.fit(X_scaled)

# Circle of correlation
features = ["sugars_100g", "fat_100g", "salt_100g", "proteins_100g", "energy-kcal_100g", "fiber_100g"]
plot_correlation_circle(pca, features, axis1=1, axis2=2)
```

## Contributors

- **Rim Slama Salmi** (notebook and project author)
- **Margaux Plounevez** (codes and README contributor)
