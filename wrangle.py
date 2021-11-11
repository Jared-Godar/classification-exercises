import pandas as pd
import numpy as np
import os
from env import host, user, password
import acquire
import prepare
import split

######################  Titanic  ###################

acquire.get_titanic_data()
prepare.prep_titanic(titanic_df)
split.split_titanic(titanic_df)

######## IRIS #############

acquire.get_iris_data()
prepare.prep_iris(iris_df)
split.split_iris(iris_df)


####### TELCO #############

acquire.get_telco_data()
prepare.prep_telco(telco_df)
split.split_telco(telco_df)

