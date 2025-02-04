# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:45:39 2024

@author: sheoguo
"""

import os
import json
from .utils import load_all_data, recurse_upper

class Chineselibraryclassification:
    
    """ Chineselibraryclassification class.
    
    Usage: 
        from chinese_library_classification import Chineselibraryclassification
        #load Chinese library classification database
        CLC = Chineselibraryclassification()
    
    """
    
    def __init__(self):
        
        pass
        
    def num2info(self,num):
        
        
        data = load_all_data()
        
        if num not in data.keys():
            print(f"!!!不存在此分类号:{num}")
            return None
        else:
            info = data[num]                        
            return info
    
    def num2upper(self,num):
        
        data = load_all_data()
        
        if num not in data.keys():
            print(f"!!!不存在此分类号:{num}")
            return None
        else:
            upper = recurse_upper(data,num,upper=[])        
            return upper
    
    def num2next(self,num):
        
        data = load_all_data()
        
        if num not in data.keys():
            print(f"!!!不存在此分类号:{num}")
            return None
        else:
            if data[num]["next_level"] == []:
                return []
            else:
                next_level_list = []
                for x in data[num]["next_level"]:
                    info = set()
                    info.add(x)
                    info.add(data[x]["name"])
                    next_level_list.append(info)
                return next_level_list
                    
                
         
        
        
        
        
             
                
        