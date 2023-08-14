import env
import os
import pandas as pd

def get_titanic_data(
    db,
    user=env.user,
    password=env.password,
    host=env.host):
    '''
    get_titanic_data will first check if the file_loc= df_titanic.csv exists. If present it will read from csv. Else it will query data from a specified positional argument (string literal)
    schema from an assumed user, password, and host provided
    that were imported from an env, then cache the information in a csv
    
    return: a pandas dataframe
    '''
    file_loc='df_titanic.csv'
    if os.path.exists(file_loc):
        df_titanic = pd.read_csv(file_loc, index_col=0)
    else:
        query = '''SELECT * FROM passengers'''
        connection = f'mysql+pymysql://{user}:{password}@{host}/{db}'
        df_titanic = pd.read_sql(query, connection)
        df_titanic.to_csv(file_loc, index=True)
    return df_titanic

def get_iris_data(
    db,
    user=env.user,
    password=env.password,
    host=env.host):
    '''
    get_iris_data will first check if the file_loc= df_iris.csv exists. If present it will read from csv. Else it will query data from a specified positional argument (string literal)
    schema from an assumed user, password, and host provided
    that were imported from an env, then cache the information in a csv
    
    return: a pandas dataframe
    '''
    file_loc='df_iris.csv'
    if os.path.exists(file_loc):
        df_iris = pd.read_csv(file_loc, index_col=0)
    else:
        query = '''SELECT * FROM measurements JOIN species USING (species_id)'''
        connection = f'mysql+pymysql://{user}:{password}@{host}/{db}'
        df_iris = pd.read_sql(query, connection)
        df_iris.to_csv(file_loc, index=True)
    return df_iris

def get_telco_data(
    db,
    user=env.user,
    password=env.password,
    host=env.host):
    '''
    get_telco_data will first check if the file_loc= df_telco.csv exists. If present it will read from csv. Else it will query data from a specified positional argument (string literal)
    schema from an assumed user, password, and host provided
    that were imported from an env, then cache the information in a csv
    
    return: a pandas dataframe
    '''
    file_loc='df_telco.csv'
    if os.path.exists(file_loc):
        df_telco = pd.read_csv(file_loc, index_col=0)
    else:
        query = '''SELECT * FROM customers JOIN contract_types USING (contract_type_id) JOIN internet_service_types USING (internet_service_type_id) JOIN payment_types USING (payment_type_id) '''
        connection = f'mysql+pymysql://{user}:{password}@{host}/{db}'
        df_telco = pd.read_sql(query, connection)
        df_telco.to_csv(file_loc, index=True)
    return df_telco