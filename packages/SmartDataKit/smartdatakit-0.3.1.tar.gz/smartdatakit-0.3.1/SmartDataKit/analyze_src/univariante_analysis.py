import os, sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

from SmartDataKit.base.base import BaseUnivariante as _BaseUnivariante
from SmartDataKit.Exception import SmartDataKitException




import sys
import matplotlib.pyplot as plt
import seaborn as sns

class UnivariateAnalysis(_BaseUnivariante):

    def __init__(self, df, nrows: int = None, ncols: int = None, colour: str = None, 
                 max_features=20, sample_size=None, figsize=(15, 10), target_column=None, method: str = None):
        try:
            self.df = df.copy()  
            self.nrows = nrows
            self.ncols = ncols
            self.colour = colour
            self.max_features = max_features
            self.sample_size = sample_size
            self.figsize = figsize
            self.method = method
            self.target_column = target_column
        except Exception as e:
            raise SmartDataKitException(sys, f"Initialization error: {e}")

    def NumericalUnivariate(self):
        try:
            data = self.df.select_dtypes(include=['number'])

            if self.sample_size and len(data) > self.sample_size:
                data = data.sample(self.sample_size, random_state=42)

            features = data.columns[:self.max_features]

            plt.figure(figsize=self.figsize)
            plt.suptitle("Numerical Feature Distributions", fontsize=14, fontweight="bold")

            for i, feature in enumerate(features):
                plt.subplot(self.nrows, self.ncols, i + 1)
                sns.histplot(data[feature], kde=True, color=self.colour)
                plt.title(f"{feature} Distribution")

            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise SmartDataKitException(sys, f"Error in NumericalUnivariate: {e}")

    def CategoricalUnivariate(self):
        try:
            self.features = self.df.select_dtypes(include="object").columns

            if self.sample_size and len(self.df) > self.sample_size:
                self.df = self.df.sample(self.sample_size, random_state=42)

            plt.figure(figsize=self.figsize)
            plt.suptitle("Distribution of Categorical Features", fontsize=16, fontweight="bold")
            
            num_subplots = self.nrows * self.ncols

            for i, feature in enumerate(self.features):
                if i < num_subplots:
                    plt.subplot(self.nrows, self.ncols, i + 1)

                    top_categories = self.df[feature].value_counts().index[:self.max_features]  
                    filtered_data = self.df[self.df[feature].isin(top_categories)]

                    sns.countplot(x=filtered_data[feature], data=filtered_data, color=self.colour)

                    plt.xticks(rotation=45)  
                    plt.title(f"Distribution of {feature}")
                    plt.xlabel(feature)
                    plt.ylabel("Count")
                else:
                    print(f"Warning: Skipping feature '{feature}' due to subplot limit.")
                    break

            plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
            plt.show()
        except Exception as e:
            raise SmartDataKitException(sys, f"Error in CategoricalUnivariate: {e}")

    def NumericalBoxplot(self):
        try:
            data = self.df.select_dtypes(include=['number'])

            if self.sample_size and len(data) > self.sample_size:
                data = data.sample(self.sample_size, random_state=42)

            features = data.columns[:self.max_features]

            plt.figure(figsize=self.figsize)
            plt.suptitle("Numerical Feature Boxplots", fontsize=14, fontweight="bold")

            for i, feature in enumerate(features):
                plt.subplot(self.nrows, self.ncols, i + 1)
                sns.boxplot(y=data[feature], color=self.colour)
                plt.title(f"Boxplot of {feature}")

            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise SmartDataKitException(sys, f"Error in NumericalBoxplot: {e}")

    def TargetImbalancePlot(self):
        try:
            if self.target_column is None:
                raise ValueError("Target column must be specified for imbalance check.")
            
            if self.target_column not in self.df.columns:
                raise ValueError(f"'{self.target_column}' is not a valid column in the dataset.")

            plt.figure(figsize=self.figsize)
            sns.countplot(x=self.df[self.target_column], color=self.colour)
            plt.title("Target Variable Distribution")
            plt.show()
        except Exception as e:
            raise SmartDataKitException(sys, f"Error in TargetImbalancePlot: {e}")

    def analyzer(self):
        try:
            method_mapping = {
                "histogram": self.NumericalUnivariate,
                "countplot": self.CategoricalUnivariate,
                "boxplot": self.NumericalBoxplot,
                "imbalance_check": self.TargetImbalancePlot
            }

            if self.method not in method_mapping:
                raise ValueError("Invalid method. Available options: histogram, countplot, boxplot, imbalance_check.")

            return method_mapping[self.method]()
        except Exception as e:
            raise SmartDataKitException(sys, f"Error in analyzer: {e}")
