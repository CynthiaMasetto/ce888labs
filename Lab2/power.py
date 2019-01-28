#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:26:19 2019

@author: cynthiamasetto
"""

import numpy as np
import compare as cp
def power(sample1, sample2, reps, size, alpha,K_iterations):
    count =0
    for i in range(reps):
        sampleA = np.random.choice(sample1, size)
        sampleB = np.random.choice(sample2, size)
        pv = cp.abTest(sampleA,sampleB,K_iterations)
        if(pv<1-alpha):
            count = count + 1
    return count/reps