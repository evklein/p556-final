from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class CreditTotalDaysOverdueTransformer(BaseEstimator, TransformerMixin):
    '''For each loan application: searches through all bureau data and finds the number of 
    days overdue across all bureaus.

    Reason: People with a history of late credit repayment may be unreliable borrowers.

    Required ancillary dataset(s): Bureau data, untransformed. Joined on `SK_ID_CURR`
    '''
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, bureaus):
        df = pd.DataFrame(X.copy())        
        df['BUREAUS_TOTAL_CREDIT_DAY_OVERDUE'] = df['SK_ID_CURR'].apply(
            lambda id_curr: bureaus[bureaus['SK_ID_CURR'] == id_curr]['CREDIT_DAY_OVERDUE'].sum()
        )
        return df
    
class MeanDaysCreditTransformer(BaseEstimator, TransformerMixin):
    '''
    For each loan application, shows the last time that the clinet
    requested credit from all bureaus.

    Reason: Frequent borrowers or recent credit requests may be less reliable.

    Required ancillary dataset(s): Bureau data, untransformed. Joined on `SK_ID_CURR` 
    '''
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X
