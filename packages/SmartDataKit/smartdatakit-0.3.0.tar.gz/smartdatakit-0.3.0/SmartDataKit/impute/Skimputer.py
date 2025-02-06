import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from SmartDataKit.Exception import SmartDataKitException 

class SKCustomImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy="mean"):  
        
        self.strategy = strategy
        self.fill_values_ = {} 

    def fit(self, X, y=None):
      
        try:
            X = pd.DataFrame(X)  

            if self.strategy == "mean":
                self.fill_values_ = X.mean()
            elif self.strategy == "median":
                self.fill_values_ = X.median()
            elif self.strategy == "mode":
                self.fill_values_ = X.mode().iloc[0]  
            else:
                raise SmartDataKitException("Unsupported strategy. Choose from 'mean', 'median', or 'mode'.")
            
            return self 
        except Exception as e:
            raise SmartDataKitException(f"Error in fit method: {str(e)}")

    def transform(self, X):
       
        try:
            X = pd.DataFrame(X)  
            return X.fillna(self.fill_values_).values 
        except Exception as e:
            raise SmartDataKitException(f"Error in transform method: {str(e)}")

    def fit_transform(self, X, y=None):
       
        try:
            return self.fit(X).transform(X)
        except Exception as e:
            raise SmartDataKitException(f"Error in fit_transform method: {str(e)}")








