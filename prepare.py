import pandas as pd
import numpy as np
import os
from env import host, user, password

############ PREPARE IRIS $$$$$$$$$$$


def prep_iris(iris_df):
    '''
    This function will accept untransformed iris data and return the prepped data
    '''
    iris_df = iris_df.drop(columns='species_id')
    iris_df.rename(columns={'species_name':'species'}, inplace=True)
    iris_dummy_df = pd.get_dummies(iris_df[['species']], dummy_na = False, drop_first = [True])
    iris_df = pd.concat([iris_df, iris_dummy_df], axis = 1)
    return iris_df

############## PREPARE TITANIC #############
    
def prep_titanic(titanic_df):
    '''
    This function will accept raw titanic data and prepare the titanic dataframe
    '''
    titanic_df = titanic_df.drop_duplicates()
    cols_to_drop = ['deck', 'embarked', 'class', 'age']
    titanic_df = titanic_df.drop(columns=cols_to_drop)
    titanic_dummy_df = pd.get_dummies(titanic_df[['sex', 'embark_town']], dummy_na = False, drop_first = [True, True])
    titanic_df = pd.concat([titanic_df, titanic_dummy_df], axis = 1)
    return titanic_df

############## PREPARE TELCO ###################

def prep_telco(telco_df):
    cols_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
    telco_df = telco_df.drop(columns=cols_to_drop)
    telco_df['total_charges'] = pd.to_numeric(telco_df['total_charges'], errors = 'coerce')
    telco_df['total_charges'] = telco_df['total_charges'].fillna(0)
    telco_df = telco_df[telco_df['total_charges'] != 0]
    telco_dummy_df = pd.get_dummies(telco_df[['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type'  ]], dummy_na = False, drop_first = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True])
    telco_df = pd.concat([telco_df, telco_dummy_df], axis = 1)
    return telco_df