import pandas as pd
import numpy as np

def generate(totalLines, seed = 0):
    nLines = int(totalLines/2)
    
    np.random.seed(seed)
    h = np.random.normal(170, 5, nLines)
    w = np.random.normal(65, 5,nLines)
    s = np.random.normal(42, 5 ,nLines)
    l = np.full(nLines, 'male')
    d = zip(h,w,s,l)

    mdf = pd.DataFrame(list(d), columns = ["Height", "Weight", "ShoeSize", "Label"])

    h = np.random.normal(162, 5, nLines)
    w = np.random.normal(60, 5, nLines)
    s = np.random.normal(38, 5, nLines)
    l = np.full(nLines, 'female')
    d = zip(h,w,s,l)

    fdf = pd.DataFrame(list(d), columns = ["Height", "Weight", "ShoeSize", "Label"])
    ds = pd.concat([fdf, mdf], 0)
    ds = ds.reset_index(drop=True) 
    return ds

def twoD10Array(totalLines):
    baseDice1 = np.random.randint(1,10, totalLines)
    baseDice2 = np.random.randint(1,10, totalLines)
    addDice = lambda x, y : x + y
    baseDiceSum = addDice(baseDice1, baseDice2)
    return baseDiceSum

def generateDD(totalLines, rseed = 0):
    nLines = int(totalLines/2)
    
    np.random.seed(rseed)
    hFunction = lambda x, y : (x + y)*2.54 
    wFunction = lambda x, y : x + (4.8*y)*.453
    sFunction = lambda x, y : round((x+y))/2
    
    baseh = np.full(nLines, 58)
    basew = np.full(nLines, 120)
    bases = np.full(nLines, 76)
    var = np.random.normal(11, 4, size=nLines)

    h = list(map(hFunction, baseh, var))
    w = list(map(wFunction, basew, var))
    s = list(map(sFunction, bases, var))
    l = np.full(nLines, 'male')
    d = list(zip(h,w,s,l))

    mdf = pd.DataFrame(d, columns = ["Height", "Weight", "ShoeSize", "Label"])

    baseh = np.full(nLines, 53)
    basew = np.full(nLines, 85)
    bases = np.full(nLines, 68)
    var = np.random.normal(11, 4, size=nLines)
    #var = twoD10Array(nLines)

    h = list(map(hFunction, baseh, var))
    w = list(map(wFunction, basew, var))
    s = list(map(sFunction, bases, var))
    l = np.full(nLines, 'female')
    d = list(zip(h,w,s,l))

    fdf = pd.DataFrame(d, columns = ["Height", "Weight", "ShoeSize", "Label"])
    return pd.concat([fdf, mdf], 0, ignore_index=True)

