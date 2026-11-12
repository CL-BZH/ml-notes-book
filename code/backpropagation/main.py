#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:11:03 2024

@author: chris
"""
from utils import Pattern2D, two_classes_pattern2D
from classifier import Classifier
import matplotlib.pyplot as plt
import numpy as np


def plot_loss_accuracy(loss_vals, accuracies):
    fig = plt.figure(figsize=(16, 8))
    fig.suptitle('Log Loss and Accuracy over iterations')
    
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(loss_vals)
    ax.grid(True)
    ax.set(xlabel='iterations', title='Log Loss')
    
    ax = fig.add_subplot(1, 2, 2)
    ax.plot(accuracies)
    ax.grid(True)
    ax.set(xlabel='iterations', title='Accuracy')
    plt.show();

if __name__ == "__main__":
    num_obs = 500
    num_batches = 10
    epochs = 20000
    #lr = 0.01
    #use_adam_optimizer = True
    lr = 0.05
    use_adam_optimizer = False
    acc =  0.
    curr_loss = 0.
    loss_vals = []
    accuracies = []
    batches = []
    
    X, y_true = two_classes_pattern2D(num_obs, Pattern2D.SQUARE, plot=False)

    classifier = Classifier(learning_rate=lr, adam_optimizer=use_adam_optimizer)
    
    for i in range(epochs):
        indexes = np.arange(num_obs) 
        np.random.shuffle(indexes)
        
        shuffled_X = [X[i,:] for i in indexes]
        shuffled_y_true = [y_true[i] for i in indexes]
        
        X_batches = np.array_split(shuffled_X, num_batches)
        y_batches = np.array_split(shuffled_y_true, num_batches)
        
        reordered_X = []
        reordered_y_true = []
        y_pred = []
        
        batch_indexes = np.arange(num_batches) 
        np.random.shuffle(batch_indexes)
    
        for idx in batch_indexes:
            
            X_batch = X_batches[idx]
            y_batch = y_batches[idx]
            
            reordered_X.append(X_batch)
            reordered_y_true.append(y_batch)
            
            ### Do a forward computation, and get the gradient
            y_pred.append(classifier.predict(X_batch, y_batch))
            #print(f"y_pred: {y_pred}")
            
            lr = classifier.update()
            
            ### Compute the loss and accuracy
            curr_loss = classifier.loss(y_pred[-1])
            loss_vals.append(curr_loss)
            acc = np.sum((y_pred[-1].flatten()>=.5) == y_batch)/len(y_batch)
            accuracies.append(acc)
    
        ## Print the loss and accuracy for every 200th iteration
        if((i%100) == 0):
            print(f'Epoch {i}, lr: {lr:.5f}, log loss: {curr_loss:.4f}, accuracy: {acc}')
        
        acc = np.mean(accuracies[-2:])
        if acc > 0.98:
            if((i%100) != 0):
                print(f'Epoch {i}, lr: {lr:.5f}, log loss: {curr_loss:.4f}, mean accuracy: {acc}')
            break
    
    plot_loss_accuracy(loss_vals, accuracies)
    
    X = np.array(reordered_X).reshape((num_obs, -1))
    y_true = np.array(reordered_y_true).reshape(-1)
    y_pred = np.array(y_pred).reshape(-1)
    
    pred1 = (y_pred >= .5)
    pred0 = (y_pred < .5)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # true predictions
    data = X[pred1 & (y_true==1)]
    if len(data) > 0:
        print(f"True positive: {len(data)}")
        ax.plot(data[:,0], data[:,1], 'go', label='true positives')
    
    data = X[pred0 & (y_true==0)]
    if len(data) > 0:
        print(f"True negative: {len(data)}")
        ax.plot(data[:,0], data[:,1], 'bx', label='true negatives')
     
    # false predictions
    data = X[pred1 & (y_true==0)]
    errors = len(data)
    if len(data) > 0:
        print(f"False positive: {len(data)}")
        ax.plot(data[:,0], data[:,1], 'mx', label='false positives')
    
    data = X[pred0 & (y_true==1)]
    errors += len(data)
    if len(data) > 0:
        print(f"False negative: {len(data)}")
        ax.plot(data[:,0], data[:,1], 'mo', label='false negatives')
    
    print(f"\nNumber of errors: {errors}\n")
    
    ax.set(title='Truth vs Prediction')
    ax.legend(bbox_to_anchor=(1.05, 1), fancybox=True, shadow=True, loc='upper left', fontsize='x-large')
    ax.axis('equal')
    plt.tight_layout()
    plt.show();