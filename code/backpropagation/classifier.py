#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:38:03 2024

@author: chris
"""
import numpy as np
from utils import sigmoid, logloss
from neural_network import NN

class Classifier:
    def __init__(self, learning_rate=0.1, adam_optimizer=False):
        self.NN = NN(input_size=2, hidden_layer_size=4, output_size=1, learning_rate=learning_rate, adam_optimizer=adam_optimizer)
        self.grads = {'b1':[], 'W1':[], 'b2':[], 'W2':[]}
        
        #print(f"y_true: {self.y_true}")
    
    def predict(self, X, y_true):
        self.X = X
        self.y_true = y_true.reshape(-1,1)
        
        self.y_pred = sigmoid(self.NN(self.X))[0]
        #print(f"y_pred: {y_pred}")
        return self.y_pred
        
    def loss(self, y_pred):
        return logloss(self.y_true, y_pred)
        
    def update(self):
        # Since the the loss is the log likelihood with sigmoid function,
        # the gradient of logistic loss function is y_pred - y_true
        D2 = self.y_pred - self.y_true
        #print(f"D2:\n{D2}")
        
        b_2_grad = np.mean(D2)
        
        M = D2 * self.NN.a_1
        #print(f"M:\n{M}")
        
        W_2_grad =  np.mean(M, axis=0).reshape((-1,1))
        #print(f"W_2_grad:\n{W_2_grad}")
        #print("\n-----------------------------------\n")

        M = np.dot(self.NN.W_2, D2.T)
        #print(f"M:\n{M}")
        
        D1 = M * self.NN.a_1_z_1_grad.T
        #print(f"D1:\n{D1}")
        #print(M[:,0])
        #print(self.NN.a_1_z_1_grad)
        #print(M[:,0] * self.NN.a_1_z_1_grad[0])
        #print(M[:,1] * self.NN.a_1_z_1_grad[1])
        
        b_1_grad = np.mean(D1, axis=1)
        #print(f"b_1_grad : {b_1_grad }")
        
        W_1_0 = D1 * self.X[:,0]
        #print(f"W_1_0:\n{W_1_0}")
        #print(D1[:,0] * self.X[0,0])
        
        W_1_1 = D1 * self.X[:,1]
        #print(f"W_1_1:\n{W_1_1}")
        #print(D1[:,0] * self.X[0,1])
        
        W_1_0_grad = np.mean(W_1_0, axis=1)
        W_1_1_grad = np.mean(W_1_1, axis=1)
        #print(f"W_1_0_grad:\n{W_1_0_grad}")
        #print(f"W_1_1_grad:\n{W_1_1_grad}")
        
        W_1_grad = np.vstack((W_1_0_grad, W_1_1_grad))
        #print(f"W_1_grad: {W_1_grad}")
        
        self.grads['b2'].append(b_2_grad)
        self.grads['W2'].append(W_2_grad)
        self.grads['b1'].append(b_1_grad)
        self.grads['W1'].append(W_1_grad)

        
        return self.NN.step(W_1_grad, b_1_grad, W_2_grad, b_2_grad)     