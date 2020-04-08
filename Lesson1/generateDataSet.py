import pandas as pd
import numpy as np

def generate(totalLines, seed = 0):
    nLines = int(totalLines/2)
    
    np.random.seed(seed)
    h = np.random.normal(173, 4, nLines)
    w = np.random.normal(65, 6,nLines)
    s = np.random.normal(42, 2 ,nLines)
    l = np.full(nLines, 'male')
    d = zip(h,w,s,l)

    mdf = pd.DataFrame(list(d), columns = ["Height", "Weight", "ShoeSize", "Label"])

    h = np.random.normal(163, 4, nLines)
    w = np.random.normal(60, 6, nLines)
    s = np.random.normal(37, 2, nLines)
    l = np.full(nLines, 'female')
    d = zip(h,w,s,l)

    fdf = pd.DataFrame(list(d), columns = ["Height", "Weight", "ShoeSize", "Label"])
    ds = pd.concat([fdf, mdf], 0)
    ds = ds.reset_index(drop=True) 
    return ds