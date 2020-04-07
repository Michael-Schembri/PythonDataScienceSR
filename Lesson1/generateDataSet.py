import pandas as pd
import numpy as np

def generate(totalLines, seed = 0):
    nLines = int(totalLines/2)
    
    np.random.seed(seed)
    h = np.random.normal(176, 4, nLines)
    w = np.random.normal(70, 3,nLines)
    s = np.random.normal(43, 2 ,nLines)
    l = np.full(nLines, 'male')
    d = zip(h,w,s,l)

    mdf = pd.DataFrame(list(d), columns = ["Height", "Weight", "ShoeSize", "Label"])

    h = np.random.normal(163, 4, nLines)
    w = np.random.normal(70, 3, nLines)
    s = np.random.normal(36, 2, nLines)
    l = np.full(nLines, 'female')
    d = zip(h,w,s,l)

    fdf = pd.DataFrame(list(d), columns = ["Height", "Weight", "ShoeSize", "Label"])
    print(np.random.seed())
    return pd.concat([fdf, mdf], 0) 