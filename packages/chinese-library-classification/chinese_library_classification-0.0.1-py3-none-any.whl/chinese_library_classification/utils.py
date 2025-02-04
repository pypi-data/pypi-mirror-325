# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:50:34 2024

@author: sheoguo
"""

import json
import time
import os


def load_all_data():
    
    print("即将加载中图分类数据")
    file_path = os.path.join(os.path.dirname(__file__),'data','data.json')
    with open(file_path,'r',encoding='utf-8') as f:
        all_data = json.load(f)
        
    print("中图分类数据加载完成")  
    return all_data
    
def recurse_upper(data,num,upper):
    
    if data[num]["up_level"] != None:
        re = []
        up_level = data[num]["up_level"]
        re = [up_level,data[up_level]["name"]]
        upper.append(re)
        upper = recurse_upper(data,up_level,upper)
        
    return upper
        
                
        
    

    
    
