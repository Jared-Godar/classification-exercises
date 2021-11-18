import pandas as pd
import numpy as np
import os
from env import host, user, password
from sklearn.model_selection import train_test_split


########### SPLIT IRIS ##########

def split_iris(iris_df):
    '''
    Takes a prepared dataframe and splits into train, validate, and test dataframes
    '''
    iris_train, iris_test = train_test_split(iris_df, test_size = 0.2, stratify = iris_df.species, random_state = 123)
    iris_train, iris_validate = train_test_split(iris_train, test_size = .3, stratify = iris_df.species, random_state = 123)
    return iris_train, iris_validate, iris_test 


#############

def split_titanic(titanic_df):
    '''
    Takes in a dataframe and returns train, validate, and test
    '''
    titanic_train, titanic_test = train_test_split(titanic_df, test_size = 0.2, stratify = titanic_df.survived, random_state = 123)
    titanic_train, titanic_validate = train_test_split(titanic_train, test_size = .3, random_state = 123, stratify = titanic_train.survived)
    return titanic_train, titanic_validate, titanic_test

###############

def split_telco(telco_df):
    '''
    Takes in a dataframe and returns train, validate, and test
    '''
    telco_train, telco_test = train_test_split(telco_df, test_size = 0.2, stratify = telco_df.churn_Yes, random_state = 123)
    telco_train, telco_validate = train_test_split(telco_train, test_size = .3, random_state = 123, stratify = telco_train.churn_Yes)
    return telco_train, telco_validate, telco_test