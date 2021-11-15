import pandas as pd
import numpy as np
import os
from env import host, user, password
import acquire
import prepare
import split

#######  Titanic  #############

def wrangle_titanic():
    titanic_df = acquire.get_titanic_data()
    titanic_df = prepare.prep_titanic(titanic_df)
    titanic_train, titanic_validate, titanic_test = split.split_titanic(titanic_df)
    return titanic_train, titanic_validate, titanic_test

######## IRIS ##################

def wrangle_iris():
    iris_df = acquire.get_iris_data()
    iris_df = prepare.prep_iris(iris_df)
    iris_train, iris_validate, iris_test =split.split_iris(prepare.prep_iris(acquire.get_iris_data()))
    return iris_train, iris_validate, iris_test 


####### TELCO ###################

def wrangle_telco():
    telco_df = acquire.get_telco_data()
    telco_df = prepare.prep_telco(telco_df)
    telco_train, telco_validate, telco_test = split.split_telco(telco_df)
    return telco_train, telco_validate, telco_test

