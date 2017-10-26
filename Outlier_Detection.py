# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:15:23 2017

@author: athir

OUTLIER DETECTION USING CHEBYCHEV'S THEOROM
"""

def get_stats(pro_code):
    conn_str = (
        '
        )
    id_values = {}                    
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    cursor.execute("""Query to fetch data""")
    rows = np.asarray(cursor.fetchall())
    data = rows[:,1].astype(np.float)  
    id_values['data'] =  data
    id_values['mean'] =  np.mean(data)
    id_values['std'] =  np.std(data)
    id_values['skew'] =  scipy.stats.skew(data)
    id_values['kurtosis'] =  scipy.stats.kurtosis(data)
    id_values['hist']= np.hstack(data)   
    p1 = 0.01
    k = 1/sqrt(p1)
    print(k)
    odvu = id_values['mean'] + k*id_values['std']
    odvl = id_values['mean'] - k*id_values['std']
    id_values['upper_cut']= odvu
    id_values['outliers']= data[np.where( data > odvu )] 
    id_values['outlier percentage'] =  id_values['outliers'].shape[0]/id_values['data'].shape[0]*100
    cnxn.close() 
    return id_values
