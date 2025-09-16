import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def plot_correlation_circle(df, features, axis1=1, axis2=2):
    """
    Standardize features, fit PCA, and plot correlation circle for two chosen axes.
    """
    X = df[features].dropna()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA()
    X_pca = pca.fit_transform(X_scaled)

    pcs = pca.components_
    x_axis = axis1 - 1
    y_axis = axis2 - 1

    plt.figure(figsize=(6,6))
    for i, feature in enumerate(features):
        plt.arrow(0, 0, pcs[x_axis, i], pcs[y_axis, i], 
                  head_width=0.05, head_length=0.05, fc='red', ec='red')
        plt.text(pcs[x_axis, i]*1.1, pcs[y_axis, i]*1.1, feature, fontsize=9)

    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)
    circle = plt.Circle((0,0), 1, color='blue', fill=False, linestyle='--')
    plt.gca().add_artist(circle)
    plt.xlabel(f"PC{axis1}")
    plt.ylabel(f"PC{axis2}")
    plt.title(f"Correlation circle (PC{axis1} vs PC{axis2})")
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.grid()
    plt.show()
