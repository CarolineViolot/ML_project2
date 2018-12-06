#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:03:36 2018

@author: jean
"""

from ETL import *

def crossvalidation(cnn, dataset, k):
    size=int(len(dataset)/k)
    lengths= [size for i in range(0,k-1)] +[len(dataset)-size*(k-1)]
    subsets=torch.utils.data.random_split(dataset,lengths)
    for separated,i in zip(subsets,np.arange(0,len(subsets))):
        valid_set=separated
        train_set=torch.utils.data.ConcatDataset(subsets[:subsets.index(separated)]+subsets[subsets.index(separated)+1:])
        cnn.train(train_set)
        result[i]=cnn.test(valid_set)
    return np.mean(result)
        
        

    
