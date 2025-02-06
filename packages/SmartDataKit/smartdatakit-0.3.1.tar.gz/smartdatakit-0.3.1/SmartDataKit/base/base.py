from abc import ABC, abstractmethod
import pandas as pd




class BaseInspection(ABC):

    @abstractmethod
    def DatatypesInspection(self, df: pd.DataFrame):

        pass

    @abstractmethod
    def SummeryStatistics(self, df: pd.DataFrame):

        pass

    @abstractmethod
    def Nullinspection(self, df: pd.DataFrame):

        pass

    @abstractmethod
    def NullHeatmap(self, df: pd.DataFrame):
        
        pass

    @abstractmethod
    def CategoricalValuecounts(self, df: pd.DataFrame):

        pass



class BaseUnivariante(ABC):

    @abstractmethod
    def NumericalUnivariate(self):
        pass

    @abstractmethod
    def CategoricalUnivariate(self):
        pass

    @abstractmethod
    def NumericalBoxplot(self):
        pass

    @abstractmethod
    def TargetImbalancePlot(self):
        pass    