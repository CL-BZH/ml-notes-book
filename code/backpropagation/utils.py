#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:51:32 2024

@author: chris
"""
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt


class Pattern2D(Enum):
    CIRCLE = 1
    DIAMOND = 2
    SQUARE = 3
 
    
def two_classes_pattern2D(num_obs: int, pattern: Pattern2D, plot: bool=False):
    x = np.random.uniform(-1, 1, size = (num_obs, 2))
    match pattern:
        case Pattern2D.CIRCLE:
            y = (np.sqrt(x[:,0]**2 + x[:,1]**2)<.75).astype(int)
        case Pattern2D.DIAMOND:
            y = ((np.abs(x[:,0]) + np.abs(x[:,1]))<1).astype(int)
        case Pattern2D.SQUARE:
            y = ((np.maximum(np.abs(x[:,0]), np.abs(x[:,1])))<.5).astype(int)

    if plot == True:
        fig, ax = plt.subplots()
        ax.plot(x[y==1, 0],x[y==1, 1], 'o', label='class 1', color='lime')
        ax.plot(x[y==0, 0],x[y==0, 1], 'x', label='class 0', color='blue')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.axis('equal')
        plt.tight_layout()
        plt.show()
        
    return x, y


def sigmoid(x):
    """
    Sigmoid function that returns the value of the sigmoid and of the grad
    """
    s = 1.0 / (1.0 + np.exp(-x))
    return s, s*(1-s)


def relu(x):
    """
    ReLU function that returns the value of the relu and of the grad
    """
    return x * (x > 0), 1. * (x > 0)


def leaky_relu(x):
    """
    ReLU function that returns the value of the relu and of the grad
    """
    leaky_coef = 0.001
    leak = leaky_coef * (x <= 0)
    return x * ((x > 0) + leak), 1. * (x > 0) + leak

def logloss(y_true, y_pred, eps=1e-16):
    """
    Logarithmic Loss
    """
    y_pred = np.maximum(y_pred,eps)
    y_pred = np.minimum(y_pred,(1-eps))
    return -(np.sum(y_true * np.log(y_pred) + (1-y_true)*np.log(1-y_pred)))/len(y_true)


def adam(t, w, dw, m, v, alpha = 0.1, beta1 = 0.9, beta2 = 0.999, epsilon = 1e-8):
    """
    Adam optimizer
    """
    # First-moment
    m = beta1*m + (1-beta1)*dw
    # Second-moment
    v = beta2*v + (1-beta2)*(dw**2)
    # Bias correction
    m_unbiased = m/(1-beta1**t)
    v_unbiased = v/(1-beta2**t)
    # Update weights
    w = w - alpha*(m_unbiased/(np.sqrt(v_unbiased) + epsilon))
    return w, m, v


def RMSprop(w, dw, vdw, alpha = 0.1, gamma=0.9):
        vdw = gamma * vdw + (1 - gamma) * dw ** 2
        w -= (alpha / (np.sqrt(vdw + 1e-08))) * dw
        return w, vdw
        
        