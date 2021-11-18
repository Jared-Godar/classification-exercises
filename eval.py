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

def f1(tp, fp, fn):
    r = recall(tp, fn)
    p = precision(tp, fp)
    f1 = (2 * r * p) / (r + p)
    return f1

def mod_eval(tp, tn, fp, fn):
    p = precision(tp, fp)
    r = recall(tp, fn)
    s = specificity(tn, fp)
    n =  npv(tn, fn)
    a = accuracy(tp, tn, fp, fn)
    f = f1(tp, fp, fn)
    return p, r, s, n, a, f



def tpr(tp, fn):
    tpr = tp/(tp+fn)
    return tpr

def fpr(fp, tn):
    fpr = fp/(tn+fp)
    return fpr

def tnr(tn, fp):
    tnr = tn/(tn+fp)
    return tnr

def fnr(fn, tp):
    fnr = fn/(tp+fn)
    return fnr

def eval_rates(tp, tn, fp, fn):
    tp = tpr(tp, fn)
    fp = fpr(fp, tn)
    tn = tnr(tn, fp)
    fn = fnr(fn, tp)
    return tp, fp, tn, fn
