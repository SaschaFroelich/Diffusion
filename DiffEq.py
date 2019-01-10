#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:35:51 2018

@author: sascha
"""

import numpy as np
import matplotlib.pyplot as plt
import copy as cp

"""dynfun returns dz/dt"""
def dynfun(CurrentValues,params):
    N = CurrentValues.shape[0]; # no of dimensions
    M = params[blat]*(-np.ones([N,N])+np.eye(N))
    return params[k]*(M@sigmoid(CurrentValues,params[r],params[o]) + params[blin]*(params[g]*np.ones([N,1]) - params[z])) + params[w];

N = 9; # dimensionality of z
z = np.random.uniform(low=-5,high=5,size=[N,1])
#z = np.array([2.,3.,-2.]);
#z = z[:,None]

"""Set parameter values"""
g = 10;
blat = 1.7;
k = 4;
r = 1;
oc = g/2
blin = blat/ (2*g)

"""Control variable w"""
w = np.zeros([N,1]);


class DiffEq(object):
    
    def __init__(self,dynfun,params,timesteps,dt,InitialValues):
        self.dynfun = dynfun;
        self.params = params;
        self.timesteps = timesteps;
        self.dt = dt;
        self.InitialValues = InitialValues;
    
    
    def increment(self,CurrentValues):
        return dynfun(CurrentValues,params)*dt
        
    def Run(self):
        History = np.zeros([self.InitialValues.shape[0], timesteps]);
        CurrentValues = cp.copy(InitialValues)
        for t in range(self.timesteps):
            History[:, t] = CurrentValues[:, 0];
            CurrentValues[:, 0] = CurrentValues[:, 0] + self.increment(CurrentValues,self.params)
            
        self.History = History;