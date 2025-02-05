import os, sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod



class _UnivariantStartegy(ABC):
    # This is an abstract base class for univariate analysis strategies.
    # The `analyze` method must be implemented by subclasses to process and visualize data.
    # Parameters include dataframe, number of rows/columns, color for plots, and figure size.
    @abstractmethod
    def analyze(self, df: pd.DataFrame, nrows: int, ncols: int, colour: str =None, figsize=(15,10)):
        pass





class CategoricalUnivariateAnalysis(_UnivariantStartegy):
    def __init__(self, max_categories=20, sample_size=None):
        """
        max_categories: Maximum number of unique categories to plot per feature.
        sample_size: Number of samples to use for faster visualization (optional).
        """
        self.max_categories = max_categories
        self.sample_size = sample_size

    def analyze(self, df: pd.DataFrame, nrows: int, ncols: int, colour: str, figsize=(15, 10)):
        self.data = df.copy()
        if self.sample_size and len(df) > self.sample_size:
            self.data = self.data.sample(self.sample_size, random_state=42)  # Sampling if needed

        self.nrows = nrows
        self.ncols = ncols
        self.colour = colour
        self.figsize = figsize
        self.features = self.data.select_dtypes(include="object").columns
        plt.figure(figsize=self.figsize)
        plt.suptitle("Distribution of Categorical Features", fontsize=16, fontweight="bold")
        num_subplots = self.nrows * self.ncols

        for i, feature in enumerate(self.features):
            if i < num_subplots:
                plt.subplot(self.nrows, self.ncols, i + 1)

                # Limit to top N categories for better visualization
                top_categories = self.data[feature].value_counts().index[:self.max_categories]
                filtered_data = self.data[self.data[feature].isin(top_categories)]

                sns.countplot(x=filtered_data[feature], data=filtered_data, color=self.colour)

                plt.xticks(rotation=45)  # Rotate labels for better visibility
                plt.title(f"Distribution of {feature}")
                plt.xlabel(feature)
                plt.ylabel("Count")
            else:
                print(f"Warning: Skipping feature '{feature}' due to subplot limit.")
                break

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()



class NumericalUnivariantAnalysis(_UnivariantStartegy):
    def __init__(self, max_features=20, sample_size=None):
        """
        max_features: Maximum number of numerical features to plot.
        sample_size: Number of samples to use for faster visualization (optional).
        """
        self.max_features = max_features
        self.sample_size = sample_size

    def analyze(self, df: pd.DataFrame, nrows: int, ncols: int, colour: str, figsize=(15, 10)):
        self.data = df.copy()
        if self.sample_size and len(df) > self.sample_size:
            self.data = self.data.sample(self.sample_size, random_state=42)  # Sampling if needed

        self.nrows = nrows
        self.ncols = ncols
        self.colour = colour
        self.figsize = figsize
        self.features = self.data.select_dtypes(include="number").columns[:self.max_features]
        plt.figure(figsize=self.figsize)
        plt.suptitle("Distribution of Numerical Features", fontsize=16, fontweight="bold")
        num_subplots = self.nrows * self.ncols

        for i, feature in enumerate(self.features):
            if i < num_subplots:
                plt.subplot(self.nrows, self.ncols, i + 1)
                sns.histplot(self.data[feature], kde=True, color=self.colour)

                plt.title(f"Distribution of {feature}")
                plt.xlabel(feature)
                plt.ylabel("Frequency")
            else:
                print(f"Warning: Skipping feature '{feature}' due to subplot limit.")
                break

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

        
