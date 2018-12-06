#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:33:50 2018

@author: jean
"""
from crossvalidation import *

def best_hyp_param_gridsearch(values,dataset,k):
    # GRIDSEARCH
    nb_param=len(values[0])
    mapping=np.meshgrid(*[param.squeeze() for param in values])
    mapping=np.asarray(mapping)
    mapping=mapping.reshape(nb_param,-1).T
    results=[crossvalidation(cnn(configuration),dataset,k) for configuration in mapping]
    best_index= np.unravel_index(np.argmin(val, axis=None), a.shape)
    return values[best_index],np.amin(results)

def best_hyp_param_random(min_vals,max_vals,nb_points,dataset,k):
    # RANDOM SEARCH
    values= [min_vals[i] + np.sample(i)*(max_vals[i]-min_val[i]) for i in range(len(min_vals))]
    results=[[crossvalidation(cnn(par),dataset,k) for parameter_value in values[0]] for parameter in values[1]]
    best_index= np.unravel_index(np.argmin(val, axis=None), a.shape)
    return values[np.argmin(results)],np.amin(results)



    