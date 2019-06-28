"""
PROVIDES SUPPORT FUNCTIONS FOR ED PYTHON SCRIPTS 
@author: erik
"""

import pandas as pd
import numpy as np

# Functions to emulate stringr:: package in R
def str_subset(x,pat):
    x = pd.Series(x)
    if len(x)==0:
        return None
    x = x[x.str.contains(pat)].tolist()
    return(x)
    
def str_which(x,pat):
    x = pd.Series(x)
    if len(x)==0:
        return None
    hit = x.str.contains(pat)
    idx = np.where(hit)[0]
    return(idx)

# Custom function to extract the date and hour from the Arrived column in EPIC
def epic_date_to_data(x,pat='%d/%m/%y %H:%M'):
    x_mat = pd.Series(x).str.strip().str.split('\\s',expand=True)
    x_slice = x_mat.iloc[:,0] + ' ' + x_mat.iloc[:,1].str.slice(0,2) + ':' + x_mat.iloc[:,1].str.slice(2,4)
    x_date = pd.to_datetime(x_slice,format=pat)
    x_mat.iloc[:,0]
    return(x_date)

