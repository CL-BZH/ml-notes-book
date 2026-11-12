#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:46:21 2024

@author: chris
"""
import numpy as np
from utils import relu, leaky_relu, adam

class NN:
    def __init__(self, input_size, hidden_layer_size, output_size, learning_rate=0.1, adam_optimizer=False):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_layer_size = hidden_layer_size
        self.lr = learning_rate
        self.adam_optimizer = adam_optimizer
        self.steps = 0
        
        
        # One fully connected hidden layer
        self.W_1 = np.random.uniform(-1, 1, size=(self.input_size, self.hidden_layer_size))
        self.b_1 = np.random.uniform(-1, 1, size=(1,self.hidden_layer_size))
        self.W_2 = np.random.uniform(-1, 1, size=(self.hidden_layer_size, self.output_size))
        self.b_2 = np.random.uniform(-1, 1, size=(1,self.output_size))
        
        self.m_W_1 = 0
        self.m_b_1 = 0
        self.v_W_1 = 0
        self.v_b_1 = 0
        
        self.m_W_2 = 0
        self.m_b_2 = 0
        self.v_W_2 = 0
        self.v_b_2 = 0
        
    # Forward
    def __call__(self, X):
        self.z_1 = X.dot(self.W_1) + self.b_1
        self.a_1, self.a_1_z_1_grad = leaky_relu(self.z_1)
        self.z_2 = self.a_1.dot(self.W_2) + self.b_2
        return self.z_2
    
    def step(self, W_1_grad, b_1_grad, W_2_grad, b_2_grad):
        """
            Update the weight matrices
        """
        self.steps += 1
        
        if self.adam_optimizer == True:
            self.W_1, self.m_W_1, self.v_W_1 = adam(self.steps, self.W_1, W_1_grad, self.m_W_1, self.v_W_1, self.lr)
            self.b_1, self.m_b_1, self.v_b_1 = adam(self.steps, self.b_1, b_1_grad, self.m_b_1, self.v_b_1, self.lr)
            self.W_2, self.m_W_2, self.v_W_2 = adam(self.steps, self.W_2, W_2_grad, self.m_W_2, self.v_W_2, self.lr)
            self.b_2, self.m_b_2, self.v_b_2 = adam(self.steps, self.b_2, b_2_grad, self.m_b_2, self.v_b_2, self.lr)
            
        else:
            self.W_1 -= self.lr * W_1_grad 
            self.b_1 -= self.lr * b_1_grad 
            self.W_2 -= self.lr * W_2_grad
            self.b_2 -= self.lr * b_2_grad 
        
            if self.steps % 100 == 0:
                self.lr *= 0.999
                #print(f"Step: {self.steps}. lr: {self.lr}")
        return self.lr
