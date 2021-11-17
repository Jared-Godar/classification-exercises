import pandas as pd
import numpy as np
import os

def precision(tp, fp):
    precision = tp/(tp+fp)
    return precision

def recall(tp, fn):
    recall = tp/(tp+fn)
    return recall

def specificity(tn, fp):
    specificity = tn/(fp+tn)
    return specificity

def npv(tn, fn):
    npv = tn/(tn+fn)
    return npv

def accuracy(tp, tn, fp, fn):
    accuracy = (tp+tn)/(tp+fp+fn+tn)
    return accuracy

def mod_eval(tp, tn, fp, fn):
    precision = precision(tp, fp)
    recall = recall(tp, fn)
    specificity = specificity(tn, fp, tn)
    npv =  npv(tn, fn)
    accuracy = accuracy(tp, tn, fp, fn)
    return precision, recall, specificity, npv, accuracy
