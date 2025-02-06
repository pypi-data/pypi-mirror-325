import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import sys
import io


from SmartDataKit.Exception import SmartDataKitException
from SmartDataKit.logger import logging

from SmartDataKit.base.base import BaseInspection as _BaseInspection




class DataInspection(_BaseInspection):

    def __init__(self, df: pd.DataFrame, method: str = None):
        self.df = df
        self.method = method

    def DatatypesInspection(self):
       
        try:
            print("\nData Types and Non-null Counts:")
            return self.df.info()
        except Exception as e:
            raise SmartDataKitException(sys, e)

    def SummeryStatistics(self):
       
        try:
            print("\nSummary Statistics (Numerical Features):")
            numerical_summary = self.df.describe()
            print("\nSummary Statistics (Categorical Features):")
            categorical_summary = self.df.describe(include=["O"])
            return numerical_summary, categorical_summary
        except Exception as e:
            raise SmartDataKitException(sys, e)

    def Nullinspection(self):
       
        try:
            missing_values = self.df.isnull().sum()
            missing_percent = (missing_values / len(self.df)) * 100
            return pd.DataFrame({"Missing_Values": missing_values, "Percentage": missing_percent})
        except Exception as e:
            raise SmartDataKitException(sys, e)

    def NullHeatmap(self):
        
        try:
            plt.figure(figsize=(10, 6))
            sns.heatmap(self.df.isnull(), cmap="viridis", cbar=False, yticklabels=False)
            plt.title("Missing Data Heatmap")
            plt.show()
        except Exception as e:
            raise SmartDataKitException(sys, e)

    def CategoricalValuecounts(self):
        
        try:
            for i in self.df.select_dtypes(include = 'object').columns:
                print(i)
                print(self.df[i].value_counts(normalize = True) * 100)
                print("*"*35)
        except Exception as e:
            raise SmartDataKitException(sys, e)

    def inspect(self):
       
        try:
            if self.method == "info":
                return self.DatatypesInspection()
            elif self.method == "summary":
                return self.SummeryStatistics()
            elif self.method == "nulls":
                return self.Nullinspection()
            elif self.method == "heatmap":
                return self.NullHeatmap()
            elif self.method == "value_counts":
                return self.CategoricalValuecounts()
            else:
                return "Invalid method. Available options: info, summary, nulls, heatmap, value_counts."
        except Exception as e:
            raise SmartDataKitException(sys, e)

